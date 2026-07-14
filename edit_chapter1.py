import re

with open('do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Hàm trợ giúp replace block
def replace_between(start_str, end_str, new_content, text):
    start_idx = text.find(start_str)
    if start_idx == -1:
        print(f'Cannot find start_str: {start_str[:50]}...')
        return text
    end_idx = text.find(end_str, start_idx)
    if end_idx == -1:
        print(f'Cannot find end_str: {end_str[:50]}...')
        return text
    
    return text[:start_idx] + start_str + new_content + text[end_idx:]

# 1.1 Đặc điểm của bài toán
s1 = r'\subsection{Đặc điểm của bài toán}'
e1 = r'\begin{figure}[htbp]'
c1 = r'''Bài toán quản lý dinh dưỡng cá nhân đòi hỏi tiếp nhận dữ liệu từ nhiều nguồn như hồ sơ sức khỏe, nhật ký ăn uống, và luyện tập. Các dữ liệu này có sự liên kết chặt chẽ và là đầu vào cho quá trình phân tích tình trạng cơ thể. Bên cạnh đó, nhiều chỉ số dinh dưỡng không được nhập trực tiếp mà do hệ thống tự động tính toán (BMI, BMR, TDEE).

Việc đánh giá chất lượng chế độ ăn cũng cần dựa trên cấu trúc thành phần dinh dưỡng thay vì chỉ sử dụng một giá trị năng lượng duy nhất. Đồng thời, hệ thống cần có cơ chế linh hoạt để nhập liệu thực phẩm mới (mã vạch, nhận dạng hình ảnh) khi dữ liệu nội bộ không đầy đủ.

Hình \ref{fig:tong_quan_bai_toan} mô tả tổng quan luồng dữ liệu của hệ thống từ lúc tiếp nhận đầu vào, qua các service xử lý nghiệp vụ tại Backend, đến khi xuất ra kết quả phân tích.

'''
content = replace_between(s1, e1, c1, content)

# 1.2.1 Mục tiêu xây dựng
s2 = r'\subsection{Mục tiêu xây dựng hệ thống}'
e2 = r'\subsection{Yêu cầu chức năng}'
c2 = r'''
Mục tiêu tổng quát của hệ thống là xây dựng một ứng dụng web hỗ trợ người dùng quản lý dinh dưỡng cá nhân thông qua việc ghi nhận dữ liệu, tính toán chỉ số, phân tích kết quả và trình bày thông tin dưới dạng trực quan.

Hệ thống quản lý các nhóm dữ liệu cốt lõi bao gồm hồ sơ sức khỏe cá nhân, nhật ký ăn uống, lượng nước uống, cân nặng và hoạt động luyện tập hằng ngày. Dựa trên dữ liệu này, hệ thống triển khai các nhóm chức năng tính toán, phân tích và hỗ trợ nhập liệu linh hoạt. Kết quả xử lý cuối cùng được tổng hợp và hiển thị trực quan thông qua Dashboard và xuất dưới dạng báo cáo PDF để người dùng dễ dàng theo dõi mục tiêu.

'''
content = replace_between(s2, e2, c2, content)

# 1.2.2 Yêu cầu chức năng
s3 = r'\subsection{Yêu cầu chức năng}'
e3 = r'\begin{table}[htbp]'
c3 = r'''
Dựa trên mục tiêu xây dựng hệ thống, các yêu cầu chức năng được xác định theo từng nhóm nghiệp vụ chính. Các chức năng này bao trùm từ khâu quản lý tài khoản, lưu trữ dữ liệu hằng ngày đến phân tích dinh dưỡng chuyên sâu, được tóm tắt chi tiết trong Bảng \ref{tab:tong_hop_chuc_nang}.

'''
content = replace_between(s3, e3, c3, content)

# 1.2.3 Yêu cầu phi chức năng
s4 = r'\subsection{Yêu cầu phi chức năng}'
e4 = r'\begin{table}[htbp]'
c4 = r'''
Bên cạnh các yêu cầu chức năng, hệ thống cần đáp ứng một số yêu cầu phi chức năng nhằm bảo đảm khả năng sử dụng, bảo mật, tính nhất quán dữ liệu, tính ổn định và khả năng mở rộng. Các yêu cầu này được tổng hợp chi tiết trong Bảng \ref{tab:tong_hop_phi_chuc_nang}.

'''
content = replace_between(s4, e4, c4, content)

s4_2 = r'\end{table}'
e4_2 = r'\section{Công nghệ và nền tảng phát triển}'
c4_2 = r'''

Các yêu cầu kỹ thuật và nghiệp vụ này định hình việc thiết kế kiến trúc tổng thể, cơ sở dữ liệu và các luồng xử lý chính trong hệ thống.

'''
# Phải cẩn thận, end{table} có nhiều. Chỉ thay giữa bảng phi chức năng và section Công nghệ
idx_phi = content.find(r'\caption{Tổng hợp yêu cầu phi chức năng của hệ thống}')
idx_endtable_phi = content.find(r'\end{table}', idx_phi)
idx_section_congnghe = content.find(r'\section{Công nghệ và nền tảng phát triển}', idx_endtable_phi)
if idx_phi != -1 and idx_endtable_phi != -1 and idx_section_congnghe != -1:
    content = content[:idx_endtable_phi+11] + c4_2 + content[idx_section_congnghe:]

# 1.3 Công nghệ - Rút gọn đoạn dẫn và bỏ Hình 1.3
# Đoạn dẫn
s5 = r'\section{Công nghệ và nền tảng phát triển}'
e5 = r'\begin{figure}[htbp]'
c5 = r'''Để đáp ứng yêu cầu xây dựng một hệ thống quản lý dinh dưỡng có khả năng xử lý dữ liệu theo thời gian, triển khai nhiều thuật toán và hỗ trợ mở rộng chức năng, đề tài lựa chọn kiến trúc Client–Server, trong đó giao diện người dùng, xử lý nghiệp vụ và cơ sở dữ liệu được tách biệt thành các thành phần độc lập. Các thành phần giao tiếp với nhau thông qua RESTful API.

Hệ thống được xây dựng hoàn toàn trên nền tảng JavaScript ở cả phía máy khách và máy chủ, giúp giảm sự khác biệt giữa Frontend và Backend. Mô hình liên kết các công nghệ trong hệ thống được thể hiện trong Hình \ref{fig:cac_cong_nghe}.

'''
# Cần check e5 là figure data_access_architecture
idx_tech = content.find(s5)
idx_fig_arch = content.find(r'\begin{figure}[htbp]', idx_tech) # Đây là fig:cac_cong_nghe
# À, trong văn bản cũ: 
# \section{Công nghệ...} (dòng 640)
# ... Hình \ref{fig:cac_cong_nghe}.
# Hình \ref{fig:data_access_architecture} mô tả... (dòng 644)
# \begin{figure}[htbp] ... \label{fig:cac_cong_nghe} ... (dòng 646)
# Thực ra Hình 1.3 là data_access_architecture, nằm SAU đoạn text. Khoan, hãy xem lại đoạn 646. Hình 1.3 là data_access_architecture hay fig:cac_cong_nghe?
# Dòng 696: \caption{Mô hình liên kết các công nghệ trong hệ thống} \label{fig:cac_cong_nghe}
# Dòng 721: \begin{figure}[htbp] ... \label{fig:data_access_architecture}
# Do đó, fig:cac_cong_nghe là Hình 1.2, data_access_architecture là Hình 1.3.

# Ta cần cắt bỏ đoạn text: "Hình \ref{fig:data_access_architecture} mô tả kiến trúc truy cập..." (Dòng 644)
import re
content = re.sub(r'Hình \\ref\{fig:data_access_architecture\} mô tả kiến trúc truy cập dữ liệu của hệ thống.*?\n', '', content, flags=re.DOTALL)

# Xóa nguyên cái figure fig:data_access_architecture
idx_fig2_start = content.find(r'\begin{figure}[htbp]', content.find(r'\subsection{MySQL và Sequelize ORM}'))
idx_fig2_end = content.find(r'\end{figure}', idx_fig2_start)
if idx_fig2_start != -1 and idx_fig2_end != -1:
    content = content[:idx_fig2_start] + content[idx_fig2_end+12:]


# 1.3.1 React
s_react = r'\subsection{React}'
e_react = r'\subsection{Node.js và Express}'
c_react = r'''
Giao diện người dùng được phát triển bằng thư viện React theo mô hình Single Page Application (SPA) thông qua Vite. Hệ thống sử dụng React Router để điều hướng và quản lý quyền truy cập qua Protected Route. Dữ liệu từ Backend được quản lý trạng thái bằng TanStack Query (React Query), kết hợp với Axios để thực hiện các yêu cầu HTTP. Các trang chức năng được tối ưu tải trang thông qua cơ chế lazy loading (React.lazy và Suspense).

'''
content = replace_between(s_react, e_react, c_react, content)

# 1.3.2 Node.js
s_node = r'\subsection{Node.js và Express}'
e_node = r'\subsection{MySQL và Sequelize ORM}'
c_node = r'''
Backend của hệ thống được xây dựng trên môi trường thực thi Node.js kết hợp framework Express. Ứng dụng tổ chức các giao tiếp thông qua RESTful API với tiền tố định tuyến \texttt{/api/v1}. Mã nguồn được phân tách kiến trúc rõ ràng thành route, middleware, controller, service và model. Cách thiết kế này giúp tách biệt vai trò xử lý yêu cầu và logic nghiệp vụ, thuận tiện cho mở rộng chức năng.

'''
content = replace_between(s_node, e_node, c_node, content)

# 1.3.3 MySQL
s_sql = r'\subsection{MySQL và Sequelize ORM}'
e_sql = r'\subsection{Các thư viện và dịch vụ hỗ trợ}'
c_sql = r'''
Hệ thống sử dụng MySQL làm hệ quản trị cơ sở dữ liệu quan hệ, được truy cập thông qua Sequelize ORM. Sequelize đảm nhiệm vai trò ánh xạ cấu trúc bảng (Model), quản lý các quan hệ (Association), thực hiện truy vấn CRUD và thực thi các kịch bản khởi tạo (Migration, Seeder), giúp tách rời mã SQL trực tiếp khỏi ứng dụng.

'''
content = replace_between(s_sql, e_sql, c_sql, content)

# 1.3.4 Các thư viện
s_lib = r'\subsection{Các thư viện và dịch vụ hỗ trợ}'
e_lib = r'\begin{longtable}'
c_lib = r'''
Ngoài các công nghệ cốt lõi, hệ thống tích hợp JSON Web Token (JWT) cho xác thực bảo mật thông qua Access Token và Refresh Token. Hệ thống tích hợp Open Food Facts API để tra cứu mã vạch và Gemini AI Vision để trích xuất bảng dinh dưỡng từ hình ảnh. Bên cạnh đó, PDFKit được dùng xuất báo cáo và tác vụ nền theo lịch được cấu hình phục vụ thuật toán Adaptive TDEE. Danh sách tổng hợp các công nghệ được trình bày trong Bảng \ref{tab:cong_nghe_su_dung}.

'''
content = replace_between(s_lib, e_lib, c_lib, content)

# 1.3.5 Đánh giá công nghệ
s_eval = r'\subsection{Đánh giá việc lựa chọn công nghệ}'
e_eval = r'\section{Kiến trúc tổng thể của hệ thống}'
c_eval = r'''
Bộ công nghệ được chọn hoàn toàn phù hợp với kiến trúc Client-Server, tạo ra môi trường phát triển đồng nhất bằng ngôn ngữ JavaScript. Giải pháp phân tách các lớp (Frontend, Backend, Database) cùng sự kết hợp của các dịch vụ bên ngoài (Open Food Facts, Gemini AI) đảm bảo tính ổn định, dễ bảo trì và có khả năng tích hợp trí tuệ nhân tạo hiệu quả vào nghiệp vụ cốt lõi.

'''
content = replace_between(s_eval, e_eval, c_eval, content)

# 1.4 Kiến trúc tổng thể
s_arch = r'\section{Kiến trúc tổng thể của hệ thống}'
e_arch = r'\begin{figure}[htbp]'
c_arch = r'''
Hệ thống NutriTrack được xây dựng theo kiến trúc Client-Server, trong đó giao diện React (Frontend), xử lý nghiệp vụ Node.js (Backend) và cơ sở dữ liệu MySQL hoạt động độc lập. Các thành phần giao tiếp qua giao thức HTTP dưới định dạng JSON bằng RESTful API.

Hình \ref{fig:kientruc_tongthe} mô tả luồng truy xuất dữ liệu: Người dùng thao tác tại Frontend, gửi yêu cầu qua Axios. Backend tiếp nhận, xử lý theo luồng Router -> Middleware -> Controller -> Service. Tại tầng Service, hệ thống truy xuất dữ liệu từ MySQL qua Sequelize ORM hoặc gọi dịch vụ ngoài rồi trả kết quả về cho Frontend.

'''
# e_arch match \begin{figure}[htbp] - fig:kientruc_tongthe
content = replace_between(s_arch, e_arch, c_arch, content)

# 1.4.1 Client-Server
s_cs = r'\subsection{Mô hình kiến trúc Client - Server}'
e_cs = r'\subsection{Kiến trúc Frontend}'
c_cs = r'''
Việc phân chia thành phần Client và Server phân định rõ ràng trách nhiệm hiển thị và xử lý logic nghiệp vụ. Client nhận dữ liệu định dạng JSON để cập nhật giao diện không cần tải lại trang. Trong khi đó, Server đảm bảo tính bảo mật và toàn vẹn dữ liệu thông qua cơ chế kiểm tra và điều phối tập trung.

'''
content = replace_between(s_cs, e_cs, c_cs, content)

# 1.4.2 Frontend
s_fe = r'\subsection{Kiến trúc Frontend}'
e_fe = r'\begin{figure}[htbp]'
c_fe = r'''
Frontend được tổ chức theo kiến trúc React SPA dạng component. Hệ thống điều hướng bằng React Router và bảo vệ quyền truy cập bằng Auth Context. Việc quản lý trạng thái dữ liệu (cache, đồng bộ) được thực hiện tối ưu qua TanStack Query, giảm thiểu gánh nặng gọi API lặp lại. Quá trình trao đổi dữ liệu với Backend do Axios đảm nhiệm (Chi tiết xem Hình \ref{fig:kientruc_frontend}).

'''
content = replace_between(s_fe, e_fe, c_fe, content)

# 1.4.3 Backend
s_be = r'\subsection{Kiến trúc Backend}'
e_be = r'\begin{figure}[htbp]'
c_be = r'''
Backend tổ chức theo mô hình MVC kết hợp tầng Service tập trung nghiệp vụ (Hình \ref{fig:kientruc_backend}). Controller chỉ nhận nhiệm vụ nhận và trả dữ liệu, mọi xử lý cốt lõi (tính toán dinh dưỡng, thuật toán, quét mã vạch) được trừu tượng hóa vào Service. Cách thiết kế này nâng cao tính độc lập của logic hệ thống, giúp dễ dàng mở rộng và bảo trì.

'''
content = replace_between(s_be, e_be, c_be, content)

# 1.4.4 Database
s_db = r'\subsection{Kiến trúc cơ sở dữ liệu}'
e_db = r'\begin{figure}[htbp]'
c_db = r'''
Cơ sở dữ liệu MySQL được thiết kế quan hệ, tổ chức xoay quanh thông tin người dùng, lịch sử dinh dưỡng, cân nặng và luyện tập (Hình \ref{fig:kientruc_csdl}). Việc ứng dụng Sequelize ORM giúp đảm bảo tính tương thích và bảo toàn dữ liệu bằng các ánh xạ Model, quản lý quan hệ khóa ngoại thay cho câu lệnh truy vấn SQL nguyên thủy. Chi tiết thiết kế dữ liệu được đề cập tại Chương 2.

'''
content = replace_between(s_db, e_db, c_db, content)

# 1.4.5 Đánh giá kiến trúc
s_eva2 = r'\subsection{Đánh giá kiến trúc hệ thống}'
e_eva2 = r'\section{Kết luận chương}'
c_eva2 = r'''
Kiến trúc đa tầng được ứng dụng cung cấp độ gắn kết lỏng lẻo giữa Frontend và Backend, hỗ trợ tích hợp linh hoạt các luồng nghiệp vụ phức tạp. Các thành phần có tính độc lập cao, vừa phục vụ tính năng phân tích dữ liệu hiệu quả, vừa đảm bảo khả năng triển khai hệ thống an toàn và mở rộng trong tương lai.

'''
content = replace_between(s_eva2, e_eva2, c_eva2, content)

# 1.5 Kết luận chương
s_con = r'\section{Kết luận chương}'
e_con = r'\chapter{PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG}'
c_con = r'''
Chương 1 đã trình bày tổng quan về bài toán và yêu cầu xây dựng ứng dụng NutriTrack, bao gồm các mục tiêu quản lý dữ liệu đa nguồn và phân tích chỉ số dinh dưỡng tự động. Việc ứng dụng linh hoạt các nền tảng React, Node.js, Express, kết hợp cùng cơ sở dữ liệu MySQL và các dịch vụ bổ trợ đã được định hình rõ qua mô hình Client-Server nhiều tầng. Kiến trúc và công nghệ này cung cấp tiền đề kỹ thuật vững chắc để hệ thống bước vào giai đoạn thiết kế chi tiết các chức năng và cơ sở dữ liệu ở Chương 2.

'''
content = replace_between(s_con, e_con, c_con, content)

with open('do_an_tot_nghiep.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hoàn tất thay thế!")
