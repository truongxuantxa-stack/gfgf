
file_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

bib_content = r'''
\clearpage
\addcontentsline{toc}{chapter}{TÀI LIỆU THAM KHẢO}
\renewcommand{\bibname}{\centering TÀI LIỆU THAM KHẢO}
\begin{thebibliography}{9}

\bibitem{mifflin1990}
Mifflin, M. D., St Jeor, S. T., Hill, L. A., et al. (1990).
\textit{A new predictive equation for resting energy expenditure in healthy individuals}.
The American Journal of Clinical Nutrition.
Truy cập ngày 30/06/2026, từ \url{https://pubmed.ncbi.nlm.nih.gov/2305711/}

\end{thebibliography}
\end{document}'''

content = content.replace(r'\end{document}', bib_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Added bibliography')
