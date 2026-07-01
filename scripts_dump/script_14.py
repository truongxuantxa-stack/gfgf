
file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

bib_content = r'''\bibitem{fao_who_unu_2001}
Joint FAO/WHO/UNU Expert Consultation (2001).
\textit{Human energy requirements: Report of a Joint FAO/WHO/UNU Expert Consultation}.
Food and Agriculture Organization (FAO).
Truy cập ngày 30/06/2026, từ \url{https://www.fao.org/3/y5686e/y5686e07.htm}

\end{thebibliography}'''

content = content.replace(r'\end{thebibliography}', bib_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Added FAO bibliography')
