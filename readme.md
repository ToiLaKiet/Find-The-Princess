# 🤴 Hành Trình Kén Rể: Tìm Đường Tới Công Chúa 👸

*Một thử thách mô phỏng thuật toán BFS, nơi hiệp sĩ phải tìm ra con đường ngắn nhất để giải cứu công chúa và chứng tỏ mình xứng đáng.*

**Hiệp sĩ thực hiện:**
| Họ và Tên     | MSSV       | Lớp         |
|---------------|------------|-------------|
| **Võ Anh Kiệt** | `23520825` | `CS112.P22` |

---

## 🗺️ Bản Đồ Hành Trình

- [🎯 **Sứ Mệnh:** Mục Tiêu Thử Thách](#🎯-sứ-mệnh-mục-tiêu-thử-thách)
- [💡 **Chiến Lược:** Ý Tưởng & Giải Pháp](#💡-chiến-lược-ý-tưởng--giải-pháp)
- [📌 **Các Chướng Ngại Vật:** Test Case](#📌-các-chướng-ngại-vật-test-case)
- [🕹️ **Phép Thuật Mở Rộng:** Tính Năng Thêm](#🕹️-phép-thuật-mở-rộng-tính-năng-thêm)
- [⚠️ **Giới Hạn Sức Mạnh:** Hạn Chế](#⚠️-giới-hạn-sức-mạnh-hạn-chế)
- [📂 **Kho Báu:** Cấu Trúc Thư Mục](#📂-kho-báu-cấu-trúc-thư-mục)
- [⚙️ **Triệu Hồi:** Hướng Dẫn Cài Đặt & Chạy](#⚙️-triệu-hồi-hướng-dẫn-cài-đặt--chạy)
- [🛠️ **Vũ Khí:** Công Nghệ Sử Dụng](#🛠️-vũ-khí-công-nghệ-sử-dụng)
- [📬 **Gửi Thư Bồ Câu:** Liên Hệ](#📬-gửi-thư-bồ-câu-liên-hệ)

## 🎯 Sứ Mệnh: Mục Tiêu Thử Thách

Nhiệm vụ của hiệp sĩ là tìm **đường đi ngắn nhất** trên một bản đồ dạng lưới (`m x n`) để đến được hoàng cung cứu công chúa.

1.  **Bản đồ:** Một lưới hình chữ nhật kích thước `m x n`, với các ô đi được (`0`) và các ô là chướng ngại vật không đi được (`1`).
2.  **Di chuyển:** Hiệp sĩ có thể di chuyển từ một ô sang 8 ô lân cận (ngang, dọc, và chéo). Mỗi bước đi tốn **1 canh giờ**.
3.  **Hệ tọa độ:** Góc dưới cùng bên trái của bản đồ có tọa độ `(0, 0)`.
4.  **Mục tiêu:** Tính toán thời gian (số bước đi) tối thiểu để đi từ vị trí của hiệp sĩ đến hoàng cung. Nếu không có đường đi, trả về `-1`.

---

## 💡 Chiến Lược: Ý Tưởng & Giải Pháp

Để hoàn thành sứ mệnh, hiệp sĩ sẽ sử dụng một chiến lược cổ xưa và hiệu quả: Thuật toán **Tìm kiếm theo chiều rộng (Breadth-First Search - BFS)**. Đây là lựa chọn tối ưu cho việc tìm đường đi ngắn nhất trên một đồ thị mà mọi bước đi đều có giá trị như nhau.

### Nguyên lý hoạt động của BFS:
1.  **Khởi tạo:**
    *   Bắt đầu từ đỉnh xuất phát (vị trí của hiệp sĩ).
    *   Sử dụng một `hàng đợi (queue)` để lưu trữ các ô sẽ được duyệt.
    *   Sử dụng một mảng 2D `check` để đánh dấu các ô đã đi qua, tránh đi lại và tạo vòng lặp vô tận.
    *   Sử dụng một mảng 2D `mark` để lưu toạ độ của ô được đi liền trước (tức là ô "cha" của ô hiện tại), giúp truy vết lại đường đi.

2.  **Quá trình duyệt:**
    *   Lấy ô đầu tiên trong hàng đợi.
    *   Kiểm tra xem ô đó có phải là vị trí của công chúa không. Nếu phải, truy vết ngược từ mảng `mark` để tìm ra đường đi và kết thúc. Nếu không, tiếp tục.
    *   Duyệt qua tất cả các ô lân cận (8 hướng di chuyển) của ô hiện tại.
    *   Với mỗi ô lân cận:
        *   Kiểm tra xem nó có nằm trong bản đồ không.
        *   Kiểm tra xem nó có phải là chướng ngại vật (`1`) hay đã được đánh dấu (`check`) chưa.
        *   Nếu ô lân cận hợp lệ, đánh dấu nó (`check`), lưu lại dấu vết trong mảng `mark`, và thêm nó vào hàng đợi.
    *   Lặp lại quá trình này cho đến khi hàng đợi rỗng hoặc tìm thấy công chúa.

3.  **Kết quả:**
    *   Nếu vòng lặp kết thúc mà chưa tìm thấy đích, có nghĩa là không tồn tại đường đi. Trả về `-1`.
    *   Ngược lại, trả về mảng chứa các tọa độ của con đường chiến thắng từ vị trí của hiệp sĩ đến công chúa.

### Chú ý về hệ tọa độ:
Đề bài quy định tọa độ `(x, y)` với `(0, 0)` ở góc dưới-trái. Khi làm việc với mảng 2D trong C++, chỉ số `[0][0]` thường ở góc trên-trái. Do đó, cần có một phép biến đổi tọa độ:
`map_array[m - 1 - y][x]` tương ứng với tọa độ `(x, y)`.

---

## 📌 Các Chướng Ngại Vật: Test Case
Hiệp sĩ có thể luyện tập với các thử thách mẫu tại đây:
[🧪 Link đến các Test Case mẫu](https://github.com/ToiLaKiet/Find-The-Princess/tree/master/test)

## 🕹️ Phép Thuật Mở Rộng: Tính Năng Thêm
Ngoài nhiệm vụ chính, hiệp sĩ còn có thể sử dụng phép thuật để:
- **Sinh ngẫu nhiên bản đồ**: Tạo ra những thử thách mới với kích thước tùy ý và các chướng ngại vật được phân bố ngẫu nhiên.

## ⚠️ Giới Hạn Sức Mạnh: Hạn Chế
Mọi phép thuật đều có giới hạn. Hiện tại, khi các thành phần giao diện được render lại liên tục (ví dụ: sinh bản đồ mới quá nhanh), ứng dụng có thể gặp lỗi và cần phải tải lại trang.

## 📂 Kho Báu: Cấu Trúc Thư Mục

Bản đồ kho báu của dự án được sắp xếp như sau để dễ dàng quản lý và sử dụng:

```
.
├── src/
│   ├── app.py            # Nơi chứa giao diện và phép thuật Streamlit
│   └── utils.py          # Lõi thuật toán BFS, trái tim của hiệp sĩ
├── assets/
│   └── logo-uit.png      # Huy hiệu, cờ hiệu
├── test/                 # Khu vực luyện tập với các thử thách
│   ├── Test Case 1
        ├── input.txt
│   └── Test Case 2  
        ├── input.txt 
├── .gitignore
├── readme.md             # Cuộn giấy hướng dẫn này
├── requirments.txt       # Danh sách các thần chú cần thiết
```

---

## ⚙️ Triệu Hồi: Hướng Dẫn Cài Đặt & Chạy

Để bắt đầu hành trình trên máy của bạn, hãy làm theo các bước sau.

### Bí Kíp Yêu Cầu
- Cài đặt Python 3.x (phiên bản 3.9+ được khuyến khích).

### Các Bước Triệu Hồi

#### 1. Nhận Nhiệm Vụ từ Thánh Địa GitHub
Đầu tiên, sao chép (clone) kho báu này về máy và di chuyển vào vùng đất của dự án.
```bash
git clone https://github.com/ToiLaKiet/Find-The-Princess.git
cd Find-The-Princess
```

#### 2. Chuẩn Bị Vùng Đất Phép Thuật (Môi Trường Ảo)
Sử dụng môi trường ảo là một nghi thức quan trọng để giữ cho các phép thuật của dự án không xung đột với thế giới bên ngoài.

**Cách A: Sử dụng `venv` (Công cụ tích hợp của Python, khuyến khích)**
```bash
# Tạo một vùng đất phép thuật tên "venv"
python3 -m venv venv

# Kích hoạt vùng đất này
# Trên macOS hoặc Linux:
source venv/bin/activate

# Trên Windows (Command Prompt/PowerShell):
venv\Scripts\activate
```

**Cách B: Sử dụng `Conda` (Nếu bạn là một pháp sư Anaconda)**
```bash
# Tạo môi trường mới tên "princess_app"
conda create --name princess_app python=3.9 -y

# Kích hoạt môi trường
conda activate princess_app
```
Sau khi kích hoạt, bạn sẽ thấy tên môi trường (`(venv)` hoặc `(princess_app)`) xuất hiện ở đầu dòng lệnh.

#### 3. Trang Bị Thần Chú (Cài Đặt Thư Viện)
Khi đã ở trong vùng đất phép thuật, hãy đọc cuộn giấy `requirements.txt` để trang bị tất cả các thần chú cần thiết.
```bash
pip install -r requirements.txt
```

#### 4. Bắt Đầu Hành Trình!
Bây giờ, bạn đã sẵn sàng. Hãy triệu hồi ứng dụng!
```bash
streamlit run src/app.py
```
Một cánh cổng sẽ tự động mở ra trên trình duyệt của bạn (thường là **http://localhost:8501**), dẫn đến giao diện của thử thách.

#### 5. Tạm Nghỉ
Để kết thúc hành trình, quay lại cửa sổ terminal đang chạy và nhấn tổ hợp phím `Ctrl + C`.

---

## 🛠️ Vũ Khí: Công Nghệ Sử Dụng

- **Ngôn ngữ:** Python (Linh hồn của hiệp sĩ)
- **Giao diện:** Streamlit (Phép thuật hiển thị)

---

## 📬 Gửi Thư Bồ Câu: Liên Hệ

- 📧 **Email:** `[toilakiet.dev@gmail.com]`
- 🐛 **Báo cáo quái vật (bug):** Nếu phát hiện quái vật trên đường đi, xin hãy mở một "issue" mới tại [Thánh Địa GitHub](https://github.com/ToiLaKiet/Find-The-Princess/issues) của dự án.
