"""
Chuyển đổi các bảng dài (table + tabular) sang longtable để cho phép ngắt trang.
Fix lỗi regex: dùng hàm đếm ngoặc nhọn thay vì greedy/non-greedy regex.
"""
import re

INPUT = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
OUTPUT = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'

def extract_brace_content(s, start):
    """Extract content inside outermost braces starting at position 'start' (which must be '{')."""
    assert s[start] == '{', f"Expected '{{' at pos {start}, got '{s[start]}'"
    depth = 0
    for i in range(start, len(s)):
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return s[start+1:i], i  # content, end index
    return None, -1  # unmatched

with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()

# Ensure longtable package
if r'\usepackage{longtable}' not in content:
    content = content.replace(r'\usepackage{float}',
                              r'\usepackage{float}' + '\n' + r'\usepackage{longtable}', 1)
    print("Added \\usepackage{longtable}")

lines = content.split('\n')
output_lines = []
i = 0
tables_converted = 0

while i < len(lines):
    line = lines[i]
    
    if re.match(r'\s*\\begin\{table\}\[H\]', line):
        block_start = i
        block_lines = [line]
        i += 1
        
        while i < len(lines):
            block_lines.append(lines[i])
            if re.match(r'\s*\\end\{table\}', lines[i]):
                break
            i += 1
        
        hline_count = sum(1 for bl in block_lines if bl.strip() == r'\hline')
        
        if hline_count >= 8:
            caption = ''
            col_spec = ''
            header_row = ''
            body_lines = []
            in_tabular = False
            header_found = False
            
            for j, bl in enumerate(block_lines):
                stripped = bl.strip()
                
                if re.match(r'\\begin\{table\}', stripped) or stripped == r'\centering' or stripped == r'\end{table}':
                    continue
                elif stripped.startswith(r'\caption{'):
                    # Extract caption using brace counting
                    cap_start = stripped.index('{')
                    cap_content, _ = extract_brace_content(stripped, cap_start)
                    if cap_content is not None:
                        caption = cap_content
                    continue
                elif stripped.startswith(r'\begin{tabular}'):
                    # Extract col_spec using brace counting
                    tab_idx = stripped.index(r'\begin{tabular}') + len(r'\begin{tabular}')
                    brace_pos = stripped.index('{', tab_idx)
                    col_spec_content, _ = extract_brace_content(stripped, brace_pos)
                    if col_spec_content is not None:
                        col_spec = col_spec_content
                    in_tabular = True
                    continue
                elif stripped == r'\end{tabular}':
                    in_tabular = False
                    continue
                elif in_tabular and not header_found:
                    if stripped == r'\hline':
                        continue
                    elif stripped.endswith(r'\\') and '&' in stripped:
                        # This is the header row
                        header_row = bl
                        header_found = True
                        continue
                    else:
                        body_lines.append(bl)
                        continue
                elif in_tabular:
                    body_lines.append(bl)
                # else: skip non-tabular lines outside table body
            
            # Build longtable
            new_block = []
            new_block.append(f'\\begin{{longtable}}{{{col_spec}}}')
            new_block.append(f'\\caption{{{caption}}} \\\\')
            new_block.append(r'\hline')
            if header_row:
                new_block.append(header_row)
                new_block.append(r'\hline')
            new_block.append(r'\endfirsthead')
            new_block.append(r'\hline')
            if header_row:
                new_block.append(header_row)
                new_block.append(r'\hline')
            new_block.append(r'\endhead')
            new_block.append(r'\hline')
            # Clean empty lines from body
            while body_lines and not body_lines[0].strip():
                body_lines.pop(0)
            while body_lines and not body_lines[-1].strip():
                body_lines.pop()
            new_block.extend(body_lines)
            new_block.append(r'\end{longtable}')
            new_block.append('')
            
            output_lines.extend(new_block)
            tables_converted += 1
        else:
            output_lines.extend(block_lines)
    else:
        output_lines.append(line)
    
    i += 1

print(f"Converted {tables_converted} tables to longtable.")

result = '\n'.join(output_lines)

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Written to {OUTPUT}")
