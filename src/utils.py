from collections import deque
import sys
import streamlit as st
import re
import time
import copy # GỢI Ý: Import thư viện copy để tạo bản sao sâu
from utils import *
import random

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
    map_str = ""
    # GỢI Ý: Chuyển sang một bảng màu khác để dễ nhìn hơn
    # ⬜: Đường đi (0), 🪨: Đá (1), 🟩: Đường đã đi (2), 🤴: Hoàng tử, 👸: Công chúa

    for r_idx, row in enumerate(matrix):
        row_str = ""
        for c_idx, cell in enumerate(row):
            pos = (r_idx, c_idx)
            if prince_pos and pos == prince_pos:
                row_str += "🤴"
            elif princess_pos and pos == princess_pos:
                row_str += "👸"
            elif cell == 2: # Đường đã đi
                row_str += "🟩"
            elif cell == 1: # Đá
                row_str += "🪨"
            else: # Đường đi
                row_str += "⬜"
            row_str += "  "
        map_str += f"<div style='font-size: 0.75vw; line-height: 1.2; white-space: nowrap;'>{row_str}</div>"

    html_content = f"<div style='overflow-x: auto;'>{map_str}</div>"
    if placeholder:
        placeholder.markdown(html_content, unsafe_allow_html=True)
    else:
        st.markdown(html_content, unsafe_allow_html=True)

