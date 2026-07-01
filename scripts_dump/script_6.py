
import re

file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\baocao_latex_raw.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = []

old_1_1 = '''\\textbf{Gợi ý chèn Bảng 1.1. Các yêu cầu chính của hệ thống}

\\textbf{Nhóm yêu cầu}

\\textbf{Nội dung}

Quản lý dữ liệu

Lưu trữ hồ sơ, nhật ký ăn uống, cân nặng và luyện tập

Tính toán

BMI, BMR, TDEE và mục tiêu dinh dưỡng

Phân tích

Đánh giá chất lượng thực phẩm và phân tích tình trạng dinh dưỡng

Hỗ trợ nhập liệu

Tra cứu mã vạch và nhận dạng bảng thành phần dinh dưỡng

Báo cáo

Dashboard và xuất báo cáo PDF'''

new_1_1 = '''\\begin{table}[htbp]
\\centering
\\caption{Các yêu cầu chính của hệ thống}
\\begin{tabular}{|p{4cm}|p{11cm}|}
\\hline
\\textbf{Nhóm yêu cầu} & \\textbf{Nội dung} \\\\
\\hline
Quản lý dữ liệu & Lưu trữ hồ sơ, nhật ký ăn uống, cân nặng và luyện tập \\\\
\\hline
Tính toán & BMI, BMR, TDEE và mục tiêu dinh dưỡng \\\\
\\hline
Phân tích & Đánh giá chất lượng thực phẩm và phân tích tình trạng dinh dưỡng \\\\
\\hline
Hỗ trợ nhập liệu & Tra cứu mã vạch và nhận dạng bảng thành phần dinh dưỡng \\\\
\\hline
Báo cáo & Dashboard và xuất báo cáo PDF \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_1_1, new_1_1))

old_1_2 = '''\\textbf{Gợi ý chèn Bảng 1.2. Danh sách công nghệ sử dụng trong hệ thống}

\\textbf{Công nghệ}

\\textbf{Vai trò trong hệ thống}

React

Xây dựng giao diện người dùng

React Router

Điều hướng và bảo vệ các trang

TanStack Query

Quản lý dữ liệu phía máy khách

Axios

Gửi yêu cầu HTTP

Node.js

Môi trường thực thi phía máy chủ

Express

Xây dựng RESTful API

Sequelize ORM

Tương tác với cơ sở dữ liệu

MySQL

Lưu trữ dữ liệu

JWT

Xác thực bằng Access Token và Refresh Token

Open Food Facts API

Tra cứu thông tin thực phẩm theo mã vạch

Gemini AI Vision

Nhận dạng bảng thành phần dinh dưỡng từ hình ảnh'''

new_1_2 = '''\\begin{table}[htbp]
\\centering
\\caption{Danh sách công nghệ sử dụng trong hệ thống}
\\begin{tabular}{|p{5cm}|p{10cm}|}
\\hline
\\textbf{Công nghệ} & \\textbf{Vai trò trong hệ thống} \\\\
\\hline
React & Xây dựng giao diện người dùng \\\\
\\hline
React Router & Điều hướng và bảo vệ các trang \\\\
\\hline
TanStack Query & Quản lý dữ liệu phía máy khách \\\\
\\hline
Axios & Gửi yêu cầu HTTP \\\\
\\hline
Node.js & Môi trường thực thi phía máy chủ \\\\
\\hline
Express & Xây dựng RESTful API \\\\
\\hline
Sequelize ORM & Tương tác với cơ sở dữ liệu \\\\
\\hline
MySQL & Lưu trữ dữ liệu \\\\
\\hline
JWT & Xác thực bằng Access Token và Refresh Token \\\\
\\hline
Open Food Facts API & Tra cứu thông tin thực phẩm theo mã vạch \\\\
\\hline
Gemini AI Vision & Nhận dạng bảng thành phần dinh dưỡng từ hình ảnh \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_1_2, new_1_2))

old_2_x = '''\\textbf{Bảng 2.x. Tóm tắt khóa chính và khóa ngoại của một số bảng chính}

\\begin{table}[H]
\\centering
\\textbf{Bảng}
\\begin{tabular}{|p{4cm}|p{5.5cm}|p{5.5cm}|}
\\hline
\\textbf{Khóa chính} & \\textbf{Khóa ngoại chính} & \\textbf{Vai trò} \\\\ \\hline
User & id & — \\\\ \\hline
Lưu tài khoản, hồ sơ sức khỏe và cấu hình cá nhân & Food & id \\\\ \\hline
userId, nếu là thực phẩm do người dùng tạo & Lưu dữ liệu thực phẩm & DiaryEntry \\\\ \\hline
id & userId, foodId & Lưu nhật ký ăn uống \\\\ \\hline
WeightLog & id & userId \\\\ \\hline
Lưu lịch sử cân nặng & WaterLog & id \\\\ \\hline
userId & Lưu dữ liệu nước uống theo ngày & ExerciseLog \\\\ \\hline
id & userId & Lưu hoạt động luyện tập \\\\ \\hline
MealTemplate & id & — \\\\ \\hline
Lưu mẫu bữa ăn & UserMealConfig & id \\\\ \\hline
userId & Lưu cấu hình phân bổ bữa ăn của người dùng & AdaptiveTDEELog \\\\ \\hline
id & userId & Lưu lịch sử tính toán TDEE thích ứng \\\\ \\hline
ScannedProduct & id & foodId, tùy chọn \\\\ \\hline
Lưu sản phẩm được quét & ProductContribution & id \\\\ \\hline
userId, scannedProductId & Lưu dữ liệu đóng góp cho sản phẩm quét & \\textbf{Gợi ý chèn Hình 2.x. Sơ đồ ERD rút gọn của hệ thống} \\\\ \\hline
\\end{tabular}
\\end{table}'''

new_2_x = '''\\begin{table}[htbp]
\\centering
\\caption{Tóm tắt khóa chính và khóa ngoại của một số bảng chính}
\\begin{tabular}{|p{4cm}|p{2cm}|p{3.5cm}|p{5.5cm}|}
\\hline
\\textbf{Bảng} & \\textbf{Khóa chính} & \\textbf{Khóa ngoại chính} & \\textbf{Vai trò} \\\\
\\hline
User & id & — & Lưu tài khoản, hồ sơ sức khỏe và cấu hình cá nhân \\\\
\\hline
Food & id & userId & Lưu dữ liệu thực phẩm \\\\
\\hline
DiaryEntry & id & userId, foodId & Lưu nhật ký ăn uống \\\\
\\hline
WeightLog & id & userId & Lưu lịch sử cân nặng \\\\
\\hline
WaterLog & id & userId & Lưu dữ liệu nước uống theo ngày \\\\
\\hline
ExerciseLog & id & userId & Lưu hoạt động luyện tập \\\\
\\hline
MealTemplate & id & — & Lưu mẫu bữa ăn \\\\
\\hline
UserMealConfig & id & userId & Lưu cấu hình phân bổ bữa ăn của người dùng \\\\
\\hline
AdaptiveTDEELog & id & userId & Lưu lịch sử tính toán TDEE thích ứng \\\\
\\hline
ScannedProduct & id & foodId (tùy chọn) & Lưu sản phẩm được quét \\\\
\\hline
ProductContribution & id & userId, scannedProductId & Lưu dữ liệu đóng góp cho sản phẩm quét \\\\
\\hline
\\end{tabular}
\\end{table}

\\textbf{Gợi ý chèn Hình 2.x. Sơ đồ ERD rút gọn của hệ thống}'''
replacements.append((old_2_x, new_2_x))

old_3_x_1 = '''Bảng 3.x trình bày các nhóm dữ liệu chính được sử dụng trong Food Scoring.

\\textbf{Nhóm dữ liệu}

\\textbf{Thành phần}

\\textbf{Vai trò}

Cơ sở chuẩn hóa

Năng lượng

Quy đổi các chất về mật độ trên 100 kcal

Thành phần cộng điểm chính

Protein, chất xơ

Phản ánh mật độ đạm và chất xơ

Thành phần trừ điểm

Đường, natri

Kiểm soát thành phần cần hạn chế

Vi chất

Vitamin A, vitamin C, canxi, sắt

Bổ sung đánh giá về mật độ vi chất

Dữ liệu phân loại

Loại thực phẩm, nhóm thực phẩm

Xử lý ngoại lệ theo đặc điểm thực phẩm'''

new_3_x_1 = '''\\begin{table}[htbp]
\\centering
\\caption{Các nhóm dữ liệu chính được sử dụng trong Food Scoring}
\\begin{tabular}{|p{4cm}|p{4cm}|p{7cm}|}
\\hline
\\textbf{Nhóm dữ liệu} & \\textbf{Thành phần} & \\textbf{Vai trò} \\\\
\\hline
Cơ sở chuẩn hóa & Năng lượng & Quy đổi các chất về mật độ trên 100 kcal \\\\
\\hline
Thành phần cộng điểm chính & Protein, chất xơ & Phản ánh mật độ đạm và chất xơ \\\\
\\hline
Thành phần trừ điểm & Đường, natri & Kiểm soát thành phần cần hạn chế \\\\
\\hline
Vi chất & Vitamin A, vitamin C, canxi, sắt & Bổ sung đánh giá về mật độ vi chất \\\\
\\hline
Dữ liệu phân loại & Loại thực phẩm, nhóm thực phẩm & Xử lý ngoại lệ theo đặc điểm thực phẩm \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_3_x_1, new_3_x_1))

old_3_x_2 = '''\\textbf{Thành phần}

\\textbf{Điều kiện đánh giá}

\\textbf{Tác động đến điểm}

Protein

Đạt mức tốt hoặc cao

+15 hoặc +25

Chất xơ

Đạt mức tốt hoặc cao

+15 hoặc +25

Đường

Vượt ngưỡng cảnh báo hoặc cao

-10 hoặc -25

Natri

Vượt ngưỡng cảnh báo hoặc cao

-10 hoặc -25

Vi chất

Đạt mức tốt hoặc cao

+5 hoặc +10'''

new_3_x_2 = '''\\begin{table}[htbp]
\\centering
\\caption{Quy tắc cộng trừ điểm cho các thành phần dinh dưỡng}
\\begin{tabular}{|p{3cm}|p{7cm}|p{5cm}|}
\\hline
\\textbf{Thành phần} & \\textbf{Điều kiện đánh giá} & \\textbf{Tác động đến điểm} \\\\
\\hline
Protein & Đạt mức tốt hoặc cao & +15 hoặc +25 \\\\
\\hline
Chất xơ & Đạt mức tốt hoặc cao & +15 hoặc +25 \\\\
\\hline
Đường & Vượt ngưỡng cảnh báo hoặc cao & -10 hoặc -25 \\\\
\\hline
Natri & Vượt ngưỡng cảnh báo hoặc cao & -10 hoặc -25 \\\\
\\hline
Vi chất & Đạt mức tốt hoặc cao & +5 hoặc +10 \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_3_x_2, new_3_x_2))

old_3_x_3 = '''Bảng 3.x trình bày các nhóm dữ liệu đầu vào chính của Health Insights.

\\textbf{Nhóm dữ liệu}

\\textbf{Nguồn dữ liệu}

\\textbf{Vai trò trong xử lý}

Năng lượng và macro

Nhật ký ăn uống

So sánh với targetCalories và mục tiêu macro

Chất xơ, đường, natri

Nhật ký ăn uống

Tạo cảnh báo hoặc gợi ý liên quan đến chất lượng khẩu phần

Nước uống

Water log trong ngày

So sánh với mục tiêu nước

Nhóm bữa ăn

Nhật ký ăn uống theo bữa

Xác định ngày đã đủ bữa hay chưa

Giờ phía client

Giao diện người dùng

Hỗ trợ tránh cảnh báo thiếu quá sớm

Giới tính

Hồ sơ người dùng

Chọn một số ngưỡng tham chiếu phù hợp'''

new_3_x_3 = '''\\begin{table}[htbp]
\\centering
\\caption{Các nhóm dữ liệu đầu vào chính của Health Insights}
\\begin{tabular}{|p{4cm}|p{4cm}|p{7cm}|}
\\hline
\\textbf{Nhóm dữ liệu} & \\textbf{Nguồn dữ liệu} & \\textbf{Vai trò trong xử lý} \\\\
\\hline
Năng lượng và macro & Nhật ký ăn uống & So sánh với targetCalories và mục tiêu macro \\\\
\\hline
Chất xơ, đường, natri & Nhật ký ăn uống & Tạo cảnh báo hoặc gợi ý liên quan đến chất lượng khẩu phần \\\\
\\hline
Nước uống & Water log trong ngày & So sánh với mục tiêu nước \\\\
\\hline
Nhóm bữa ăn & Nhật ký ăn uống theo bữa & Xác định ngày đã đủ bữa hay chưa \\\\
\\hline
Giờ phía client & Giao diện người dùng & Hỗ trợ tránh cảnh báo thiếu quá sớm \\\\
\\hline
Giới tính & Hồ sơ người dùng & Chọn một số ngưỡng tham chiếu phù hợp \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_3_x_3, new_3_x_3))

old_3_x_4 = '''Bảng 3.x tóm tắt cơ chế phân tầng trong Health Insights.

\\textbf{Tầng xử lý}

\\textbf{Điều kiện theo calo}

\\textbf{Cảnh báo thiếu hụt được ưu tiên}

Sinh tồn

Dưới 50\\% mục tiêu

Chỉ cảnh báo lượng ăn quá thấp

Đa lượng

Từ 50\\% đến dưới 70\\% mục tiêu

Thiếu calo, protein và chất béo

Vi lượng

Từ 70\\% mục tiêu trở lên

Chất xơ, canxi, sắt, vitamin C, vitamin A'''

new_3_x_4 = '''\\begin{table}[htbp]
\\centering
\\caption{Tóm tắt cơ chế phân tầng trong Health Insights}
\\begin{tabular}{|p{3cm}|p{6cm}|p{6cm}|}
\\hline
\\textbf{Tầng xử lý} & \\textbf{Điều kiện theo calo} & \\textbf{Cảnh báo thiếu hụt được ưu tiên} \\\\
\\hline
Sinh tồn & Dưới 50\\% mục tiêu & Chỉ cảnh báo lượng ăn quá thấp \\\\
\\hline
Đa lượng & Từ 50\\% đến dưới 70\\% mục tiêu & Thiếu calo, protein và chất béo \\\\
\\hline
Vi lượng & Từ 70\\% mục tiêu trở lên & Chất xơ, canxi, sắt, vitamin C, vitamin A \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_3_x_4, new_3_x_4))


old_3_x_5 = '''\\textbf{Nhóm insight}

\\textbf{Severity}

\\textbf{Vai trò hiển thị}

Cảnh báo nguy cơ

danger

Ưu tiên hiển thị trước

Cảnh báo cần chú ý

warning

Nhắc người dùng điều chỉnh

Nước uống

water

Theo dõi lượng nước trong ngày

Gợi ý cải thiện

suggestion

Đưa ra hướng điều chỉnh nhẹ'''

new_3_x_5 = '''\\begin{table}[htbp]
\\centering
\\caption{Phân loại các nhóm insight theo severity}
\\begin{tabular}{|p{4cm}|p{4cm}|p{7cm}|}
\\hline
\\textbf{Nhóm insight} & \\textbf{Severity} & \\textbf{Vai trò hiển thị} \\\\
\\hline
Cảnh báo nguy cơ & danger & Ưu tiên hiển thị trước \\\\
\\hline
Cảnh báo cần chú ý & warning & Nhắc người dùng điều chỉnh \\\\
\\hline
Nước uống & water & Theo dõi lượng nước trong ngày \\\\
\\hline
Gợi ý cải thiện & suggestion & Đưa ra hướng điều chỉnh nhẹ \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_3_x_5, new_3_x_5))


old_3_x_6 = '''Bảng 3.x trình bày các nhóm xử lý chính trong Meal Planner.

\\textbf{Nhóm xử lý}

\\textbf{Vai trò}

Meal Target Allocation

Chuyển mục tiêu dinh dưỡng trong ngày thành mục tiêu cho từng bữa

Template Matching

Chọn tổ hợp nguyên liệu theo các vai trò carbohydrate, protein, chất béo và rau

Weight Calculator

Tính khối lượng nguyên liệu để đạt mục tiêu macro của bữa ăn

Edge Case Handling

Kiểm tra nghiệm âm, khối lượng bất thường hoặc tổ hợp không khả thi

Smart Swap

Gợi ý thay thế nguyên liệu khi tổ hợp hiện tại không phù hợp'''

new_3_x_6 = '''\\begin{table}[htbp]
\\centering
\\caption{Các nhóm xử lý chính trong Meal Planner}
\\begin{tabular}{|p{5cm}|p{10cm}|}
\\hline
\\textbf{Nhóm xử lý} & \\textbf{Vai trò} \\\\
\\hline
Meal Target Allocation & Chuyển mục tiêu dinh dưỡng trong ngày thành mục tiêu cho từng bữa \\\\
\\hline
Template Matching & Chọn tổ hợp nguyên liệu theo các vai trò carbohydrate, protein, chất béo và rau \\\\
\\hline
Weight Calculator & Tính khối lượng nguyên liệu để đạt mục tiêu macro của bữa ăn \\\\
\\hline
Edge Case Handling & Kiểm tra nghiệm âm, khối lượng bất thường hoặc tổ hợp không khả thi \\\\
\\hline
Smart Swap & Gợi ý thay thế nguyên liệu khi tổ hợp hiện tại không phù hợp \\\\
\\hline
\\end{tabular}
\\end{table}'''
replacements.append((old_3_x_6, new_3_x_6))


not_found = []
for old_text, new_text in replacements:
    if old_text in content:
        content = content.replace(old_text, new_text)
    else:
        # handle line endings
        old_text_lf = old_text.replace('\\r\\n', '\\n')
        content_lf = content.replace('\\r\\n', '\\n')
        if old_text_lf in content_lf:
             # to be safe, rebuild the file with exact replace
             import sys
             print(f'Replacing line endings for a block {old_text_lf[:30]}...')
             content = content_lf.replace(old_text_lf, new_text)
        else:
            not_found.append(old_text[:30])

if not_found:
    print('Not found:')
    for nf in not_found:
        print(nf)
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Success')
