import streamlit as st
import re
import time
import copy
from utils import * # Giả sử utils.py đã có các hàm cần thiết
from PIL import Image
import numpy as np

# --- Cấu hình trang và Khởi tạo ---
uit = Image.open('./assets/logo-uit.png')
st.set_page_config(page_title="UIT@CS | ToiLaKiet | Kén rể", page_icon=uit, layout="wide")

# Dữ liệu mẫu (giữ nguyên)
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
1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 1 0 0 1 0 0 0 0 0 0 1 0 1 0 1 1
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

# --- Khởi tạo Session State ---
if 'matrix_data' not in st.session_state:
    st.session_state.matrix_data = None
if 'map_confirmed' not in st.session_state:
    st.session_state.map_confirmed = False
if 'prince_pos' not in st.session_state:
    st.session_state.prince_pos = None
if 'princess_pos' not in st.session_state:
    st.session_state.princess_pos = None
# --- THAY ĐỔI 1: Thêm biến trạng thái để khóa UI ---
if 'processing' not in st.session_state:
    st.session_state.processing = False

# --- Giao diện ứng dụng ---
st.title("🗺️ UIT@CS112 | Kén Rể | Đi tìm công chúa")
st.header("Bước 1: Nhập dữ liệu bản đồ")

# --- THAY ĐỔI 2: Thêm `disabled` vào tất cả các widget tương tác ---
is_disabled = st.session_state.processing

map_input_text = st.text_area(
    "Dán dữ liệu ma trận của bạn vào đây (0: đường đi, 1: đá).",
    value=convert_matrix_to_text(st.session_state.matrix_data) if st.session_state.matrix_data is not None else DEFAULT_MAP_DATA,
    height=250,
    disabled=is_disabled
)

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("Tạo Bản Đồ", type="primary", icon="⚙️", disabled=is_disabled):
        # Không cần khóa UI ở đây vì hành động này nhanh
        st.session_state.map_confirmed = False
        st.session_state.matrix_data = None
        parsed_matrix = parse_matrix_from_text(map_input_text)
        if parsed_matrix:
            st.session_state.matrix_data = parsed_matrix
            st.session_state.rows = len(parsed_matrix)
            st.session_state.cols = len(parsed_matrix[0])
            st.session_state.map_confirmed = True
            st.session_state.prince_pos = None
            st.session_state.princess_pos = None
            st.rerun()
        else:
            st.session_state.map_confirmed = False
with col2:
    if st.button("Sinh ngẫu nhiên bản đồ", type="secondary", icon="🎲", disabled=is_disabled):
        st.session_state.map_confirmed = True
        st.session_state.rows = np.random.randint(3, 101)
        st.session_state.cols = np.random.randint(3, 101)
        st.session_state.matrix_data = np.random.randint(0, 2, size=(st.session_state.rows, st.session_state.cols))
        st.rerun()
with col3:
    if st.button("Đặt Lại", type="secondary", icon="🔄", disabled=is_disabled):
        # Xóa tất cả trạng thái và rerun
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

if st.session_state.map_confirmed:
    st.success(f"Bản đồ đã được tạo thành công với kích thước {st.session_state.rows}x{st.session_state.cols}!")
    st.divider()
    display_map(st.session_state.matrix_data)
    st.divider()

    st.header("Bước 2: Đặt vị trí xuất phát")
    st.caption(f"Tọa độ dòng từ 0 đến {st.session_state.rows - 1}, tọa độ cột từ 0 đến {st.session_state.cols - 1}.")

    with st.form(key="positions_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hoàng tử 🤴")
            prince_x = st.number_input("Dòng của Hoàng tử", 0, st.session_state.rows - 1, 0, 1, disabled=is_disabled)
            prince_y = st.number_input("Cột của Hoàng tử", 0, st.session_state.cols - 1, 0, 1, disabled=is_disabled)
        with col2:
            st.subheader("Công chúa 👸")
            princess_x = st.number_input("Dòng của Công chúa", 0, st.session_state.rows - 1, st.session_state.rows - 1, 1, disabled=is_disabled)
            princess_y = st.number_input("Cột của Công chúa", 0, st.session_state.cols - 1, st.session_state.cols - 1, 1, disabled=is_disabled)

        submit_positions = st.form_submit_button("Xác nhận vị trí", disabled=is_disabled)

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

    if st.session_state.prince_pos:
        st.header("Bước 3: Bắt đầu hành trình")
        st.divider()
        map_placeholder = st.empty()
        display_map(st.session_state.matrix_data, st.session_state.prince_pos, st.session_state.princess_pos, placeholder=map_placeholder)
        st.divider()

        if st.button("Tìm đường đi!", type="primary", icon="🏃‍♂️", disabled=is_disabled):
            # --- THAY ĐỔI 3: Sử dụng try...finally để đảm bảo UI luôn được mở khóa ---
            st.session_state.processing = True
            st.rerun() # Rerun ngay để vô hiệu hóa các nút

# --- THAY ĐỔI 4: Tách logic xử lý nặng ra khỏi luồng chính ---
# Khối code này chỉ chạy khi `processing` là True
if st.session_state.get('processing', False):
    try:
        # Lấy lại các biến cần thiết từ session state
        matrix = st.session_state.matrix_data
        prince_pos = st.session_state.prince_pos
        princess_pos = st.session_state.princess_pos
        
        # Tạo placeholder ở đây để nó không bị ảnh hưởng bởi các lần rerun trước
        st.header("Bước 3: Bắt đầu hành trình")
        st.divider()
        map_placeholder = st.empty()
        st.divider()

        with st.spinner("Hoàng tử đang dò đường..."):
            path = kenre_python_literal(matrix, prince_pos[0], prince_pos[1], princess_pos[0], princess_pos[1])
        print(path)
        if path != -1:
            st.info(f"Đã tìm thấy đường đi với {len(path)} bước. Bắt đầu di chuyển...")
            animated_matrix = copy.deepcopy(matrix)
            animated_matrix[prince_pos[0]][prince_pos[1]] = 2
            
            for i, pos in enumerate(path):
                animated_matrix[pos[0]][pos[1]] = 2
                current_prince_pos = pos
                display_map(animated_matrix, current_prince_pos, princess_pos, placeholder=map_placeholder)
                time.sleep(0.15)
            
            st.success("Thành công! Hoàng tử đã cứu được công chúa! ❤️")
            st.balloons()
        else:
            st.error("Rất tiếc, không có đường nào để Hoàng tử tìm Công chúa. 💔")
    finally:
        # Dù thành công hay thất bại, luôn mở khóa UI
        st.session_state.processing = False
        st.rerun() # Rerun lần cuối để kích hoạt lại các nút
