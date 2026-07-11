import json

targets = [
    "def\\ga>{\\raggedright\\arraybackslash}p{1.85cm}",
    "chia sẻ các thành phần xử lý.",
    "subsection{Thiết kế xác thực API}",
    "giữ giao diện nhất quán.",
    "hạn chế số bước thao tác.",
    "giảm lặp logic giữa các module.",
    "lặp lại công thức ở phía client.",
    "trình bày trong Phụ lục C.",
    "hạn chế tải không cần thiết cho hệ thống."
]

with open("do_an_tot_nghiep.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

results = []
for i, line in enumerate(lines):
    for t in targets:
        if t in line:
            results.append({"target": t, "line": i+1, "content": line.rstrip('\n')})

print(json.dumps(results, indent=2, ensure_ascii=False))
