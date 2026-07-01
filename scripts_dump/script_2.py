
import sys

with open(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\baocao_latex_raw.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def dump_block(start, num_lines):
    print(f'--- Block starting at line {start} ---')
    for i in range(start-1, start-1+num_lines):
        if i < len(lines):
            print(f'{i+1}: {lines[i].rstrip()}')

dump_block(1617, 40)
dump_block(1715, 60)
dump_block(1771, 60)
dump_block(1871, 60)
