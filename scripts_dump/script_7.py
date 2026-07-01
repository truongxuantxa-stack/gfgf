
with open(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

in_table = False
table_lines = []
for i, line in enumerate(lines):
    if line.startswith(r'\textbf{Bảng') or (line.startswith('Bảng') and 'trình bày' in line):
        print(f'--- Table Start ---: {line}')
        for j in range(i+1, min(i+10, len(lines))):
            print(lines[j])
        break
