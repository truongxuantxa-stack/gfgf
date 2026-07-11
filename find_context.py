import json

targets = [
    "fig:tong_quan_bai_toan",
    "fig:data_access_architecture"
]

with open("do_an_tot_nghiep.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

results = []
for i, line in enumerate(lines):
    for t in targets:
        if t in line:
            # get 5 lines before and 5 lines after
            context = lines[max(0, i-5):min(len(lines), i+6)]
            results.append({
                "target": t,
                "line": i+1,
                "context": "".join(context)
            })

print(json.dumps(results, indent=2, ensure_ascii=False))
