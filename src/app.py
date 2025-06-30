import streamlit as st
import re
import time
import copy # GỢI Ý: Import thư viện copy để tạo bản sao sâu
from src.utils import *
from PIL import Image
import random

uit = Image.open('./assets/logo-uit.png')

st.set_page_config(
    page_title="UIT@CS | ToiLaKiet | Kén rể",
    page_icon=uit,
    layout="wide"
)

# --- Dữ liệu mẫu ---
DEFAULT_MAP_DATA = """
1 0 1 0 1 0 0 0 0 1 0 0 0 0 0 1 1 0 1 0 0 0 1 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0
0 0 1 0 1 0 0 0 0 1 0 0 1 0 1 1 1 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 1 0 1 0 1 0 1 1 0 0 1 1 1 0 0 1 0 0 0 1
0 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 0 0 0 1 1
0 0 1 1 0 0 0 1 0 0 1 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1
0 0 0 1 1 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0
0 0 0 1 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0 1 1 0 1 0 0 0 1 0 0 0 0 0 1 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0 0 1 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 1 1 0 1 0 0 0 0 0 0 0 1
0 0 1 0 1 1 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 1 1 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0 1 1 0 0 1
0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 1 0 0 1 0
0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 0 0 1 1 0 0 1 0 0 1 0 0 0 0 1 1 0 0 1 0 0 0 0 0 1 1 0 1 1
0 1 1 1 0 1 0 0 1 1 0 1 1 0 0 0 0 1 1 1 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1
0 0 0 0 0 1 1 1 1 1 0 1 0 0 1 1 0 0 1 1 0 0 1 0 0 1 1 1 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 1 1 1 1 1 0
0 1 0 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 0 0 0
0 0 0 1 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 1 1 0
0 0 0 1 1 1 1 0 0 0 0 0 0 0 1 1 1 1 1 0 0 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1
0 0 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1 1 1 1 0 0 1 0 0 0 0 1 0 0 1 1 1 0 1 0 0 1 0 1 0 0
0 1 0 0 1 0 0 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 1 0 0 0 1 0 0 1 1 0 1 1
1 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 1 0 0 0 0 1 1 0 0 1 1 0
0 0 0 1 1 0 0 0 1 0 0 1 1 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 0 1 0 1 0 1 0 0 1 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0 1 1
0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 1 0 1 0 0 0 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 1 0 0 0 0 1 0 0 0
1 0 0 0 1 0 0 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 1 0 0 1 1 1 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 1 1 1 0 0 1 1 0 1
0 0 0 0 0 0 0 1 1 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 0 1 0
0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1 1 0 1 1 1 0 0 0 0 1 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 0 0 0 1 0 0 1
0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 1 0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0
0 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0 0 1 0 0 1 1 0 0 0 0 0
0 0 0 1 0 0 0 1 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 0 1
1 0 0 0 0 1 0 0 1 1 0 0 0 1 0 0 0 0 1 1 0 1 1 1 1 0 0 1 1 1 0 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 1 0
1 1 0 0 0 1 1 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 1 1 0 1 1 1
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 1 1 1 0 0 0 0 1
0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 1 0 0
1 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 1 1 0 0 0 1 0 0 0 1 0 0 1 1 0 0 1 1 0 1 1 0 0 0 0 0 0 0 0 1
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 1 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0 1 1 0 0 0
0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 1 1 0 0 0 1 1
0 0 1 1 0 0 1 0 1 0 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 1 1
0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 1
1 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 0 0 1
0 1 0 0 0 1 0 1 0 1 1 0 0 1 1 0 1 1 1 1 0 0 1 0 1 0 0 0 0 1 1 0 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 1
1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 0 0 0 0 0 0 1 0 1 0 1 1
0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 1
1 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 1 1 0 0 1 1 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 0 1 0 0 0 1 1 1 0 0 1 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 1 1 1 0 1 0
1 0 1 1 1 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 1 1 1 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 1 1 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 0 0 1 1 0 1 1 0 1 0 1 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 0 1 1 0 0 1 0 1 1 1 0 0 0 0 1 0 0 1 0 0 0 0 0 1
0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0 1 0 1 0 0 0 1 1 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0
""".strip()


# --- Các hàm trợ giúp ---

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
        map_str += f"<div style='font-size: 1vw; line-height: 1.2; white-space: nowrap;'>{row_str}</div>"

    html_content = f"<div style='overflow-x: auto;'>{map_str}</div>"
    if placeholder:
        placeholder.markdown(html_content, unsafe_allow_html=True)
    else:
        st.markdown(html_content, unsafe_allow_html=True)

# --- Khởi tạo Session State ---
if 'matrix_data' not in st.session_state:
    st.session_state.matrix_data = None
if 'map_confirmed' not in st.session_state:
    st.session_state.map_confirmed = False
if 'prince_pos' not in st.session_state:
    st.session_state.prince_pos = None
if 'princess_pos' not in st.session_state:
    st.session_state.princess_pos = None

# --- Giao diện ứng dụng ---
st.title("🗺️ UIT@CS112 | Kén Rể Cho Đức Vua")
st.header("Bước 1: Nhập dữ liệu bản đồ")
map_input_text = st.text_area(
    "Dán dữ liệu ma trận của bạn vào đây (0: đường đi, 1: đá).",
    value=DEFAULT_MAP_DATA, height=250
)
if st.button("Tạo Bản Đồ", type="primary", icon="⚙️"):
    parsed_matrix = parse_matrix_from_text(map_input_text)
    if parsed_matrix:
        st.session_state.matrix_data = parsed_matrix
        st.session_state.rows = len(parsed_matrix)
        st.session_state.cols = len(parsed_matrix[0])
        st.session_state.map_confirmed = True
        # Reset các trạng thái khác
        st.session_state.prince_pos = None
        st.session_state.princess_pos = None
        st.success(f"Bản đồ đã được tạo thành công với kích thước {st.session_state.rows}x{st.session_state.cols}!")
        print(parsed_matrix)
        st.rerun()
    else:
        st.session_state.map_confirmed = False

if st.session_state.map_confirmed:
    st.divider()
    display_map(st.session_state.matrix_data)
    st.divider()

    st.header("Bước 2: Đặt vị trí xuất phát")
    st.caption(f"Tọa độ dòng từ 0 đến {st.session_state.rows - 1}, tọa độ cột từ 0 đến {st.session_state.cols - 1}.")

    with st.form(key="positions_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hoàng tử 🤴")
            prince_x = st.number_input("Dòng của Hoàng tử", 0, st.session_state.rows - 1, 0, 1)
            prince_y = st.number_input("Cột của Hoàng tử", 0, st.session_state.cols - 1, 0, 1)
        with col2:
            st.subheader("Công chúa 👸")
            princess_x = st.number_input("Dòng của Công chúa", 0, st.session_state.rows - 1, st.session_state.rows - 1, 1)
            princess_y = st.number_input("Cột của Công chúa", 0, st.session_state.cols - 1, st.session_state.cols - 1, 1)
        
        # GỢI Ý: Tách nút "Đặt vị trí" và "Tìm đường" ra
        submit_positions = st.form_submit_button("Xác nhận vị trí")

    if submit_positions:
        prince_pos = (prince_x, prince_y)
        princess_pos = (princess_x, princess_y)
        valid = True
        if st.session_state.matrix_data[prince_x][prince_y] == 1:
            st.error(f"Vị trí Hoàng tử ({prince_x}, {prince_y}) là đá! 🪨")
            valid = False
        if st.session_state.matrix_data[princess_x][princess_y] == 1:
            st.error(f"Vị trí Công chúa ({princess_x}, {princess_y}) là đá! 🪨")
            valid = False
        if prince_pos == princess_pos:
            st.error("Vị trí Hoàng tử và Công chúa không được trùng nhau!")
            valid = False
        
        if valid:
            st.session_state.prince_pos = prince_pos
            st.session_state.princess_pos = princess_pos
            st.success("Đã xác nhận vị trí! Nhấn nút 'Tìm đường' để bắt đầu.")
        else:
            st.session_state.prince_pos = None
            st.session_state.princess_pos = None

    # Chỉ hiển thị bản đồ với nhân vật và nút "Tìm đường" sau khi vị trí hợp lệ
    if st.session_state.prince_pos:
        st.header("Bước 3: Bắt đầu hành trình")
        st.divider()
        map_placeholder = st.empty()
        display_map(st.session_state.matrix_data, st.session_state.prince_pos, st.session_state.princess_pos,placeholder=map_placeholder)
        st.divider()
        if st.button("Tìm đường đi!", type="primary", icon="🏃‍♂️"):
            # GỢI Ý: Sử dụng spinner để thông báo cho người dùng
            with st.spinner("Hoàng tử đang dò đường..."):
                path = kenre_python_literal(
                    st.session_state.matrix_data,
                    st.session_state.prince_pos[0], st.session_state.prince_pos[1],
                    st.session_state.princess_pos[0], st.session_state.princess_pos[1]
                )
            
            # Kiểm tra xem có tìm thấy đường đi không
            if path != -1:
                st.info(f"Đã tìm thấy đường đi với {len(path)} bước. Bắt đầu di chuyển...")
                # Tạo bản sao của ma trận để animation không làm thay đổi bản gốc
                animated_matrix = copy.deepcopy(st.session_state.matrix_data)
                animated_matrix[st.session_state.prince_pos[0]][st.session_state.prince_pos[1]] = 2
                for i, pos in enumerate(path):
                    # Đánh dấu đường đi
                    animated_matrix[pos[0]][pos[1]] = 2
                    
                    # Vị trí hoàng tử hiện tại là pos
                    current_prince_pos = pos
                    
                    # Hiển thị frame hiện tại
                    display_map(
                        animated_matrix,
                        current_prince_pos,
                        st.session_state.princess_pos,
                        placeholder=map_placeholder
                    )
                    time.sleep(0.15) 
                
                st.success("Thành công! Hoàng tử đã cứu được công chúa! ❤️")
                st.balloons()
            else:
                st.error("Rất tiếc, không có đường nào để Hoàng tử tìm Công chúa. 💔")
