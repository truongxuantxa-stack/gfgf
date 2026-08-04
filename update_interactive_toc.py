import re

with open("slide_baove.tex", "r", encoding="utf-8") as f:
    content = f.read()

idx_backup_start = content.find("% --- BACKUP B1 ---")
if idx_backup_start == -1:
    print("Cannot find BACKUP B1")
    exit(1)

idx_toc_start = content.find(r"\begin{frame}[label=backup_toc_1]")
part1 = content[:idx_toc_start]
part_slides = content[idx_backup_start:]

tocs = r"""\begin{frame}[label=backup_toc_master]{Mục lục Backup (Q\&A)}
\hypertarget{backup_toc_target}{}
    \vspace{0.5cm}
    \begin{columns}[T]
        \begin{column}{0.55\textwidth}
            \begin{itemize}
                \setlength\itemsep{0.6cm}
                \Large
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b1_target}{\textbf{B1. Thuật toán Meal Planner}}
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b2_target}{\textbf{B2. Đánh giá Sức khỏe (Health Score)}}
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b3_target}{\textbf{B3. Thuật toán TDEE (EMA)}}
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b4_target}{\textbf{B4. Kiến trúc Cơ sở dữ liệu}}
            \end{itemize}
        \end{column}
        \begin{column}{0.45\textwidth}
            \begin{itemize}
                \setlength\itemsep{0.6cm}
                \Large
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b5_target}{\textbf{B5. Phân tích Thực phẩm}}
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b6_target}{\textbf{B6. Xử lý Ảnh \& Barcode}}
                \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{subtoc_b7_target}{\textbf{B7. Xác thực \& Phân quyền}}
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

% --- SUB-TOCS ---

\begin{frame}[label=subtoc_b1]{Mục lục Chi tiết: B1. Thuật toán Meal Planner}
\hypertarget{subtoc_b1_target}{}
    \vspace{0.5cm}
    \begin{itemize}
        \setlength\itemsep{0.5cm}
        \Large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b1_1_target}{B1.1: Toán học đằng sau Meal Planner}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b1_2_target}{B1.2: Thuật toán Khử Gauss + Partial Pivoting}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b1_3_target}{B1.3: Ưu điểm của phương pháp Khử Gauss}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b1_4_target}{B1.4: Xử lý ngoại lệ (Edge Cases)}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b1_5_target}{B1.5: Giải đáp - Lựa chọn thuật toán}
    \end{itemize}
\end{frame}

\begin{frame}[label=subtoc_b2]{Mục lục Chi tiết: B2. Đánh giá Sức khỏe}
\hypertarget{subtoc_b2_target}{}
    \vspace{0.3cm}
    \begin{itemize}
        \setlength\itemsep{0.4cm}
        \large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_0_target}{B2.0: Luồng tổng hợp Health Insights}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_1_target}{B2.1: RDI theo giới tính}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_2_target}{B2.2: Chấm điểm — Phân loại 3 tầng}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_3_target}{B2.3: Weighted Penalty — Hàm phạt tỷ lệ}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_4_target}{B2.4: Điểm thưởng}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_5_target}{B2.5: Nhận biết ngữ cảnh}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_6_target}{B2.6: Hệ số trượt \& Giới hạn trần}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b2_7_target}{B2.7: Tổng kết luồng tính điểm}
    \end{itemize}
\end{frame}

\begin{frame}[label=subtoc_b3]{Mục lục Chi tiết: B3. Thuật toán TDEE}
\hypertarget{subtoc_b3_target}{}
    \vspace{0.5cm}
    \begin{itemize}
        \setlength\itemsep{0.5cm}
        \Large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b3_1_target}{B3.1: EMA \& Bộ Lọc Thông Thấp}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b3_2_target}{B3.2: Ý nghĩa của trọng số $\alpha$}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b3_3_target}{B3.3: Warm-up 14 ngày \& Anti-Smoothing}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b3_4_target}{B3.4: Guardrails — Chống nhiễu dữ liệu}
    \end{itemize}
\end{frame}

\begin{frame}[label=subtoc_b4]{Mục lục Chi tiết: B4. Kiến trúc CSDL}
\hypertarget{subtoc_b4_target}{}
    \vspace{0.5cm}
    \begin{itemize}
        \setlength\itemsep{0.5cm}
        \Large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b4_1_target}{B4.1: Sơ đồ CSDL — Các bảng chính}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b4_2_target}{B4.2: Quan hệ \& Điểm thiết kế nổi bật}
    \end{itemize}
\end{frame}

\begin{frame}[label=subtoc_b5]{Mục lục Chi tiết: B5. Phân tích Thực phẩm}
\hypertarget{subtoc_b5_target}{}
    \vspace{0.5cm}
    \begin{itemize}
        \setlength\itemsep{0.5cm}
        \Large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b5_0_target}{B5.0: Luồng tổng hợp thuật toán}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b5_1_target}{B5.1: Mật độ Dinh dưỡng (Nutrient Density)}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b5_2_target}{B5.2: Double Medical Protection}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b5_3_target}{B5.3: Cơ chế miễn trừ phạt (Triage)}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b5_4_target}{B5.4: Trích xuất thói quen \& Đánh giá}
    \end{itemize}
\end{frame}

\begin{frame}[label=subtoc_b6]{Mục lục Chi tiết: B6. Xử lý Ảnh \& Barcode}
\hypertarget{subtoc_b6_target}{}
    \vspace{0.5cm}
    \begin{itemize}
        \setlength\itemsep{0.5cm}
        \Large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b6_1_target}{B6.1: Cơ chế xác minh cộng đồng}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b6_2_target}{B6.2: Luồng xử lý ảnh AI Vision}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b6_3_target}{B6.3: Xử lý ngoại lệ JSON \& Validation}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b6_4_target}{B6.4: Quét Barcode \& Fallback nhiều lớp}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b6_5_target}{B6.5: Quản trị Rủi ro API}
    \end{itemize}
\end{frame}

\begin{frame}[label=subtoc_b7]{Mục lục Chi tiết: B7. Xác thực \& Phân quyền}
\hypertarget{subtoc_b7_target}{}
    \vspace{0.2cm}
    \begin{itemize}
        \setlength\itemsep{0.35cm}
        \large
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_1_target}{B7.1: Phân loại Route theo mức bảo vệ}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_2_target}{B7.2: ProtectedRoute hoạt động thế nào?}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_3_target}{B7.3: AuthOnlyRoute khác gì ProtectedRoute?}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_4_target}{B7.4: Axios interceptor xử lý token}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_5_target}{B7.5: Luồng xử lý khi Access Token hết hạn}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_6_target}{B7.6: Sử dụng useQuery đọc dữ liệu}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_7_target}{B7.7: Sử dụng useMutation ghi dữ liệu}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_8_target}{B7.8: Luồng đồng bộ dữ liệu tới Dashboard}
        \item[\textcolor{NutriDark}{$\blacktriangleright$}] \hyperlink{b7_9_target}{B7.9: Vai trò của Custom hook}
    \end{itemize}
\end{frame}

"""

def process_slides(text):
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        match = re.search(r'\\begin\{frame\}(?:\[(.*?)\])?\{(?:.*?BACKUP\s+B(\d+)\.(\d+).*?)\}', line)
        if match:
            options = match.group(1) or ""
            x = match.group(2)
            y = match.group(3)
            
            opts = [opt.strip() for opt in options.split(',') if opt.strip() and not opt.strip().startswith('label=')]
            opts.append(f'label=b{x}_{y}')
            new_options = ', '.join(opts)
            
            new_line = re.sub(r'\\begin\{frame\}(?:\[.*?\])?', f'\\\\begin{{frame}}[{new_options}]', line, count=1)
            out.append(new_line)
            
            target_str = f'\\hypertarget{{b{x}_{y}_target}}{{}}'
            if i+1 < len(lines) and target_str in lines[i+1]:
                pass
            elif i+1 < len(lines) and '\\hypertarget' in lines[i+1]:
                lines[i+1] = target_str
            else:
                out.append(target_str)
                
        else:
            out.append(line)
        i += 1
    return '\n'.join(out)

processed_slides = process_slides(part_slides)
final_content = part1 + tocs + processed_slides

with open("slide_baove.tex", "w", encoding="utf-8") as f:
    f.write(final_content)

print("Done updating TOCs and slide labels.")
