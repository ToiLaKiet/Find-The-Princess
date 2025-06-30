# 🤴 Tìm Đường Cứu Công Chúa (Thử Thách Kén Rể)

Đồ án môn học ứng dụng thuật toán **BFS (Breadth-First Search)** để tìm đường đi ngắn nhất trên bản đồ dạng lưới. Ứng dụng được xây dựng bằng Python và có giao diện trực quan hóa bằng Streamlit.

**Sinh viên thực hiện:**
- **Họ và Tên:** `Võ Anh Kiệt`
- **MSSV:** `23520825`
- **Lớp:** `CS112.P22`

---

## 📜 Sơ Lược Hành Trình

- [🎯 Mục Tiêu Bài Toán](#-mục-tiêu-bài-toán)
- [💡 Ý Tưởng và Giải Pháp](#-ý-tưởng-và-giải-pháp)
- [📌 Test Case Mẫu](#-test-case-mẫu)
- [🕹️ Tính Năng Mở Rộng](#-tính-năng-mở-rộng)
- [⚠️ Hạn Chế](#-hạn-chế)
- [📂 Cấu Trúc Thư Mục](#-cấu-trúc-thư-mục)
- [⚙️ Hướng Dẫn Cài Đặt và Chạy](#-hướng-dẫn-cài-đặt-và-chạy)
- [🛠️ Công Nghệ Sử Dụng](#-công-nghệ-sử-dụng)
- [📬 Thông Tin Liên Hệ](#-thông-tin-liên-hệ)

## 🎯 Mục Tiêu Bài Toán

Bài toán yêu cầu tìm **đường đi ngắn nhất** cho một hiệp sĩ trên bản đồ dạng lưới (`m x n`) để đến được hoàng cung cứu công chúa.

1.  **Bản đồ:** Một lưới hình chữ nhật kích thước `m x n`, với các ô đi được (`0`) và các ô là chướng ngại vật không đi được (`1`).
2.  **Di chuyển:** Hiệp sĩ có thể di chuyển từ một ô sang 8 ô lân cận (ngang, dọc, và chéo). Mỗi bước đi tốn **1 canh giờ**.
3.  **Hệ tọa độ:** Góc dưới cùng bên trái của bản đồ có tọa độ `(0, 0)`.
4.  **Mục tiêu:** Tính toán thời gian (số bước đi) tối thiểu để đi từ vị trí của hiệp sĩ đến hoàng cung. Nếu không có đường đi, trả về `-1`.

---

## 💡 Ý Tưởng và Giải Pháp

Để giải quyết bài toán tìm đường đi ngắn nhất trên một đồ thị không có trọng số (hoặc các cạnh có cùng trọng số), thuật toán **Tìm kiếm theo chiều rộng (Breadth-First Search - BFS)** là lựa chọn tối ưu.

### Nguyên lý hoạt động của BFS:
1.  **Khởi tạo:**
    *   Bắt đầu từ đỉnh xuất phát (vị trí của hiệp sĩ).
    *   Sử dụng một `hàng đợi (queue)` để lưu trữ các ô sẽ được duyệt.
    *   Sử dụng một mảng 2D `check` để đánh dấu các ô đã đi qua, tránh đi lại và tạo vòng lặp vô tận.
    *   Sử dụng một mảng 2D `mark` để lưu toạ độ của ô được đi liền trước (tức là ô "cha" của ô hiện tại), giúp truy vết lại đường đi.

2.  **Quá trình duyệt:**
    *   Lấy ô đầu tiên trong hàng đợi.
    *   Kiểm tra xem ô đó có phải là vị trí của công chúa không. Nếu phải thì truy vết ngược từ mảng `mark` để tìm ra đường đi và kết thúc. Nếu không, tiếp tục.
    *   Duyệt qua tất cả các ô lân cận (8 hướng di chuyển) của ô hiện tại.
    *   Với mỗi ô lân cận:
        *   Kiểm tra xem nó có nằm trong phạm vi của bản đồ không.
        *   Kiểm tra xem ô đó có phải là chướng ngại vật (`1`) hay đã được đánh dấu (`check`) chưa.
        *   Nếu ô lân cận hợp lệ, đánh dấu nó là đã đi qua (`check`), lưu tọa độ của ô hiện tại vào mảng `mark`, và thêm nó vào hàng đợi.
    *   Lặp lại quá trình này cho đến khi hàng đợi rỗng hoặc tìm thấy công chúa.
3.  **Kết quả:**
    *   Nếu vòng lặp kết thúc mà chưa tìm thấy đích, có nghĩa là không tồn tại đường đi. Trả về `-1`.
    *   Ngược lại, trả về mảng chứa các tọa độ của đường đi từ vị trí của hiệp sĩ đến công chúa.

### Chú ý về hệ tọa độ:
Đề bài quy định tọa độ `(x, y)` với `(0, 0)` ở góc dưới-trái. Khi làm việc với mảng 2D trong C++ (hoặc các ngôn ngữ khác), chỉ số `[0][0]` thường ở góc trên-trái. Do đó, cần có một bước chuyển đổi tọa độ:
`map_array[m - 1 - y][x]` tương ứng với tọa độ `(x, y)`.

---

## 📌 Test Case Mẫu
[🧪 Link đến các Test Case mẫu](https://github.com/ToiLaKiet/Find-The-Princess/tree/master/test)

## 🕹️ Tính Năng Mở Rộng
- **Sinh ngẫu nhiên bản đồ**: Bạn có thể tạo một bản đồ mới với kích thước tùy ý và các chướng ngại vật được phân bố ngẫu nhiên.

## ⚠️ Hạn chế
- Tuy tính năng sinh ngẫu nhiên tốt nhưng hiện tại khi các component render liên tục sẽ dẫn tới lỗi, phải reload lại trang.

## 📂 Cấu Trúc Thư Mục

Cấu trúc dự án được tổ chức để dễ dàng quản lý và biên dịch.

```
.
├── src/
│   ├── app.py            # File chứa giao diện Streamlit app
│   └── utils.py          # File chứa logic thuật toán BFS
├── assets/
│   └── logo-uit.png      # Logo, favicon
├── test/                 # Thư mục chứa các file test case
│   ├── Test Case 1
        ├── input.txt
│   └── Test Case 2  
        ├── input.txt 
├── .gitignore
├── readme.md             # File hướng dẫn sử dụng    
├── requirements.txt      # File chứa các thư viện cần thiết
```

---

## ⚙️ Hướng Dẫn Cài Đặt và Chạy

Để chạy chương trình trên máy của bạn, hãy làm theo các bước sau.

### Yêu cầu
- Cài đặt Python 3.x (phiên bản 3.9+ được khuyến khích).

### Các bước thực hiện

#### 1. Tải mã nguồn về máy
Đầu tiên, sao chép (clone) repository này về máy tính của bạn và di chuyển vào thư mục dự án.
```bash
git clone https://github.com/ToiLaKiet/Find-The-Princess.git
cd Find-The-Princess
```

#### 2. Tạo và kích hoạt môi trường ảo
Sử dụng môi trường ảo là một thói quen tốt để quản lý các thư viện của dự án một cách độc lập, tránh xung đột với các dự án khác.

**Cách A: Sử dụng `venv` (Công cụ tích hợp sẵn của Python, khuyến khích)**
```bash
# Tạo một môi trường ảo có tên là "venv"
python3 -m venv venv

# Kích hoạt môi trường vừa tạo
# Trên macOS hoặc Linux:
source venv/bin/activate

# Trên Windows (Command Prompt/PowerShell):
venv\Scripts\activate
```

**Cách B: Sử dụng `Conda` (Nếu bạn đã cài đặt Anaconda hoặc Miniconda)**
```bash
# Tạo một môi trường mới tên là "princess_app" với phiên bản Python 3.9
conda create --name princess_app python=3.9 -y

# Kích hoạt môi trường
conda activate princess_app
```
Sau khi kích hoạt, bạn sẽ thấy tên môi trường (`(venv)` hoặc `(princess_app)`) xuất hiện ở đầu dòng lệnh.

#### 3. Cài đặt các thư viện cần thiết
Khi môi trường ảo đã được kích hoạt, hãy chạy lệnh sau để cài đặt tất cả các thư viện được yêu cầu từ file `requirements.txt`.
```bash
pip install -r requirements.txt
```

#### 4. Khởi chạy ứng dụng Streamlit
Bây giờ, bạn đã sẵn sàng để chạy ứng dụng!
```bash
streamlit run src/app.py
```
Sau khi thực thi lệnh này, một tab mới trên trình duyệt của bạn sẽ tự động mở ra trang web của ứng dụng, thường có địa chỉ là **http://localhost:8501**.

#### 5. Dừng ứng dụng
Để dừng ứng dụng, quay lại cửa sổ terminal đang chạy và nhấn tổ hợp phím `Ctrl + C`.

---

## 🛠️ Công Nghệ Sử Dụng

- **Ngôn ngữ:** Python
- **Giao diện:** Streamlit

---

## 📬 Thông Tin Liên Hệ

- 📧 **Email:** `[toilakiet.dev@gmail.com]`
- 🐛 **Báo lỗi:** Mọi góp ý hoặc báo lỗi, vui lòng mở một issue mới tại [GitHub Issues](https://github.com/ToiLaKiet/Find-The-Princess/issues) của repository.
