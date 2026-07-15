import re

file_path = 'do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(\\begin\{thebibliography\}.*?\n)(.*?)(\\end\{thebibliography\})', content, flags=re.DOTALL)
if not match:
    print('Could not find thebibliography')
    exit(1)

preamble = match.group(1)
bib_content = match.group(2)
postamble = match.group(3)

# Split into bibitems
# Regex to match \bibitem{...} and everything until the next \bibitem or end of string
bib_items = re.split(r'(?=\\bibitem\{)', bib_content)
# Remove empty items
bib_items = [b for b in bib_items if b.strip()]

vietnamese_items = []
english_items = []

for item in bib_items:
    if 'vien_dinh_duong_2007' in item:
        vietnamese_items.append(item)
    else:
        # Check if year has period after it: (2025). -> (2025),
        item = re.sub(r'(\([0-9]{4}\))\.', r'\1,', item)
        english_items.append(item)

# Sort english items based on the line following \bibitem
def get_sort_key(item):
    lines = item.strip().split('\n')
    if len(lines) > 1:
        # line 0 is \bibitem{...}
        # line 1 is author
        author_line = lines[1].strip()
        # Remove LaTeX commands or quotes at start if any
        author_line = re.sub(r'^(\\\w+\{|``|\")', '', author_line)
        return author_line.lower()
    return ''

english_items.sort(key=get_sort_key)

new_bib_content = ''
for item in vietnamese_items:
    new_bib_content += item
for item in english_items:
    new_bib_content += item

new_content = content[:match.start()] + preamble + new_bib_content + postamble + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Sorted {len(vietnamese_items)} VN items and {len(english_items)} EN items.')
