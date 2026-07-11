import re

with open('do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the typo >_{ to >{
content = content.replace('>_{\\raggedright\\arraybackslash}', '>{\\raggedright\\arraybackslash}')

with open('do_an_tot_nghiep.tex', 'w', encoding='utf-8') as f:
    f.write(content)
print('Typo fixed.')
