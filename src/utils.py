from collections import deque
import sys
import streamlit as st
import re
import time
import copy # GỢI Ý: Import thư viện copy để tạo bản sao sâu
from utils import *
import random
import numpy as np 

def kenre_python_literal(bando, w_h, w_c, p_h, p_c):
    m = len(bando)
    n = len(bando[0])
    
    # Hàng đợi, tương đương q_ready
    q_ready = deque([(w_h, w_c)])
    
    # Ma trận check
    check = [[False for _ in range(n)] for _ in range(m)]
    check[w_h][w_c] = False
    
    # Ma trận mark, dùng để lưu ô cha của ô hiện tại 
    # Khởi tạo với giá trị không hợp lệ, ví dụ (-1, -1)
    mark = [[(-1, -1) for _ in range(n)] for _ in range(m)]

    # 8 hướng di chuyển
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while q_ready:
        curr_h, curr_c = q_ready.popleft()

        # Nếu tìm thấy đích
        if curr_h == p_h and curr_c == p_c:
            temp = []
            hours = 0
            o_h, o_c = p_h, p_c
            while not (o_h == w_h and o_c == w_c):
                hours += 1
                temp.append((o_h, o_c))
                o_h, o_c = mark[o_h][o_c]

            return temp[::-1]# Trả về số giờ và đường đi từ đích về nguồn

        # Duyệt 8 hướng xung quanh
        for dr, dc in directions:
            next_h, next_c = curr_h + dr, curr_c + dc

            if (0 <= next_h < m and 0 <= next_c < n and
                bando[next_h][next_c] == 0 and not check[next_h][next_c]):
                
                # Đánh dấu đã thăm
                check[next_h][next_c] = True
                # Lưu ô cha
                mark[next_h][next_c] = (curr_h, curr_c)
                # Thêm vào hàng đợi
                q_ready.append((next_h, next_c))
    
    return -1 # Không tìm thấy đường đi
def parse_matrix_from_text(text_data):
    matrix = []
    lines = text_data.strip().split('\n')
    try:
        for i, line in enumerate(lines):
            line = line.strip()
            if not line: continue
            row_str = re.split(r'\s+', line)
            row_int = [int(num) for num in row_str]
            if any(cell not in [0, 1] for cell in row_int):
                st.error(f"Lỗi ở dòng {i+1}: Dữ liệu chứa giá trị không phải 0 hoặc 1.")
                return None
            matrix.append(row_int)
        if not matrix:
            st.warning("Dữ liệu đầu vào trống.")
            return None
        first_row_len = len(matrix[0])
        if any(len(r) != first_row_len for r in matrix):
            st.error("Lỗi: Các dòng có số cột không đồng nhất.")
            return None
        # GỢI Ý: Bỏ matrix.reverse() đi. Tọa độ (0,0) theo list index tự nhiên là góc trên bên trái.
        # Điều này giúp logic tọa độ nhất quán hơn.
        return matrix
    except ValueError:
        st.error("Lỗi: Dữ liệu chứa ký tự không phải là số.")
        return None
    except Exception as e:
        st.error(f"Đã xảy ra lỗi không xác định: {e}")
        return None
def convert_matrix_to_text(matrix):
    """
    Chuyển đổi một ma trận (list of lists) thành một chuỗi văn bản.

    Mỗi hàng của ma trận sẽ trở thành một dòng trong chuỗi,
    và các phần tử trong mỗi hàng được nối với nhau bằng một khoảng trắng.

    Ví dụ:
        Input: [[0, 1, 0], [1, 1, 0]]
        Output: "0 1 0\n1 1 0"

    Args:
        matrix (list[list[int]]): Ma trận chứa các số nguyên (0 hoặc 1).

    Returns:
        str: Chuỗi văn bản biểu diễn ma trận.
             Trả về một chuỗi rỗng nếu ma trận đầu vào không hợp lệ hoặc rỗng.
    """
    # Xử lý trường hợp đầu vào không phải là list hoặc là list rỗng
    if matrix is None: # Hoạt động đúng với mọi kiểu dữ liệu
        return ""

    # Sử dụng list comprehension để chuyển đổi từng hàng thành một chuỗi
    # 1. `map(str, row)`: Chuyển mọi số trong `row` thành chuỗi.
    # 2. `" ".join(...)`: Nối các chuỗi số lại với nhau bằng khoảng trắng.
    # 3. `for row in matrix`: Lặp qua từng hàng của ma trận.
    row_strings = [" ".join(map(str, row)) for row in matrix]

    # Nối tất cả các chuỗi hàng lại với nhau bằng ký tự xuống dòng
    return "\n".join(row_strings)
def display_map(matrix, prince_pos=None, princess_pos=None, placeholder=None):
    """
    Hiển thị bản đồ với một giải pháp duy nhất, thanh lịch:
    - Bản đồ luôn nằm gọn trong một "hộp" có kích thước tương đối với màn hình.
    - Các ô bên trong tự động co giãn để lấp đầy "hộp" và luôn là hình vuông.
    - Nội dung (emoji) được đảm bảo không bao giờ tràn ra ngoài làm vỡ layout.
    """
    # Định nghĩa CSS.
    css_styles = """
    <style>
        .map-wrapper {
            /* Container này giúp căn giữa bản đồ */
            width: 100%;
            display: flex;
            justify-content: center;
        }
        .map-container {
            /* Đây là "cái hộp" có kích thước cố định so với màn hình */
            width: 45vw; /* Chiếm 45% chiều rộng màn hình */
            max-width: 90vh; /* Ngăn bản đồ quá lớn trên màn hình siêu rộng */
            min-width: 300px; /* Đảm bảo bản đồ không quá nhỏ trên màn hình hẹp */

            /* Các thuộc tính của CSS Grid */
            display: grid;
            /* CHÌA KHÓA #1: Chia chiều rộng thành N cột bằng nhau (1fr = 1 phần) */
            grid-template-columns: repeat(var(--cols), 1fr);
            gap: 2px;
            
            border: 2px solid #555;
            border-radius: 5px;
            padding: 2px;
            background-color: #555;
        }
        .map-cell {
            /* CHÌA KHÓA #2: Tự động làm cho chiều cao bằng chiều rộng, tạo ra ô vuông hoàn hảo */
            aspect-ratio: 1 / 1;

            /* Căn giữa nội dung (emoji) trong ô */
            display: flex;
            justify-content: center;
            align-items: center;

            /* Kích thước emoji co giãn, tỉ lệ với chiều nhỏ hơn của màn hình */
            font-size: 2vmin;
            
            /* CHÌA KHÓA #3: "LÁ CHẮN BẢO VỆ" - Đảm bảo nội dung không bao giờ tràn ra ngoài */
            overflow: hidden;

            border-radius: 3px;
        }
        /* Định nghĩa màu sắc cho từng loại ô */
        .path { background-color: #e9ecef; }
        .wall { background-color: #6c757d; }
        .trail { background-color: #87CEEB; }
    </style>
    """

    matrix_np = np.array(matrix)
    rows, cols = matrix_np.shape

    # Bắt đầu xây dựng chuỗi HTML
    map_cells_html = ""
    for r_idx in range(rows):
        for c_idx in range(cols):
            pos = (r_idx, c_idx)
            content = ""
            cell_class = ""
            
            if prince_pos and pos == prince_pos:
                content = "🤴"
                cell_class = "path"
            elif princess_pos and pos == princess_pos:
                content = "👸"
                cell_class = "path"
            else:
                cell_type = matrix_np[r_idx, c_idx]
                if cell_type == 2:
                    cell_class = "trail"
                elif cell_type == 1:
                    cell_class = "wall"
                    content = "🪨"
                else:
                    cell_class = "path"

            map_cells_html += f'<div class="map-cell {cell_class}">{content}</div>'

    # Ghép CSS và HTML
    final_html = f"""
    {css_styles}
    <div class="map-wrapper">
        <div class="map-container" style="--cols: {cols};">
            {map_cells_html}
        </div>
    </div>
    """

    # Xử lý đúng cả hai trường hợp hiển thị
    if placeholder:
        placeholder.markdown(final_html, unsafe_allow_html=True)
    else:
        st.markdown(final_html, unsafe_allow_html=True)
