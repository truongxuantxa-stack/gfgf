
import re

def process_tex(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        is_table_title = False
        caption_text = ''
        
        m1 = re.match(r'\\textbf{Gợi ý chèn (Bảng\s+[\d\.x]+)[.:]?\s*(.*)}', line)
        m2 = re.match(r'\\textbf{(Bảng\s+[\d\.x]+)[.:]?\s*(.*)}', line)
        m3 = re.match(r'(Bảng\s+[\d\.x]+)\s+(trình bày\s+.*|tóm tắt\s+.*)', line)
        
        if m1:
            caption_text = m1.group(2).strip()
            is_table_title = True
        elif m2:
            caption_text = m2.group(2).strip()
            is_table_title = True
        elif m3:
            caption_text = m3.group(2).strip()
            is_table_title = True
        elif line == r'\textbf{Thành phần}' and lines[i+2].strip() == r'\textbf{Điều kiện đánh giá}':
            caption_text = 'Quy tắc cộng trừ điểm cho các thành phần dinh dưỡng'
            is_table_title = True
            # we need to step back so the loop below parses the header correctly
            i = i - 1
        elif line == r'\textbf{Nhóm insight}' and lines[i+2].strip() == r'\textbf{Severity}':
            caption_text = 'Phân loại các nhóm insight theo severity'
            is_table_title = True
            i = i - 1
            
        if is_table_title:
            headers = []
            j = i + 1
            
            while j < len(lines) and not lines[j].strip():
                j += 1
                
            while j < len(lines):
                l_strip = lines[j].strip()
                if not l_strip:
                    j += 1
                    continue
                if l_strip.startswith(r'\textbf{') and not (l_strip.startswith(r'\textbf{Bảng') or l_strip.startswith(r'\textbf{Hình')):
                    m_head = re.match(r'\\textbf{(.*?)}', l_strip)
                    if m_head:
                        headers.append(m_head.group(1))
                    else:
                        headers.append(l_strip.replace(r'\textbf{', '').replace('}', ''))
                    j += 1
                else:
                    break
            
            if len(headers) > 0:
                num_cols = len(headers)
                rows = []
                current_row = []
                
                while j < len(lines):
                    l_strip = lines[j].strip()
                    if not l_strip:
                        j += 1
                        continue
                    
                    if l_strip.startswith(r'\section') or l_strip.startswith(r'\subsection') or l_strip.startswith(r'\chapter') or l_strip.startswith(r'\begin{') or l_strip.startswith(r'Bảng ') or l_strip.startswith(r'Hình ') or l_strip.startswith(r'\textbf{Bảng') or l_strip.startswith(r'\textbf{Hình') or l_strip.startswith(r'\textbf{Gợi ý'):
                        break
                    
                    # Some lines might be paragraphs and not part of the table. Usually table cells are short.
                    # If we encounter a very long line, it might be the end of the table and start of text.
                    # But some table cells in descriptions can be long. Let's just trust the section/textbf boundaries.
                    # Wait, if there's plain text after the table, it might get swallowed!
                    # Tables usually end when a new paragraph starts that is NOT a cell.
                    # How to detect end of table? Usually the rows come in exact multiples of num_cols.
                    # If we find a block that doesn't fit, we might have over-read. 
                    
                    # Actually, for safety, let's stop reading if we hit a line that is too long or clearly normal text.
                    # Wait, table cells CAN be long! (Mô tả yêu cầu).
                    
                    current_row.append(l_strip)
                    j += 1
                    
                    if len(current_row) == num_cols:
                        rows.append(current_row)
                        current_row = []
                
                # if there is a leftover row, we over-read. Let's put those lines back.
                if current_row:
                    j -= len(current_row)
                
                out_lines.append('\\begin{table}[htbp]\n')
                out_lines.append('\\centering\n')
                if caption_text:
                    out_lines.append(f'\\caption{{{caption_text}}}\n')
                
                # format columns
                if num_cols == 2: col_fmt = '|p{5cm}|p{10cm}|'
                elif num_cols == 3: col_fmt = '|p{4cm}|p{4cm}|p{7cm}|'
                elif num_cols == 4: col_fmt = '|p{3cm}|p{3cm}|p{4cm}|p{5cm}|'
                else: col_fmt = '|'.join([f'p{{{15/num_cols:.1f}cm}}' for _ in range(num_cols)])
                
                out_lines.append(f'\\begin{{tabular}}{{{col_fmt}}}\n')
                out_lines.append('\\hline\n')
                out_lines.append(' & '.join([f'\\textbf{{{h}}}' for h in headers]) + ' \\\\\n')
                out_lines.append('\\hline\n')
                
                for row in rows:
                    out_lines.append(' & '.join(row) + ' \\\\\n')
                    out_lines.append('\\hline\n')
                
                out_lines.append('\\end{tabular}\n')
                out_lines.append('\\end{table}\n')
                
                # Advance i to j
                i = j
                continue

        out_lines.append(lines[i])
        i += 1
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

process_tex(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex', r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep_fixed.tex')
