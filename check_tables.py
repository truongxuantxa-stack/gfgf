import re

file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all tables and longtables
pattern = r'(\\begin\{(table|longtable)\}.*?\\end\{\2\})'
matches = re.finditer(pattern, content, flags=re.DOTALL)

for m in matches:
    table_text = m.group(1)
    # Check for long lines in table
    lines = table_text.split('\n')
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)
    
    caption_match = re.search(r'\\caption\{(.*?)\}', table_text)
    caption = caption_match.group(1) if caption_match else 'No caption'
    
    if max_len > 200:  # Arbitrary threshold for a 'long' paragraph
        print(f'Table at line {content[:m.start()].count(chr(10))+1}: {caption} (Max line length: {max_len})')
