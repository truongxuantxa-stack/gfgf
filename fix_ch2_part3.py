with open('do_an_tot_nghiep.tex', 'r', encoding='utf8') as f:
    text = f.read()

# 1
text = text.replace(r'\subsection{Cơ chế xác thực và phân quyền}', r'\subsection{Cơ chế xác thực và kiểm soát truy cập}')

# 2
text = text.replace(r'Nhằm đảm bảo giao diện Frontend xử lý dữ liệu một cách đồng nhất, tất cả API đều trả về kết quả tuân theo cấu trúc tiêu chuẩn được định nghĩa tại Bảng \ref{tab:cau_truc_phan_hoi}.', 
                    r'Các API nghiệp vụ trả về dữ liệu JSON chủ yếu sử dụng cấu trúc phản hồi thống nhất được định nghĩa tại Bảng \ref{tab:cau_truc_phan_hoi}.')

# 3
text = text.replace(r'Theo dõi Cân nặng / Nước & Nhập thông số thực tế, hiển thị biểu đồ xu hướng \\',
                    r'Theo dõi cân nặng & Ghi nhận cân nặng và hiển thị biểu đồ xu hướng \\' + '\n' + r'\hline' + '\n' + r'Luyện tập & Ghi nhận hoạt động, thời lượng và năng lượng tiêu hao \\')

# 4
text = text.replace(r'Tính toàn vẹn dữ liệu được đảm bảo thông qua việc mọi dữ liệu phát sinh (như nhật ký, cân nặng) đều được liên kết chặt chẽ qua khóa ngoại \texttt{userId}.',
                    r'Các dữ liệu cá nhân phát sinh như nhật ký ăn uống, cân nặng, nước uống, luyện tập và lịch sử Adaptive TDEE được liên kết với người dùng thông qua khóa ngoại \texttt{userId}.')

# 5
text = text.replace(r'tạo cơ sở vững chắc', r'tạo cơ sở cho')

# 6
text = text.replace(r'lưu vết lịch sử chặt chẽ', r'lưu trữ lịch sử theo thời gian')

# 7
text = text.replace(r'thiết kế các thành phần thiết kế chính', r'thiết kế các thành phần chính')

# 8
text = text.replace(r'đảm bảo khả năng sử dụng trên nhiều kích thước màn hình', r'hỗ trợ hiển thị trên nhiều kích thước màn hình')

with open('do_an_tot_nghiep.tex', 'w', encoding='utf8') as f:
    f.write(text)

print("Done part 3!")
