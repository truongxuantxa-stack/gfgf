"""
Fix hai vấn đề trong file LaTeX:
1. Xóa các \hline thừa liên tiếp (chỉ giữ lại 1)
2. Đổi \begin{table}[htbp] thành \begin{table}[H] để bảng không float xa
"""
import re

INPUT = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
OUTPUT = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'

with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()

# ── Fix 1: Collapse consecutive \hline lines into a single \hline ─────────────
# Match 2 or more consecutive \hline (with optional whitespace between them)
before = content.count('\\hline')

# Use regex to collapse runs of \hline separated only by whitespace/newlines
# Pattern: one \hline, then one or more additional \hline (with only \n/\r/space between)
content = re.sub(r'(\\hline[ \t]*\r?\n)([ \t]*\\hline[ \t]*\r?\n)+', r'\1', content)

after = content.count('\\hline')
print(f'\\hline count: {before} → {after} (removed {before - after} duplicate lines)')

# ── Fix 2: Replace \begin{table}[htbp] with \begin{table}[H] ─────────────────
# First check if float package is already loaded
if r'\usepackage{float}' not in content and r'\usepackage[H]{float}' not in content:
    # Add float package right after \usepackage{longtable} or similar
    # Find a good insertion point: after \usepackage{array} or \usepackage{booktabs}
    insert_after = [r'\usepackage{longtable}', r'\usepackage{array}', r'\usepackage{booktabs}', r'\usepackage{tabularx}', r'\usepackage{multirow}']
    inserted = False
    for pkg in insert_after:
        if pkg in content:
            content = content.replace(pkg, pkg + '\n\\usepackage{float}', 1)
            print(f'Added \\usepackage{{float}} after {pkg}')
            inserted = True
            break
    if not inserted:
        # Add before \begin{document}
        content = content.replace(r'\begin{document}', r'\usepackage{float}' + '\n' + r'\begin{document}', 1)
        print('Added \\usepackage{float} before \\begin{document}')

# Replace table placement specifiers
old_htbp = content.count(r'\begin{table}[htbp]')
content = content.replace(r'\begin{table}[htbp]', r'\begin{table}[H]')
print(f'Changed {old_htbp} \\begin{{table}}[htbp] → \\begin{{table}}[H]')

# Also fix any remaining [h] or [t] or [b] specifiers on table
old_h = len(re.findall(r'\\begin\{table\}\[h\b', content))
content = re.sub(r'\\begin\{table\}\[h\b[^\]]*\]', r'\\begin{table}[H]', content)
if old_h:
    print(f'Changed {old_h} other table placement specifiers to [H]')

# ── Fix 3: Remove excessive blank lines between tables and paragraphs ─────────
# More than 2 consecutive blank lines → 1 blank line
before_blanks = len(re.findall(r'\n{4,}', content))
content = re.sub(r'\n{4,}', '\n\n', content)
print(f'Collapsed {before_blanks} excessive blank-line blocks (4+ newlines)')

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. Written to {OUTPUT}')
