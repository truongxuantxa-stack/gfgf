import zipfile, re

docx_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\Bao cao do an_01 (1).docx'
try:
    with zipfile.ZipFile(docx_path) as z:
        with z.open('word/document.xml') as f:
            content = f.read().decode('utf-8')
except:
    docx_path = r'c:\Users\Hi Windows 10\Videos\baocao_webdinhduong\Báo cáo đồ án_01 (1).docx'
    with zipfile.ZipFile(docx_path) as z:
        with z.open('word/document.xml') as f:
            content = f.read().decode('utf-8')

paragraphs = re.findall(r'<w:p[ >].*?</w:p>', content, re.DOTALL)
for para in paragraphs:
    style_m = re.search(r'<w:pStyle w:val="Heading(\d)"/>', para)
    if style_m:
        heading_level = style_m.group(1)
        texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', para)
        text = ''.join(texts)
        if text.strip():
            prefix = '  ' * (int(heading_level) - 1)
            print(f'{prefix}H{heading_level}: {text[:120]}')
