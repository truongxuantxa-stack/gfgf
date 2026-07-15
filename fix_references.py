import re

file_path = 'do_an_tot_nghiep.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Bảng 4.5
content = content.replace(
    'định hiện tượng này \\cite{nunes2022, muller2013}. & Trong hướng phát triển, có thể bổ sung dữ liệu thành',
    'định hiện tượng này \\cite{muller2013, nunes2022}. & Trong hướng phát triển, có thể bổ sung dữ liệu thành'
)

# 2. Xoá hall2008
hall_regex = r'\\bibitem\{hall2008\}\nHall, K\. D\. \(2008\),\n"What is the required energy deficit per unit weight loss\?",\n\\textit\{International Journal of Obesity\}, Tập 32, Số 3, Trang 573--576\. DOI: 10\.1038/sj\.ijo\.0803720\.\n\n?'
content = re.sub(hall_regex, '', content)

# 3. mifflin1990
mifflin_old = r'\\bibitem\{mifflin1990\}\nMifflin, M\. D\., St Jeor, S\. T\., Hill, L\. A\., et al\. \(1990\),\n\\textit\{A new predictive equation for resting energy expenditure in healthy individuals\}\.\nThe American Journal of Clinical Nutrition\.\nTruy cập ngày 30/06/2026, từ \\url\{https://pubmed\.ncbi\.nlm\.nih\.gov/2305711/\}'
mifflin_new = r'\\bibitem{mifflin1990}\nMifflin, M. D., St Jeor, S. T., Hill, L. A., et al. (1990),\n"A new predictive equation for resting energy expenditure in healthy individuals",\n\\textit{The American Journal of Clinical Nutrition}, Tập 51, Số 2, Trang 241--247.'
content = re.sub(mifflin_old, mifflin_new, content)

# 4. AHA added sugars
aha1_old = r'\\bibitem\{aha_addedsugars\}\nAHA,\n"Added Sugars",\n\\textit\{American Heart Association\}, Truy cập ngày 12/07/2026, từ \\url\{https://www\.heart\.org/en/healthy-living/healthy-eating/eat-smart/sugar/added-sugars\}\.'
aha1_new = r'\\bibitem{aha_addedsugars}\nAmerican Heart Association,\n"Added Sugars",\n\\textit{\\url{https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/sugar/added-sugars}}, truy cập ngày 12/07/2026.'
content = re.sub(aha1_old, aha1_new, content)

# 5. AHA sodium
aha2_old = r'\\bibitem\{aha_sodium\}\nAHA,\n"How much sodium should I eat per day\?",\n\\textit\{American Heart Association\}, Truy cập ngày 12/07/2026, từ \\url\{https://www\.heart\.org/en/healthy-living/healthy-eating/eat-smart/sodium/how-much-sodium-should-i-eat-per-day\}\.'
aha2_new = r'\\bibitem{aha_sodium}\nAmerican Heart Association,\n"How much sodium should I eat per day?",\n\\textit{\\url{https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/sodium/how-much-sodium-should-i-eat-per-day}}, truy cập ngày 12/07/2026.'
content = re.sub(aha2_old, aha2_new, content)

# 6. FDA added sugars
fda_old = r'\\bibitem\{fda_addedsugars\}\nFDA,\n"Added Sugars on the New Nutrition Facts Label",\n\\textit\{U\.S\. Food and Drug Administration\}, Truy cập ngày 12/07/2026, từ \\url\{https://www\.fda\.gov/food/nutrition-facts-label/added-sugars-nutrition-facts-label\}\.'
fda_new = r'\\bibitem{fda_addedsugars}\nU.S. Food and Drug Administration,\n"Added Sugars on the New Nutrition Facts Label",\n\\textit{\\url{https://www.fda.gov/food/nutrition-facts-label/added-sugars-nutrition-facts-label}}, truy cập ngày 12/07/2026.'
content = re.sub(fda_old, fda_new, content)

# 7. FAO WHO UNU
fao_who_old = r'\\bibitem\{fao_who_unu_2001\}\nFAO/WHO/UNU\. \(2004\),\n"Human Energy Requirements: Report of a Joint FAO/WHO/UNU Expert Consultation, Rome, 17–24 October 2001"\.\n\\textit\{FAO Food and Nutrition Technical Report Series No\. 1\}\.\nRome: Food and Agriculture Organization of the United Nations\. Truy cập ngày 11/07/2026, từ \\url\{https://www\.fao\.org/4/y5686e/y5686e07\.htm\}'
fao_who_new = r'\\bibitem{fao_who_unu_2001}\nFAO/WHO/UNU (2004),\n"Human Energy Requirements: Report of a Joint FAO/WHO/UNU Expert Consultation, Rome, 17–24 October 2001",\n\\textit{FAO Food and Nutrition Technical Report Series No. 1},\nFood and Agriculture Organization of the United Nations, Rome.'
content = re.sub(fao_who_old, fao_who_new, content)

# 8. FAO 2003
fao2003_old = r'\\bibitem\{fao_2003\}\nFood and Agriculture Organization of the United Nations \(2003\),\n\\textit\{Food Energy -- Methods of Analysis and Conversion Factors\},\nFAO Food and Nutrition Paper 77, Rome\. Truy cập ngày 11/07/2026, từ \\url\{https://www\.fao\.org/4/y5022e/y5022e04\.htm\}'
fao2003_new = r'\\bibitem{fao_2003}\nFood and Agriculture Organization of the United Nations (2003),\n\\textit{Food Energy -- Methods of Analysis and Conversion Factors},\nFAO Food and Nutrition Paper 77, Rome.'
content = re.sub(fao2003_old, fao2003_new, content)

# 9. nhlbiPracticalGuide2000
nhlbi_old = r'\\bibitem\{nhlbiPracticalGuide2000\}\nNational Heart, Lung, and Blood Institute \(2000\),\n\\textit\{The Practical Guide: Identification, Evaluation, and Treatment of Overweight and Obesity in Adults\}\.\nNational Institutes of Health\. Truy cập ngày 15/07/2026, từ \\url\{https://www\.nhlbi\.nih\.gov/files/docs/guidelines/prctgd_c\.pdf\}'
nhlbi_new = r'\\bibitem{nhlbiPracticalGuide2000}\nNational Heart, Lung, and Blood Institute (2000),\n\\textit{The Practical Guide: Identification, Evaluation, and Treatment of Overweight and Obesity in Adults},\nNational Institutes of Health.'
content = re.sub(nhlbi_old, nhlbi_new, content)

# 10. whoObesityOverweight2025
who_old = r'\\bibitem\{whoObesityOverweight2025\}\nWorld Health Organization \(2025\),\n"Obesity and overweight"\.\nCập nhật ngày 08/12/2025, truy cập ngày 15/07/2026, từ \\url\{https://www\.who\.int/news-room/fact-sheets/detail/obesity-and-overweight\}'
who_new = r'\\bibitem{whoObesityOverweight2025}\nWorld Health Organization (2025),\n"Obesity and overweight",\n\\textit{\\url{https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight}}, truy cập ngày 15/07/2026.'
content = re.sub(who_old, who_new, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing.")
