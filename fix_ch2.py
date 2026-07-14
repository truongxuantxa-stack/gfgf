import re

with open('do_an_tot_nghiep.tex', 'r', encoding='utf8') as f:
    text = f.read()

# 1. Bảng 2.6
text = text.replace(r'\texttt{User}, \texttt{UserProfile}', r'\texttt{User}')
text = text.replace(r'\texttt{UserMealConfig}, \texttt{MealTemplate}, \texttt{MealRecommendation}', r'\texttt{UserMealConfig}, \texttt{MealTemplate}')

# 2. Scanner
old_scanner_2 = r'Bảng \texttt{ScannedProduct} lưu thông tin sản phẩm được tra cứu hoặc nhận dạng, cùng trạng thái và độ tin cậy của dữ liệu. Bảng \texttt{ProductContribution} lưu các lượt đóng góp liên quan đến sản phẩm và người dùng, phục vụ quá trình tổng hợp và đánh giá độ nhất quán.'
new_scanner = r'Các bảng \texttt{ScannedProduct} và \texttt{ProductContribution} lưu thông tin sản phẩm được tra cứu hoặc nhận dạng, trạng thái dữ liệu và các lượt đóng góp của người dùng. Dữ liệu này được sử dụng để tổng hợp độ tin cậy, xác minh sản phẩm và liên kết với bảng \texttt{Food} khi đáp ứng điều kiện nhập vào danh mục thực phẩm.'
text = text.replace(old_scanner_2, new_scanner)

old_scanner_1 = r'Các bảng \texttt{ScannedProduct} và \texttt{ProductContribution} hỗ trợ lưu trữ tạm thời các dữ liệu trả về từ Open Food Facts hoặc AI Vision. Dữ liệu này giúp người dùng sử dụng ngay trong phiên làm việc hoặc đóng góp chờ xác thực mà không làm loãng cơ sở dữ liệu \texttt{Food} gốc.'
text = text.replace(old_scanner_1, new_scanner)

# 3. Endpoint
text = text.replace(r'\texttt{/api/v1/users/me}', r'\texttt{/api/v1/auth/me}')
text = text.replace(r'\texttt{/api/v1/diary}', r'\texttt{/api/v1/diary/entries}')
text = text.replace(r'\texttt{/api/v1/tdee/adaptive}', r'\texttt{/api/v1/adaptive-tdee/calculate}')
text = re.sub(r'GET(\s*&\s*\\texttt\{/api/v1/adaptive-tdee/calculate\})', r'POST\1', text)
text = text.replace(r'\texttt{/api/v1/scanner/analyze}', r'\texttt{/api/v1/scanner/ai-vision}')

# 4. JWT Access Token
text = text.replace(r'Lưu Access Token\\vào bộ nhớ tạm', r'Lưu Access Token\\vào localStorage')

# 5. Sơ đồ điều hướng
old_nav = r'Người dùng sau khi đăng nhập nhưng chưa có hồ sơ sẽ đã đăng nhập nhưng chưa hoàn thành hồ sơ được chuyển hướng tới trang Onboarding thông qua \texttt{AuthOnlyRoute}. Các trang chức năng chính như Dashboard, Nhật ký ăn uống, Meal Planner, Cân nặng và Luyện tập được bảo vệ bởi \texttt{ProtectedRoute}.'
new_nav = r'Trang Onboarding được đặt trong AuthOnlyRoute, do đó chỉ yêu cầu người dùng đã đăng nhập. Các trang nghiệp vụ được bảo vệ bởi ProtectedRoute; người dùng chưa đăng nhập được chuyển tới trang đăng nhập, còn người dùng đã đăng nhập nhưng chưa hoàn thành onboarding được chuyển tới trang Onboarding.'
text = text.replace(old_nav, new_nav)
# Nếu dòng gốc chưa bị lỗi:
old_nav_2 = r'Người dùng sau khi đăng nhập nhưng chưa có hồ sơ sẽ bị ép buộc truy cập Onboarding thông qua \texttt{AuthOnlyRoute}. Các trang chức năng chính như Dashboard, Nhật ký ăn uống, Meal Planner, Cân nặng và Luyện tập được bảo vệ bởi \texttt{ProtectedRoute}.'
text = text.replace(old_nav_2, new_nav)

# Fix lại câu "Các trang Landing Page, đăng nhập, đăng ký là công khai." nếu cần, nhưng text.replace là đủ.
text = text.replace('Luồng điều hướng được tổ chức dựa trên trạng thái xác thực.', 'Luồng điều hướng được tổ chức theo trạng thái xác thực và trạng thái hoàn thành onboarding.')

# 6. Báo cáo / Thống kê
text = re.sub(r'\\node\[page\]\s*\(report\)\s*at\s*\([^)]+\)\s*\{Báo cáo / Thống kê\};\n?', '', text)
text = re.sub(r'\\draw\[arrow\]\s*\(forkApp\)\s*\|-\s*\(report\.west\);\n?', '', text)

# 7. ERD
old_erd = r'Bất kỳ tương tác phát sinh dữ liệu nào cũng phải thông qua khóa ngoại \texttt{userId}.'
new_erd = r'Các bảng lưu dữ liệu cá nhân như \texttt{DiaryEntry}, \texttt{WeightLog}, \texttt{WaterLog}, \texttt{ExerciseLog} và \texttt{AdaptiveTDEELog} được liên kết với \texttt{User} thông qua khóa ngoại \texttt{userId}.'
text = text.replace(old_erd, new_erd)

# 8. Lỗi lặp chữ & giọng văn
text = text.replace('sẽ được được xây dựng', 'sẽ được xây dựng')
text = text.replace('được xây dựng theo yêu cầu đã xác định theo các định hướng đã được xác định', 'được xây dựng theo các định hướng đã được xác định')
text = text.replace('Đây là làm cơ sở cho việc triển khai, kết nối chặt chẽ với ORM, làm tiền đề để xây dựng các API xử lý nghiệp vụ ở phần kế tiếp.', 'Mô hình này làm cơ sở cho việc triển khai, kết nối chặt chẽ với ORM và hỗ trợ xây dựng các API xử lý nghiệp vụ ở phần kế tiếp.')
text = text.replace('phục vụ ứng dụng React SPA cho Web SPA', 'phục vụ ứng dụng React SPA')
text = text.replace('tạo tiền đề vững chắc', 'tạo cơ sở vững chắc')
text = text.replace('Đây là nhóm chức năng có tần suất sử dụng cao nhất.', 'Đây là nhóm chức năng đóng vai trò cốt lõi trong thao tác hằng ngày.')

# 9. Tối ưu truy vấn dữ liệu
old_index = r'Do yêu cầu truy xuất dữ liệu hằng ngày theo khoảng thời gian rất lớn, các trường như \texttt{date} trong bảng log hay nhật ký đều cần được thiết lập chỉ mục phụ (secondary index). Việc này đảm bảo tốc độ phản hồi nhanh khi tính toán lượng calories hoặc chất đa lượng.'
new_index = r'Các bảng \texttt{DiaryEntry}, \texttt{WeightLog}, \texttt{WaterLog} và \texttt{ExerciseLog} sử dụng chỉ mục kết hợp giữa \texttt{userId} và \texttt{date}. Các chỉ mục này hỗ trợ truy vấn dữ liệu theo người dùng và khoảng thời gian, phục vụ quá trình tổng hợp Dashboard và báo cáo.'
text = text.replace(old_index, new_index)

with open('do_an_tot_nghiep.tex', 'w', encoding='utf8') as f:
    f.write(text)
print("Done fixing")
