
file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

bib_content = r'''\bibitem{who_healthy_lifestyle}
World Health Organization (WHO) (n.d.).
\textit{A healthy lifestyle - WHO recommendations}.
World Health Organization.
Truy cập ngày 30/06/2026, từ \url{https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations}

\end{thebibliography}'''

content = content.replace(r'\end{thebibliography}', bib_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Added WHO bibliography')
