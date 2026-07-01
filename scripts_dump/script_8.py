
with open(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Tác động đến điểm' in line:
        for j in range(i-10, i+10):
            print(f'{j+1}: {lines[j].strip()}')
        break
