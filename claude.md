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
8. **Quy trình biên dịch LaTeX (Compilation Protocol):**
   - **Luôn compile đủ 3 lần liên tiếp** sau bất kỳ thay đổi nào ảnh hưởng đến cấu trúc tài liệu (chapter, section, toc, lof, lot, aux). Lý do: lần 1 tạo file `.toc`/`.aux`, lần 2 nhúng vào PDF, lần 3 ổn định toàn bộ tham chiếu chéo.
   - **Khi pdflatex bị ngắt giữa chừng (kill/crash):** File `.toc` có thể đã bị xóa trắng. Dấu hiệu nhận biết là log xuất hiện dòng `No file do_an_tot_nghiep.toc.`. Bắt buộc phải chạy lại **ít nhất 2 lần** để phục hồi.
   - **Cấm dùng lệnh nội bộ của package bên trong `\addtocontents`:** Ví dụ: `\addtocontents{toc}{\cftpagenumbersoff{chapter}}` là **NGUY HIỂM** — nó nhúng lệnh phụ thuộc package trực tiếp vào file `.toc`, gây lỗi parser trên mọi phần mềm. Thay thế an toàn: dùng `\addtocontents{toc}{\protect\contentsline{chapter}{Tên mục}{}{}}` với tham số số trang để trống.
   - **Bắt buộc xác minh kết quả sau compile:** Sau khi biên dịch xong, luôn chạy lệnh sau để kiểm tra trực tiếp nội dung PDF trước khi báo cho người dùng:
     ```powershell
     pdftotext do_an_tot_nghiep.pdf - | Select-String "MỤC LỤC" -Context 0,3
     ```

## 5. QUY ĐỊNH TRÍCH DẪN VÀ TÀI LIỆU THAM KHẢO (Theo Mẫu ĐATN-14 ĐHXDHN)
**1. Quy tắc viết trích dẫn trong nội dung bài (In-text Citation):**
- **Hình thức:** Bắt buộc sử dụng chữ số đặt trong ngoặc vuông (ví dụ: `[1]`, `[2]`, `[3]`). Số này tương ứng với số thứ tự của tài liệu được liệt kê trong danh mục Tài liệu tham khảo ở cuối quyển.
- **Vị trí:** Trích dẫn phải được đặt ngay sau nội dung tham chiếu và trước dấu chấm câu. Ví dụ: *"Hệ thống sử dụng thuật toán Adaptive TDEE để tự động tính toán năng lượng tiêu hao dựa trên biến động cân nặng thực tế [4]."*
- **Trích dẫn nhiều tài liệu:** Dùng dấu phẩy cho các tài liệu rời rạc: `[1, 3]`. Dùng dấu gạch nối cho một chuỗi tài liệu liên tục: `[1-4]`.

**2. Quy tắc sắp xếp Danh mục Tài liệu tham khảo:**
- **Theo ngôn ngữ:** Tài liệu tiếng Việt xếp trước, sau đó đến tài liệu tiếng nước ngoài (Anh, Pháp, v.v.). Không được trộn lẫn các ngôn ngữ.
- **Theo thứ tự chữ cái:** Trong mỗi nhóm ngôn ngữ, sắp xếp theo thứ tự ABC của tác giả.
  - Tác giả Việt Nam: Xếp theo Tên.
  - Tác giả nước ngoài: Xếp theo Họ.
  - Không có tác giả cá nhân: Xếp theo chữ cái đầu tiên của tên cơ quan ban hành (ví dụ: "Bộ Giáo dục và Đào tạo" xếp theo chữ "B").

**3. Quy định về định dạng ghi thông tin từng loại tài liệu:**
- **Đối với Sách:** `[Số thứ tự] Tên tác giả (năm xuất bản), Tên sách (in nghiêng), Nhà xuất bản, Nơi xuất bản.`
- **Đối với Bài báo khoa học/Hội nghị:** `[Số thứ tự] Tên tác giả (năm công bố), "Tên bài báo (đặt trong ngoặc kép)", Tên tạp chí/kỷ yếu hội nghị (in nghiêng), Tập, Số, Số trang.`
- **Đối với Tài liệu từ Internet:** `[Số thứ tự] Tên tác giả hoặc Tên cơ quan tổ chức, "Tên bài viết/tài liệu trên web", Đường dẫn URL chi tiết (in nghiêng), ngày truy cập.`
*(Ví dụ: Viện Dinh dưỡng Quốc gia, "Bảng nhu cầu dinh dưỡng khuyến nghị cho người Việt Nam", http://viendinhduong.vn/abc-xyz, truy cập ngày 15/05/2026).*

> ⚠️ **Lưu ý quan trọng về Liêm chính học thuật:** Mọi ý tưởng, số liệu, hình ảnh, hay thuật toán không phải do bạn tự tạo ra đều bắt buộc phải có trích dẫn nguồn rõ ràng để tránh vi phạm đạo văn khi trường quét bằng phần mềm trước bảo vệ M3.

## 6. QUY ĐỊNH VỀ PHONG CÁCH VÀ GIỌNG VĂN THUYẾT MINH (Theo HUCE)
**1. Tính khách quan và Giọng văn khoa học (Academic Tone):**
- **Không dùng ngôi thứ nhất:** Thuyết minh đồ án là văn bản nghiên cứu kỹ thuật/khoa học. Tuyệt đối không sử dụng các từ xưng hô mang tính cá nhân như "Tôi nghĩ rằng...", "Em nhận thấy...", "Chúng ta nên..." trong các chương nội dung chính.
- **Sử dụng câu bị động hoặc ẩn ngôi:** Viết theo lối khách quan. Thay vì viết "Tôi đã xây dựng mô hình...", phải viết: "Mô hình hệ thống đã được xây dựng...", hoặc "Qua quá trình nghiên cứu, giải pháp được đề xuất là...".
- **Ngoại lệ duy nhất:** Chỉ được phép xưng "Em" hoặc "Tôi" ở Lời nói đầu (Lời cảm ơn) và Lời cam đoan.

**2. Sự rõ ràng, mạch lạc và chuẩn xác về mặt thuật ngữ:**
- **Ngôn từ định lượng:** Lối viết phải chính xác, có căn cứ số liệu rõ ràng. Tránh các tính từ cảm tính, mơ hồ như "rất nhanh", "khá mạnh", "công nghệ rất hiện đại". Phải dùng số liệu chứng minh (Ví dụ: "Tốc độ phản hồi đạt dưới 200ms", "Hàm lượng dinh dưỡng đáp ứng 85% tiêu chuẩn").
- **Thống nhất thuật ngữ chuyên ngành:** Các thuật ngữ kỹ thuật (mã nguồn, cơ sở dữ liệu, vi chất, năng lượng...) phải viết đúng danh pháp khoa học và thống nhất xuyên suốt. Viết tắt bắt buộc phải xuất hiện trong danh mục viết tắt ở phần đầu.

**3. Tính nghiêm túc và Liêm chính học thuật (Plagiarism-free):**
- **Giọng văn cam đoan quyết liệt:** Tại Mẫu ĐATN-14, phải dùng giọng văn khẳng định 100% về tính độc lập: "Đồ án này là công trình nghiên cứu của riêng tôi, các số liệu... là trung thực và chưa từng được công bố".
- **Tuyệt đối khách quan (Lạnh lùng, lý tính):** Tập trung hoàn toàn vào số liệu và sự thật kỹ thuật, không đưa cảm xúc cá nhân. Nếu copy nội dung do AI sinh ra, **bắt buộc phải sửa lại** những câu có giọng điệu quá bay bổng, quảng cáo (kiểu "Giải pháp tuyệt vời này sẽ mang lại...") thành giọng văn báo cáo kỹ thuật trung lập. Mọi ý tưởng "mượn" đều phải trích dẫn (như đã quy định ở Mục 5).

## 7. LỊCH SỬ CẬP NHẬT GẦN NHẤT
- Đã quyết định **KHÔNG CHIA TÁCH** file LaTeX (`do_an_tot_nghiep.tex`) để đảm bảo an toàn tuyệt đối trước thềm bảo vệ.
- Đã fix triệt để lỗi biên dịch LaTeX (crash do ngoặc nhọn `{` nằm ngay sau ký tự xuống dòng `\\` bên trong TikZ node).
- Đã hoàn thiện **Hình 1.5**: Sơ đồ Kiến trúc tổng thể Client - Server. 
- Đã chèn quy tắc xử lý lỗi khoảng trắng khổng lồ do `longtable` gây ra bằng cách dời vị trí code để text chảy lên lấp khoảng trống.
- Đã bổ sung quy tắc số 7 (Kiểm chứng file thực tế) để chống tình trạng hallucinate.
- Đã bổ sung Quy định trích dẫn tài liệu tham khảo theo Mẫu ĐATN-14 của trường ĐHXDHN.
- Bổ sung quy định chặt chẽ về phong cách và giọng văn học thuật theo tiêu chuẩn HUCE (tính khách quan, ngôn từ định lượng, liêm chính).
- Bổ sung **Quy tắc số 8 (Quy trình biên dịch LaTeX)**: compile đủ 3 lần, xử lý khi pdflatex bị ngắt giữa chừng, cấm dùng lệnh nội bộ package trong `\addtocontents`, và bắt buộc xác minh kết quả bằng `pdftotext` sau khi compile.

---
*(Cập nhật lần cuối: Tháng 7/2026 - Thêm quy tắc biên dịch LaTeX 3-pass và xác minh PDF bằng pdftotext)*
