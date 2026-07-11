import re

with open('do_an_tot_nghiep.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Add \usepackage{array} if not present
if '\\usepackage{array}' not in content:
    content = content.replace('\\usepackage{longtable}', '\\usepackage{longtable}\n\\usepackage{array}')

# Find the specific tables containing Hybrid Nutrition Scanner and fix their columns
# Table at line 1129: \begin{longtable}{|p{4cm}|p{4cm}|p{7cm}|}
content = content.replace('\\begin{longtable}{|p{4cm}|p{4cm}|p{7cm}|}', '\\begin{longtable}{|>{\\raggedright\\arraybackslash}p{4cm}|>{\\raggedright\\arraybackslash}p{4cm}|>{\\raggedright\\arraybackslash}p{7cm}|}')

# Table at line 1227: \begin{longtable}{|p{4.5cm}|p{3cm}|p{4.5cm}|p{3cm}|}
content = content.replace('\\begin{longtable}{|p{4.5cm}|p{3cm}|p{4.5cm}|p{3cm}|}', '\\begin{longtable}{|>{\\raggedright\\arraybackslash}p{4.5cm}|>{\\raggedright\\arraybackslash}p{3cm}|>{\\raggedright\\arraybackslash}p{4.5cm}|>{\\raggedright\\arraybackslash}p{3cm}|}')

# Table at line 4160: \begin{longtable}{|p{3cm}|p{4cm}|p{4cm}|p{4cm}|}
content = content.replace('\\begin{longtable}{|p{3cm}|p{4cm}|p{4cm}|p{4cm}|}', '\\begin{longtable}{|>{\\raggedright\\arraybackslash}p{3cm}|>{\\raggedright\\arraybackslash}p{4cm}|>{\\raggedright\\arraybackslash}p{4cm}|>{\\raggedright\\arraybackslash}p{4cm}|}')

# Also fix the one at line 564 if needed: \begin{longtable}{|p{2cm}|p{4.5cm}|p{9cm}|}
content = content.replace('\\begin{longtable}{|p{2cm}|p{4.5cm}|p{9cm}|}', '\\begin{longtable}{|>{\\raggedright\\arraybackslash}p{2cm}|>{\\raggedright\\arraybackslash}p{4.5cm}|>{\\raggedright\\arraybackslash}p{9cm}|}')

with open('do_an_tot_nghiep.tex', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed raggedright for tables.')
