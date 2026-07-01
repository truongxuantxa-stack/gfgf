
with open(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.bak', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(1620, 1630):
    print(lines[i].strip())
