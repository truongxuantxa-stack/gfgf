
with open(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\baocao_latex_raw.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(1615, 1655):
    print(f'{i+1}: {lines[i].rstrip()}')
