# NGỮ CẢNH VÀ QUY TẮC LÀM VIỆC DỰ ÁN (PROJECT CONTEXT)

> **Mục đích của file này:** Lưu trữ toàn bộ ngữ cảnh, trạng thái, cấu trúc và quy tắc làm việc của dự án báo cáo Đồ án tốt nghiệp "Hệ thống quản lý dinh dưỡng cá nhân" (NutriTrack). Bất kỳ AI nào (kể cả Claude, GPT hay Gemini) khi bắt đầu phiên làm việc (session) mới đều PHẢI đọc file này đầu tiên để đồng bộ ngữ cảnh.

---

## 1. TỔNG QUAN DỰ ÁN (NUTRI-TRACK)
- **Tên đề tài:** Xây dựng hệ thống quản lý dinh dưỡng cá nhân.
- **Mục tiêu:** Ứng dụng giúp người dùng theo dõi hồ sơ sức khỏe, ghi nhật ký ăn uống (calo, macro), theo dõi vận động, lượng nước uống. Hệ thống tích hợp tính toán Adaptive TDEE, chấm điểm thực phẩm (Food Scoring), gợi ý thực đơn (Meal Planner) và có khả năng quét mã vạch / nhận diện nhãn dinh dưỡng (Scanner) bằng AI.

## 2. KIẾN TRÚC CÔNG NGHỆ (TECH STACK)
- **Frontend:** React, Axios (gọi API), TanStack Query (quản lý state/cache), React Router.
- **Backend:** Node.js, Express (RESTful API), tổ chức theo mô hình Layered Architecture (Router -> Middleware -> Controller -> Service).
- **Cơ sở dữ liệu:** MySQL.
- **ORM / Truy cập dữ liệu:** Sequelize (Model, Association, Query/CRUD, Migration/Seeder).
- **Dịch vụ & API bên ngoài:** 
  - *Xác thực:* JSON Web Token (JWT).
  - *Dữ liệu thực phẩm:* Open Food Facts API.
  - *AI OCR / Nhận diện:* Gemini AI Vision.

## 3. TRẠNG THÁI FILE BÁO CÁO (LATEX)
- **File làm việc chính:** `do_an_tot_nghiep.tex` (và phiên bản song song `do_an_tot_nghiep_fixed.tex`).
- **Tình trạng cấu trúc:** File nguyên khối (monolithic) cực lớn, dài khoảng 2.700 dòng (~314KB).
- **Chiến lược hiện tại (PHƯƠNG ÁN A):** Đồ án đang ở giai đoạn cuối sát deadline. **TUYỆT ĐỐI KHÔNG** chia tách file LaTeX này thành các file con (`\input{}`) để tránh rủi ro vỡ cấu trúc (spacing, pagebreak, cross-reference). Chấp nhận file lớn (hơi lag) nhưng đổi lại sự an toàn 100% cho file PDF output. Việc refactor/tách file chỉ được cân nhắc SAU KHI bảo vệ xong đồ án.

## 4. QUY TẮC LÀM VIỆC DÀNH CHO AI (CRITICAL RULES)
1. **Định vị khu vực (Targeted Edits):** Vì file LaTeX rất nặng, AI **không được** load và đọc lại toàn bộ file nếu không cần thiết. Người dùng sẽ cung cấp từ khóa, số dòng, hoặc mục cụ thể (VD: "Sửa phần 2.3", "dòng 885-1715"). AI phải dùng công cụ `grep_search` hoặc `view_file` để khoanh vùng và thao tác chính xác tại khu vực đó.
2. **Sửa đổi cục bộ (Surgical Changes):** Dùng `replace_file_content` hoặc `multi_replace_file_content` (thay vì ghi đè cả file) để giữ an toàn cho các phần không liên quan.
3. **Vẽ sơ đồ bằng TikZ / Chèn hình ảnh:**
   - **Tuyệt đối không dùng `\begin{figure}[H]`** để tránh tạo khoảng trắng lớn ở cuối trang. Luôn dùng `\begin{figure}[htbp]` để thả nổi hình (floating).
   - **Tham chiếu chéo BẮT BUỘC:** Mọi hình ảnh đều phải được gọi tên trong văn bản (VD: "Chi tiết được minh họa trong Hình \ref{tên_label}."), **bất kể hình nằm ở vị trí nào** (ngay sát chữ hay trôi sang trang sau). Đây là tiêu chuẩn học thuật bắt buộc để vn bản độc lập với hình.
   - Đảm bảo thiết kế gọn gàng, chia tầng (layer) rõ ràng bằng các khung `fit` hoặc `rectangle`.
   - Các chữ/nhãn trên mũi tên phải được tinh chỉnh `xshift`, `yshift`, `pos` để không đè lên các đối tượng khác.
   - Chương 1 chỉ vẽ khái quát (lược bỏ các chi tiết kỹ thuật quá sâu nếu không cần thiết).
4. **Xử lý Bảng biểu (Tables):**
   - Tránh dùng `[H]` cho môi trường `table` tương tự như `figure`.
   - Khi dùng `longtable` cho các bảng dài, nếu bảng bị đẩy sang trang sau và để lại khoảng trắng lớn ở cuối trang trước: **Tuyệt đối không đổi thành `table` float** (vì bảng dài sẽ bị văng mất khỏi luồng văn bản). Cách xử lý đúng là **giữ nguyên `longtable`** nhưng dời toàn bộ khối code của bảng xuống bên dưới đoạn/tiểu mục tiếp theo trong source code. Điều này giúp chữ tự động trôi lên lấp đầy khoảng trắng, còn bảng sẽ xuất hiện ở trang sau một cách tự nhiên. Bắt buộc dùng `\ref{}` để tham chiếu thay vì dùng từ "bảng sau".
5. **Ngôn ngữ:** Luôn giao tiếp, giải thích, và comment code bằng tiếng Việt.
6. **Đồng bộ Git:** Luôn kết thúc một task quan trọng bằng việc tạo commit rõ ràng và push lên repository.
7. **Kiểm chứng file thực tế (Read before execute):** Tuyệt đối không dựa vào trí nhớ tạm thời đối với các file mã nguồn hoặc file kế hoạch (Plan/Task), đặc biệt là sau khi phiên làm việc bị ngắt quãng hoặc bộ nhớ bị cắt bớt (truncate / checkpoint). Luôn phải dùng lệnh `view_file` để đọc trực tiếp nội dung mới nhất của file trên ổ cứng trước khi đưa ra nhận xét hoặc code, nhằm tránh tình trạng bịa đặt (hallucinate) và bỏ sót các cập nhật mới nhất từ người dùng hoặc AI khác.

## 5. LỊCH SỬ CẬP NHẬT GẦN NHẤT
- Đã quyết định **KHÔNG CHIA TÁCH** file LaTeX (`do_an_tot_nghiep.tex`) để đảm bảo an toàn tuyệt đối trước thềm bảo vệ.
- Đã fix triệt để lỗi biên dịch LaTeX (crash do ngoặc nhọn `{` nằm ngay sau ký tự xuống dòng `\\` bên trong TikZ node).
- Đã hoàn thiện **Hình 1.5**: Sơ đồ Kiến trúc tổng thể Client - Server. 
  - Giao diện trải ngang trực quan: `Router → Middleware → Controller → Service → Sequelize ORM`.
  - Tách RESTful API làm cầu nối, thêm luồng JWT Authentication một chiều vào Middleware, và các dịch vụ ngoài (Open Food Facts, Gemini AI) giao tiếp nét đứt 2 chiều với tầng Service.
- Đã chèn quy tắc xử lý lỗi khoảng trắng khổng lồ do `longtable` gây ra bằng cách dời vị trí code để text chảy lên lấp khoảng trống.
- Đã bổ sung quy tắc số 7 (Kiểm chứng file thực tế) để chống tình trạng hallucinate do truncate bộ nhớ, bắt buộc AI dùng lệnh `view_file` đọc lại nội dung trước khi code.

---
*(Cập nhật lần cuối: Tháng 7/2026 - Cập nhật quy tắc kiểm chứng file thực tế)*
