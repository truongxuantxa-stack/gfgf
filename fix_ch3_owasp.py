import re

file_path = "do_an_tot_nghiep.tex"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Cookie description
old_cookie = "Đối với xác thực, Backend sử dụng cơ chế Access Token và Refresh Token. Khi người dùng đăng nhập thành công, hệ thống tạo Access Token để Frontend gửi kèm trong header Authorization khi gọi các API cần xác thực. Refresh Token có thời gian sống dài hơn và được lưu trong HttpOnly Cookie. Việc đặt Refresh Token trong HttpOnly Cookie giúp hạn chế việc JavaScript phía Frontend truy cập trực tiếp vào token này. Ngoài ra, cookie refresh token được cấu hình đường dẫn riêng cho endpoint làm mới token, nhờ đó giảm phạm vi gửi cookie trong các request không cần thiết."
new_cookie = "Đối với xác thực, Backend sử dụng cơ chế Access Token và Refresh Token. Khi người dùng đăng nhập thành công, hệ thống tạo Access Token để Frontend gửi kèm trong header Authorization khi gọi các API cần xác thực. Refresh Token có thời gian sống 7 ngày và được lưu trong cookie với các thuộc tính \\texttt{HttpOnly}, \\texttt{SameSite=Strict}, \\texttt{Secure} khi hệ thống chạy trong môi trường production và \\texttt{Path} giới hạn ở endpoint làm mới token. Thuộc tính \\texttt{HttpOnly} hạn chế JavaScript phía Frontend đọc trực tiếp cookie, trong khi \\texttt{Secure} yêu cầu cookie chỉ được truyền qua HTTPS ở môi trường production. \\texttt{SameSite=Strict} hạn chế việc gửi cookie trong các request khác nguồn, còn phạm vi \\texttt{Path} hẹp giúp giảm số request không cần thiết mang theo Refresh Token. Cách cấu hình này phù hợp với một số khuyến nghị quản lý phiên của OWASP \\cite{owaspSessionManagement}. Tuy nhiên, \\texttt{Path} chỉ giới hạn phạm vi trình duyệt gửi cookie, không được xem là một ranh giới bảo mật tuyệt đối."
text = text.replace(old_cookie, new_cookie)

# 2. Update Password Hashing and Error/Rate Limit
old_pass_err_rate = """Mật khẩu người dùng không được lưu trực tiếp dưới dạng văn bản gốc. Khi đăng ký, Backend sử dụng bcrypt để băm mật khẩu trước khi lưu vào cơ sở dữ liệu. Khi đăng nhập, mật khẩu người dùng nhập vào được so sánh với giá trị đã băm. Nếu email không tồn tại hoặc mật khẩu không khớp, hệ thống trả về thông báo chung như “Email hoặc mật khẩu không đúng” thay vì nêu rõ sai email hay sai mật khẩu. Cách xử lý này giúp giảm khả năng suy đoán tài khoản hợp lệ từ phản hồi của hệ thống.

Bên cạnh xác thực, hệ thống áp dụng giới hạn request cho các route đăng nhập và đăng ký. Trong mã nguồn, nhóm route này được giới hạn 20 request trong 15 phút cho mỗi IP. Nếu vượt quá số lần cho phép, server trả về lỗi yêu cầu thử lại sau."""

new_pass_err_rate = """Mật khẩu người dùng không được lưu trực tiếp dưới dạng văn bản gốc. Khi đăng ký, Backend sử dụng thư viện \\texttt{bcryptjs} để thực hiện thuật toán bcrypt với cost factor 12 trước khi lưu giá trị băm vào cơ sở dữ liệu. Khi đăng nhập, mật khẩu đầu vào được kiểm tra bằng hàm \\texttt{bcrypt.compare}. OWASP khuyến nghị sử dụng các hàm băm mật khẩu chậm và thích ứng, trong đó Argon2id được ưu tiên cho hệ thống mới; đối với bcrypt, tài liệu nêu work factor tối thiểu là 10 \\cite{owaspPasswordStorage}. Vì vậy, cost factor 12 của NutriTrack cao hơn mức tối thiểu được OWASP nêu cho bcrypt, nhưng không nên được mô tả là lựa chọn hiện đại được OWASP ưu tiên nhất.

Nếu email không tồn tại hoặc mật khẩu không khớp, luồng đăng nhập đều trả về thông báo chung ‘Email hoặc mật khẩu không đúng’ thay vì phân biệt nguyên nhân thất bại. Phản hồi chung giúp giảm khả năng suy đoán sự tồn tại của tài khoản từ nội dung trả về và phù hợp với khuyến nghị về phản hồi xác thực của OWASP \\cite{owaspAuthentication}.

Bên cạnh xác thực, hệ thống áp dụng giới hạn request cho các route đăng nhập và đăng ký. Các route đăng nhập và đăng ký được giới hạn tối đa 20 request trong khoảng 15 phút theo địa chỉ IP. Đây là một hình thức throttling nhằm hạn chế số lượng request tự động trong thời gian ngắn \\cite{owaspAuthentication}. Tuy nhiên, cơ chế hiện tại chỉ đếm theo IP và chưa gắn bộ đếm với từng tài khoản, do đó được xem là một lớp phòng vệ bổ sung chứ không phải biện pháp ngăn chặn hoàn toàn brute-force hoặc credential stuffing."""
text = text.replace(old_pass_err_rate, new_pass_err_rate)

# 3. Add localStorage limit before table
old_before_table = "Một số cơ chế bảo mật và xử lý lỗi trong Backend được tổng hợp trong Bảng \\ref{tab:bao_mat_xu_ly_loi}."
new_before_table = "Ở phía Frontend, Access Token có thời hạn 15 phút được lưu trong \\texttt{localStorage} và được Axios interceptor đọc để gắn vào header \\texttt{Authorization}. Cách lưu trữ này thuận tiện cho việc duy trì trạng thái đăng nhập và tự động gửi lại request sau khi làm mới token, nhưng \\texttt{localStorage} luôn có thể được JavaScript cùng origin truy cập. OWASP cảnh báo rằng dữ liệu nhạy cảm hoặc định danh phiên trong \\texttt{localStorage} có thể bị lấy cắp khi ứng dụng xuất hiện lỗ hổng XSS \\cite{owaspHTML5Security}. Vì vậy, việc bảo vệ Refresh Token bằng HttpOnly Cookie không loại bỏ hoàn toàn rủi ro đối với Access Token đang được lưu tại phía client.\n\nMột số cơ chế bảo mật và xử lý lỗi trong Backend được tổng hợp trong Bảng \\ref{tab:bao_mat_xu_ly_loi}."
text = text.replace(old_before_table, new_before_table)

# 4. Update Summary paragraph
old_summary = "Nhìn chung, các cơ chế bảo mật và xử lý lỗi trong NutriTrack được triển khai ở mức phù hợp với một hệ thống quản lý dinh dưỡng cá nhân, giúp bảo vệ phiên đăng nhập, hạn chế request bất thường và duy trì cấu trúc phản hồi API nhất quán."
new_summary = "Nhìn chung, NutriTrack đã triển khai một số biện pháp bảo mật như phân tách Access Token và Refresh Token, bảo vệ Refresh Token bằng cookie, băm mật khẩu, sử dụng phản hồi đăng nhập chung, giới hạn request và chuẩn hóa xử lý lỗi. Một số cơ chế này tham chiếu và phù hợp với các khuyến nghị liên quan của OWASP. Tuy nhiên, hệ thống chưa được đánh giá theo toàn bộ tiêu chí của OWASP và vẫn còn các giới hạn như Access Token được lưu trong \\texttt{localStorage} và login throttling chỉ được thực hiện theo địa chỉ IP. Do đó, báo cáo chỉ đánh giá việc áp dụng từng biện pháp trong phạm vi mã nguồn hiện tại, không khẳng định hệ thống tuân thủ hoàn toàn OWASP."
text = text.replace(old_summary, new_summary)

# 5. Update Table 3.11 rows
text = text.replace("Refresh Token & Làm mới phiên đăng nhập & Lưu trong HttpOnly Cookie \\\\", "Refresh Token & Làm mới phiên đăng nhập & HttpOnly Cookie, SameSite=Strict, Secure ở production \\\\")
text = text.replace("bcrypt & Bảo vệ mật khẩu người dùng & Băm mật khẩu trước khi lưu \\\\", "bcrypt & Bảo vệ mật khẩu người dùng & Băm bằng bcryptjs với cost factor 12 \\\\")
text = text.replace("Rate limit & Hạn chế request bất thường & Giới hạn login/register theo IP \\\\", "Rate limit & Hạn chế request bất thường & 20 request/15 phút/IP cho login và register \\\\")

# 6. Add bibliography items
bib_items = """\\bibitem{owaspAuthentication}
OWASP Foundation,
``Authentication Cheat Sheet'',
\\textit{\\url{https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html}},
truy cập ngày 15/07/2026.

\\bibitem{owaspSessionManagement}
OWASP Foundation,
``Session Management Cheat Sheet'',
\\textit{\\url{https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html}},
truy cập ngày 15/07/2026.

\\bibitem{owaspPasswordStorage}
OWASP Foundation,
``Password Storage Cheat Sheet'',
\\textit{\\url{https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html}},
truy cập ngày 15/07/2026.

\\bibitem{owaspHTML5Security}
OWASP Foundation,
``HTML5 Security Cheat Sheet'',
\\textit{\\url{https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html}},
truy cập ngày 15/07/2026.

\\end{thebibliography}"""
text = text.replace("\\end{thebibliography}", bib_items)

# Update abbreviations list for OWASP
abbreviation = "OWASP & Open Worldwide Application Security Project \\\\"
if abbreviation not in text and "OWASP" not in text[:2000]: # just a heuristic, I will find the abbreviation list more properly
    # Try finding the right place to insert OWASP in alphabetical order. 
    # Abbreviations table usually has ORM, PAL, REST, etc.
    if "ORM & Object-Relational Mapping \\\\" in text:
        text = text.replace("ORM & Object-Relational Mapping \\\\", "ORM & Object-Relational Mapping \\\\\nOWASP & Open Worldwide Application Security Project \\\\")
    else:
        print("Could not find ORM abbreviation to insert OWASP")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Done basic replacements.")
