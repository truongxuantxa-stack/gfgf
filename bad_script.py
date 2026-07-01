"
file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = []

old_1_1 = '''\\textbf{Gợi ý chèn Bảng 1.1. Các yêu cầu chính của hệ thống}

\\textbf{Nhóm yêu cầu}

\\textbf{Nội dung}'''
if old_1_1 in content:
    print('Found 1.1!')
else:
    print('1.1 missing')

old_3_x_2 = '''\\textbf{Thành phần}

\\textbf{Điều kiện đánh giá}

\\textbf{Tác động đến điểm}

Protein'''
if old_3_x_2 in content:
    print('Found 3.x_2!')
else:
    print('3.x_2 missing')

old_3_x_5 = '''\\textbf{Nhóm insight}

\\textbf{Severity}

\\textbf{Vai trò hiển thị}

Cảnh báo nguy cơ'''
if old_3_x_5 in content:
    print('Found 3.x_5!')
else:
    print('3.x_5 missing')

"