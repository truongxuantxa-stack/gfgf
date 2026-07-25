import re

with open('do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hình 1.5 (Kiến trúc Backend) từ [p] -> [htbp]
content = re.sub(r'\\begin\{figure\}\[p\](\s*\\centering\s*\\resizebox\{0\.8\\textwidth\}\{!\}\{\s*\\begin\{tikzpicture\}\[\s*node distance=0\.7cm and 1\.5cm)', r'\\begin{figure}[htbp]\1', content)

# 2. Hình 1.6 (Cơ sở dữ liệu) từ [p] -> [htbp]
content = re.sub(r'\\begin\{figure\}\[p\](\s*\\centering\s*\\resizebox\{0\.8\\textwidth\}\{!\}\{\s*\\begin\{tikzpicture\}\[\s*node distance=0\.8cm and 1\.5cm)', r'\\begin{figure}[htbp]\1', content)

# 3. Dời Hình 1.6 về sau "Kiến trúc cơ sở dữ liệu"
# Cẩn thận: pattern chỉ bắt Hình 1.6 (có label fig:kientruc_csdl)
fig16_pattern = r'(\\begin\{figure\}\[htbp\].*?\\caption\{Kiến trúc tổng quan cơ sở dữ liệu\}.*?\\label\{fig:kientruc_csdl\}\n\\end\{figure\}\n)'
match = re.search(fig16_pattern, content, re.DOTALL)
if match:
    fig_text = match.group(1)
    content = content.replace(fig_text, '')
    target = 'Chi tiết thiết kế dữ liệu được đề cập tại Chương 2.\n'
    content = content.replace(target, target + '\n' + fig_text + '\n')

# 4. Thêm 3 đoạn văn
para_frontend = """
Việc phân tách rõ ràng tầng hiển thị (Frontend) và tầng xử lý nghiệp vụ (Backend) mang lại nhiều ưu điểm vượt trội. Về phía Frontend, mô hình Single Page Application (SPA) xây dựng trên nền tảng React kết hợp Vite không chỉ mang lại trải nghiệm người dùng mượt mà, giảm thiểu thời gian tải lại trang, mà còn tối ưu hóa luồng dữ liệu thông qua công cụ quản lý trạng thái TanStack Query. Các truy vấn API, bộ nhớ đệm (cache) và đồng bộ dữ liệu thời gian thực được xử lý tự động, giúp giảm tải đáng kể cho máy chủ và nâng cao tốc độ phản hồi của giao diện.

Về phía Backend, kiến trúc MVC kết hợp chặt chẽ với tầng Service độc lập là điểm cốt lõi giúp hệ thống quản lý trơn tru các luồng nghiệp vụ phức tạp. Thay vì tập trung mã lệnh tại Controller, toàn bộ logic tính toán chuyên sâu như Thuật toán thích ứng TDEE (Adaptive TDEE), cơ sở dữ liệu dinh dưỡng (Nutrition Core) hay xử lý nhận diện ảnh qua Gemini AI Vision đều được đóng gói gọn gàng trong các Service Modules. Nhờ đó, mã nguồn trở nên tinh gọn, dễ bảo trì và thuận tiện trong việc tích hợp thêm các dịch vụ ngoại vi sau này mà không phá vỡ cấu trúc hiện tại.
"""
para_conclusion = """
Đặc biệt, hệ thống đã giải quyết thành công các thách thức về luồng dữ liệu và bảo mật trong một ứng dụng quản lý sức khỏe. Cơ chế xác thực an toàn thông qua JSON Web Token (JWT) kết hợp Refresh Token lưu trữ qua HttpOnly Cookie đảm bảo an toàn tối đa cho phiên đăng nhập của người dùng. Sự kết hợp giữa cơ sở dữ liệu nội bộ MySQL lưu trữ thông tin cá nhân bảo mật và các nguồn dữ liệu mở rộng như Open Food Facts API giúp phong phú hóa kho dữ liệu thực phẩm mà không làm quá tải hệ thống lưu trữ cốt lõi.

Nhìn chung, những phân tích ban đầu về yêu cầu chức năng và phi chức năng đã định hình rõ ràng các ràng buộc kỹ thuật. Sự lựa chọn công nghệ phù hợp không chỉ giải quyết trọn vẹn bài toán ghi chép nhật ký ăn uống truyền thống mà còn mở ra không gian tích hợp AI, tự động hóa quy trình phân tích dinh dưỡng. Với bộ khung kiến trúc phân lớp toàn diện này, nhóm phát triển đã có đầy đủ cơ sở lý luận và nền tảng công nghệ để tự tin chuyển sang bước quan trọng tiếp theo: mô hình hóa chi tiết cấu trúc dữ liệu vật lý, thiết kế danh mục API hoàn chỉnh và xây dựng nguyên mẫu giao diện người dùng (UI/UX) ở Chương 2.
"""

# Chèn para_frontend trước \section{Kết luận chương}
target2 = r'(\n\\section\{Kết luận chương\}\n)'
content = re.sub(target2, '\n' + para_frontend.strip() + '\n\n' + r'\1', content)

# Chèn para_conclusion trước \chapter{PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG}
target3 = r'(\n\\chapter\{PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG\}\n)'
content = re.sub(target3, '\n' + para_conclusion.strip() + '\n\n' + r'\1', content)

# 5. Sửa Hình 2.6 (và 2 hình kia) - thay \makebox bằng \resizebox
content = content.replace(r'\makebox[\textwidth][c]{', r'\resizebox{0.95\textwidth}{!}{')

with open('do_an_tot_nghiep.tex', 'w', encoding='utf-8') as f:
    f.write(content)
