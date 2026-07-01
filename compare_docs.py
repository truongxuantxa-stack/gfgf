import zipfile
import re
import xml.etree.ElementTree as ET

def extract_clean_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            content = z.read('word/document.xml')
    except:
        docx_path = docx_path.replace('Báo cáo đồ án_01 (1).docx', 'Bao cao do an_01 (1).docx')
        with zipfile.ZipFile(docx_path) as z:
            content = z.read('word/document.xml')
            
    root = ET.fromstring(content)
    # XML namespace for word
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    paragraphs = []
    for p in root.findall('.//w:p', ns):
        texts = p.findall('.//w:t', ns)
        text = ''.join([t.text for t in texts if t.text])
        if text.strip():
            paragraphs.append(text.strip())
            
    return paragraphs

def extract_clean_text_from_tex(tex_path):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove everything before \chapter{TỔNG QUAN ĐỀ TÀI}
    match = re.search(r'\\chapter\{TỔNG QUAN ĐỀ TÀI\}', content)
    if match:
        content = content[match.start():]
    
    # Remove everything after \chapter{KẾT LUẬN} and its content
    # Actually just remove \end{document} and bibliography
    
    content = re.sub(r'%.*?$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\\begin\{.*?\}(.*?)\\end\{.*?\}', r'\1', content, flags=re.DOTALL)
    content = re.sub(r'\\[a-zA-Z]+\*?\{(.*?)\}', r'\1', content)
    content = re.sub(r'\\[a-zA-Z]+', '', content)
    
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    return lines

docx_file = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\Báo cáo đồ án_01 (1).docx'
tex_file = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\do_an_tot_nghiep.tex'

docx_paras = extract_clean_text_from_docx(docx_file)
tex_paras = extract_clean_text_from_tex(tex_file)

# Find start index in DOCX for "TỔNG QUAN ĐỀ TÀI"
start_idx = 0
for i, p in enumerate(docx_paras):
    if "TỔNG QUAN ĐỀ TÀI" in p:
        start_idx = i
        break

# Filter out early docx pages
docx_paras = docx_paras[start_idx:]

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

tex_norm_str = ' '.join([normalize(p) for p in tex_paras])

missing = []
for p in docx_paras:
    p_norm = normalize(p)
    if len(p_norm) < 40: 
        continue # Ignore short titles or table headers
    
    if p_norm not in tex_norm_str:
        # Check if at least 50% of the words are sequentially in tex
        words = p_norm.split()
        if len(words) > 10:
            chunk = ' '.join(words[:10])
            if chunk not in tex_norm_str:
                missing.append(p)

print(f"Total paragraphs in DOCX (content): {len(docx_paras)}")
print(f"Found {len(missing)} potentially missing paragraphs in TEX.")

for i, chunk in enumerate(missing):
    print(f"[{i+1}] {chunk[:200]}...")
