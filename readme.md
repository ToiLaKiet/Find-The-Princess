# 🤴 Tìm Đường Cứu Công Chúa (Kén Rể)

- **Họ và Tên:** `Võ Anh Kiệt`
- **MSSV:** `23520825`
- **Lớp:** `CS112.P22`

[🔗 Link đến Repository GitHub](https://github.com/ToiLaKiet/Find-The-Princess)  
[🧪 Link đến các Test Case mẫu](https://github.com/your-username/your-repo-name/tree/main/test)

---

## 📚 Mục Lục

- [🎯 Mục Tiêu Bài Toán](#-mục-tiêu-bài-toán)
- [💡 Ý Tưởng và Giải Pháp](#-ý-tưởng-và-giải-pháp)
- [📌 Ví Dụ Input](#-ví-dụ-input)
- [✅ Ví Dụ Output Tương Ứng](#-ví-dụ-output-tương-ứng)
- [📂 Cấu Trúc Thư Mục](#-cấu-trúc-thư-mục)
- [⚙️ Hướng Dẫn Biên Dịch và Chạy Chương Trình](#️-hướng-dẫn-biên-dịch-và-chạy-chương-trình)
- [🛠️ Công Nghệ Sử Dụng](#️-công-nghệ-sử-dụng)
- [📬 Liên Hệ](#-liên-hệ)

---

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
    *   Sử dụng một mảng 2D `visited` để đánh dấu các ô đã đi qua, tránh đi lại và tạo vòng lặp vô tận.
    *   Sử dụng một mảng 2D `distance` để lưu khoảng cách (số canh giờ) từ điểm xuất phát đến ô hiện tại.

2.  **Quá trình duyệt:**

3.  **Kết quả:**
    *   Nếu vòng lặp kết thúc mà chưa tìm thấy đích, có nghĩa là không tồn tại đường đi. Trả về `-1`.

### Chú ý về hệ tọa độ:
Đề bài quy định tọa độ `(x, y)` với `(0, 0)` ở góc dưới-trái. Khi làm việc với mảng 2D trong C++ (hoặc các ngôn ngữ khác), chỉ số `[0][0]` thường ở góc trên-trái. Do đó, cần có một bước chuyển đổi tọa độ:
`map_array[m - 1 - y][x]` tương ứng với tọa độ `(x, y)`.

---

## 📌 Test case mẫu 

```
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
```
*   Bản đồ `5 x 6`.
*   Hiệp sĩ bắt đầu tại `(0, 0)`.
*   Công chúa ở tại `(5, 4)`.

---

## ✅ Ví Dụ Output Tương Ứng

```
5
```
**Giải thích:** Đường đi ngắn nhất từ `(0,0)` đến `(5,4)` tốn 5 bước (canh giờ). Một đường đi khả thi là: `(0,0) -> (1,1) -> (2,2) -> (3,3) -> (4,3) -> (5,4)`.

---

## 📂 Cấu Trúc Thư Mục

Cấu trúc dự án được tổ chức để dễ dàng quản lý và biên dịch.

```
.
├── src/
│   ├── main.cpp         # File chứa hàm main, xử lý input/output
│   └── bfs.cpp          # File chứa logic thuật toán BFS (tùy chọn)
├── include/
│   └── bfs.h            # Header file cho thuật toán (tùy chọn)
├── test/                # Thư mục chứa các file test case
│   ├── input1.txt
│   └── output1.txt
├── .gitignore
└── Makefile             # File hướng dẫn biên dịch tự động
```

---

## ⚙️ Hướng Dẫn Biên Dịch và Chạy Chương Trình

Để chạy chương trình trên máy của bạn, hãy làm theo các bước sau.

### Yêu cầu
- Trình biên dịch C++ (ví dụ: `g++`).
- Công cụ `make` (khuyến khích).

### Các bước
1.  **Clone repository về máy:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Biên dịch chương trình:**
    Sử dụng `Makefile` đã cung cấp để biên dịch.
    ```bash
    make
    ```
    Lệnh này sẽ tạo ra một file thực thi trong thư mục `bin/` (ví dụ: `bin/main`).

3.  **Chạy chương trình:**
    Cung cấp dữ liệu đầu vào cho chương trình. Bạn có thể dùng redirection từ file:
    ```bash
    ./bin/main < test/input1.txt
    ```

4.  **Dọn dẹp (tùy chọn):**
    Để xóa các file object và file thực thi đã được tạo ra:
    ```bash
    make clean
    ```

---

## 🛠️ Công Nghệ Sử Dụng

- **Ngôn ngữ:** C++ (Sử dụng `g++` để biên dịch)
- **Công cụ Build:** Make

---

## 📬 Liên Hệ

- 📧 **Email:** `[toilakiet.dev@gmail.com]`
- 🐛 **Báo lỗi:** Mở một issue mới tại [GitHub Issues](https://github.com/ToiLaKiet/Find-The-Princess/issues) của repository.
