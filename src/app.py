import streamlit as st
import re
import time
import copy # GỢI Ý: Import thư viện copy để tạo bản sao sâu
from utils import *
from PIL import Image
import random
import numpy as np

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
st.title("🗺️ UIT@CS112 | Kén Rể | Đi tìm công chúa")
st.header("Bước 1: Nhập dữ liệu bản đồ")
map_input_text = st.text_area(
    "Dán dữ liệu ma trận của bạn vào đây (0: đường đi, 1: đá).",
    value=convert_matrix_to_text(st.session_state.matrix_data) if st.session_state.matrix_data != None else DEFAULT_MAP_DATA,
    height=250
)
# Tạo 2 cột
col1, col2, col3 = st.columns([1,1,1]) 
st.markdown("""
<style>
    div[data-testid="column"] {
        padding: 0 5px; /* Giảm khoảng cách giữa các cột */
    }
</style>
""", unsafe_allow_html=True)

with col1:
    if st.button("Tạo Bản Đồ", type="primary", icon="⚙️"):
        st.session_state.map_confirmed = False  
        st.session_state.matrix_data = None  # Reset dữ liệu bản đồ
        parsed_matrix = parse_matrix_from_text(map_input_text)
        if parsed_matrix:
            time.sleep(0.5)  # Giả lập thời gian xử lý
            st.session_state.matrix_data = parsed_matrix
            st.session_state.rows = len(parsed_matrix)
            st.session_state.cols = len(parsed_matrix[0])
            st.session_state.map_confirmed = True
            # Reset các trạng thái khác
            st.session_state.prince_pos = None
            st.session_state.princess_pos = None
            st.rerun() # Làm mới trang để hiển thị bản đồ mới
        else:
            st.session_state.map_confirmed = False
with col2:
    if st.button("Sinh ngẫu nhiên bản đồ", type="secondary", icon="🎲"):
        st.session_state.map_confirmed = True
        # Randomly choose rows and columns between 3 and 100
        st.session_state.rows = np.random.randint(3, 101)
        st.session_state.cols = np.random.randint(3, 101)
        # Generate matrix with random 0 or 1
        st.session_state.matrix_data = np.random.randint(0, 2, size=(st.session_state.rows, st.session_state.cols))
with col3:
    if st.button("Đặt Lại", type="secondary", icon="🔄"):
        st.session_state.matrix_data = None
        st.session_state.map_confirmed = False
        st.session_state.prince_pos = None
        st.session_state.princess_pos = None
        st.rerun()  # Làm mới trang để xoá bản đồ


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
