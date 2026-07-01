import re

file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Match tables and longtables
pattern = r'(\\begin\{(table|longtable)\}.*?\\end\{\2\})'
matches = re.finditer(pattern, content, flags=re.DOTALL)

for m in matches:
    table_text = m.group(1)
    caption_match = re.search(r'\\caption\{(.*?)\}', table_text)
    caption = caption_match.group(1) if caption_match else 'No caption'
    
    # Extract rows (between \hline or just lines ending with \\)
    rows = re.findall(r'^(.*?)\\\\\s*$', table_text, flags=re.MULTILINE)
    
    bad_rows = []
    for r in rows:
        # Ignore headers (usually have \textbf for all cells)
        if r.count(r'\textbf{') >= r.count('&') and '&' in r:
            pass # might be header
        
        r_clean = r.strip()
        if len(r_clean) > 300:
            bad_rows.append(r_clean)
            
    if bad_rows:
        print(f'\\nTable: {caption}')
        for br in bad_rows:
            print(f'  [Len {len(br)}] {br[:100]}...')
