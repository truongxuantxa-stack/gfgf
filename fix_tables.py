import re

file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def process_table(match):
    table_type = match.group(2) # table or longtable
    table_text = match.group(1)
    
    # We only process if it has \\hline to be safe, but all of them do.
    # Split table text into lines.
    lines = table_text.split('\n')
    
    new_lines = []
    extracted_text = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # If it's a structural line (not a table row), keep it
        if line.startswith(r'\begin') or line.startswith(r'\end') or line.startswith(r'\caption') or line.startswith(r'\centering') or line.startswith(r'\hline') or not line.strip() or line.startswith(r'\textbf{'):
            # wait, \textbf{ could be a row! 
            # In LaTeX, table rows end with \\.
            if r'\\' not in line and not line.strip().endswith(r'\\'):
                new_lines.append(line)
                i += 1
                continue
                
        # It's a row. Let's gather the full row (might span multiple lines, though usually it's one line)
        row = line
        while r'\\' not in row and i + 1 < len(lines) and not lines[i+1].startswith(r'\hline'):
             i += 1
             row += '\n' + lines[i]
             
        # Check if row is bad
        row_clean = row.strip()
        is_bad = False
        if len(row_clean) > 300:
            is_bad = True
        elif r'\textbf{b.' in row_clean or r'\textbf{c.' in row_clean or r'\textbf{d.' in row_clean or r'\textbf{e.' in row_clean:
            is_bad = True
        elif row_clean.startswith('Đối với nhóm') or row_clean.startswith('Đối với đường'):
            is_bad = True
            
        if is_bad:
            # Extract text
            cells = row_clean.split('&')
            for cell in cells:
                # remove trailing \\
                cell = re.sub(r'\\\\\s*$', '', cell)
                cell_clean = cell.strip()
                if cell_clean and cell_clean != '-':
                    extracted_text.append(cell_clean)
        else:
            new_lines.append(row)
            
        i += 1
        
    # Reconstruct table
    clean_table = '\n'.join(new_lines)
    
    if extracted_text:
        return clean_table + '\n\n' + '\n\n'.join(extracted_text)
    else:
        return clean_table

pattern = r'(\\begin\{(table|longtable)\}.*?\\end\{\2\})'
content_fixed = re.sub(pattern, process_table, content, flags=re.DOTALL)

with open(r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep_fixed.tex', 'w', encoding='utf-8') as f:
    f.write(content_fixed)
