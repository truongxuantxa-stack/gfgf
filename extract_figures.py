import re
import json

file_path = "do_an_tot_nghiep.tex"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

figures = []
i = 0
while i < len(lines):
    if r"\begin{figure}" in lines[i]:
        fig_start = i
        caption = None
        label = None
        
        # Find caption and label
        for j in range(i, len(lines)):
            if r"\caption{" in lines[j]:
                m = re.search(r"\\caption{([^}]+)}", lines[j])
                if m: caption = m.group(1)
            if r"\label{" in lines[j]:
                m = re.search(r"\\label{([^}]+)}", lines[j])
                if m: label = m.group(1)
            if r"\end{figure}" in lines[j]:
                fig_end = j
                i = j
                break
        
        # Get context (up to 3 non-empty lines before \begin{figure})
        context = []
        for j in range(fig_start - 1, max(-1, fig_start - 20), -1):
            line = lines[j].strip()
            if line and not line.startswith("%"):
                context.insert(0, line)
                if len(context) == 3:
                    break
        context_str = " ".join(context)
        
        # Check rules
        missing_label = label is None
        missing_ref = False
        bad_wording = False
        bad_words_found = []
        
        if not missing_label:
            if f"\\ref{{{label}}}" not in context_str:
                missing_ref = True
        else:
            missing_ref = True
            
        bad_words = ["hình sau", "hình dưới đây", "bên dưới", "như sau", "minh hoạ sau", "dưới đây"]
        for bw in bad_words:
            if bw in context_str.lower():
                bad_wording = True
                bad_words_found.append(bw)
                
        figures.append({
            "line": fig_start + 1,
            "caption": caption,
            "label": label,
            "context_snippet": context[-1] if context else "",
            "missing_label": missing_label,
            "missing_ref": missing_ref,
            "bad_wording": bad_wording,
            "bad_words_found": bad_words_found
        })
    i += 1

# Generate markdown report
md = "# Báo cáo rà soát hình ảnh\n\n"
for idx, fig in enumerate(figures):
    md += f"## Hình {idx + 1}: {fig['caption'] or 'Không có caption'} (Dòng {fig['line']})\n"
    md += f"- **Label**: `{fig['label'] or 'THIẾU'}`\n"
    
    issues = []
    if fig['missing_label']: issues.append("Thiếu `\\label`")
    if fig['missing_ref']: issues.append(f"Không tìm thấy `\\ref{{{fig['label']}}}` trong đoạn văn trước hình.")
    if fig['bad_wording']: issues.append(f"Sử dụng từ ngữ không chuẩn: {', '.join(fig['bad_words_found'])}")
    
    if issues:
        md += "- **Vấn đề**:\n"
        for issue in issues:
            md += f"  - {issue}\n"
    else:
        md += "- **Trạng thái**: Hợp lệ\n"
        
    md += f"- **Đoạn dẫn hiện tại**: {fig['context_snippet']}\n"
    md += "\n"

with open("figures_report.md", "w", encoding="utf-8") as f:
    f.write(md)

print("Report saved to figures_report.md")
