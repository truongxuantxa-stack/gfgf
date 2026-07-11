import re

with open("do_an_tot_nghiep.tex", "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find: 
# \begin{figure} ... \end{figure} 
# followed by optional blank lines
# followed by a paragraph starting with "Hình \ref{..."
# We will capture:
# Group 1: The text before \begin{figure}
# Group 2: The \begin{figure}...\end{figure} block
# Group 3: The paragraph starting with Hình \ref{...}

pattern = re.compile(
    r"(\\begin\{figure\}.*?\\end\{figure\})\s*\n+(Hình \\ref\{[^\}]+\}[^\n]+)",
    re.DOTALL
)

def replacer(match):
    fig_block = match.group(1)
    para = match.group(2)
    return f"{para}\n\n{fig_block}"

new_content, count = pattern.subn(replacer, content)

if count > 0:
    with open("do_an_tot_nghiep.tex", "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Moved {count} paragraphs before their figures.")
else:
    print("No matches found.")
