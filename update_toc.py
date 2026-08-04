with open("slide_baove.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_content = r"""\begin{frame}[label=backup_toc_1]{Mục lục Backup (1/3): Meal Planner \& Health Score}
\hypertarget{backup_toc_target}{}
    \vspace{0.2cm}
    \begin{columns}[T]
        \begin{column}{0.48\textwidth}
            \textbf{\textcolor{NutriDark}{B1. Thuật toán Meal Planner}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B1.1: Toán học đằng sau Meal Planner
                \item B1.2: Thuật toán Khử Gauss + Partial Pivoting
                \item B1.3: Ưu điểm của phương pháp Khử Gauss
                \item B1.4: Xử lý ngoại lệ (Edge Cases)
                \item B1.5: Giải đáp - Lựa chọn thuật toán
            \end{itemize}
        \end{column}
        
        \begin{column}{0.48\textwidth}
            \textbf{\textcolor{NutriDark}{B2. Đánh giá Sức khỏe (Health Score)}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B2.0: Luồng tổng hợp Health Insights
                \item B2.1: RDI theo giới tính
                \item B2.2: Chấm điểm — Phân loại 3 tầng
                \item B2.3: Weighted Penalty — Hàm phạt tỷ lệ
                \item B2.4: Điểm thưởng
                \item B2.5: Nhận biết ngữ cảnh
                \item B2.6: Hệ số trượt \& Giới hạn trần
                \item B2.7: Tổng kết luồng tính điểm
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}[label=backup_toc_2]{Mục lục Backup (2/3): TDEE, Database \& Food Scoring}
    \vspace{0.2cm}
    \begin{columns}[T]
        \begin{column}{0.48\textwidth}
            \textbf{\textcolor{NutriDark}{B3. Thuật toán TDEE (EMA)}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B3.1: EMA \& Bộ Lọc Thông Thấp
                \item B3.2: Ý nghĩa của trọng số $\alpha$
                \item B3.3: Warm-up 14 ngày \& Anti-Smoothing
                \item B3.4: Guardrails — Chống nhiễu dữ liệu
            \end{itemize}
            
            \vspace{0.4cm}
            \textbf{\textcolor{NutriDark}{B4. Kiến trúc Cơ sở dữ liệu}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B4.1: Sơ đồ CSDL — Các bảng chính
                \item B4.2: Quan hệ \& Điểm thiết kế nổi bật
            \end{itemize}
        \end{column}
        
        \begin{column}{0.48\textwidth}
            \textbf{\textcolor{NutriDark}{B5. Phân tích Thực phẩm (Food Scoring)}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B5.0: Luồng tổng hợp thuật toán
                \item B5.1: Mật độ Dinh dưỡng (Nutrient Density)
                \item B5.2: Double Medical Protection
                \item B5.3: Cơ chế miễn trừ phạt (Triage)
                \item B5.4: Trích xuất thói quen \& Đánh giá
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}[label=backup_toc_3]{Mục lục Backup (3/3): AI Scanner \& Xác thực}
    \vspace{0.2cm}
    \begin{columns}[T]
        \begin{column}{0.48\textwidth}
            \textbf{\textcolor{NutriDark}{B6. Xử lý Ảnh \& Barcode (Scanner)}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B6.1: Cơ chế xác minh cộng đồng
                \item B6.2: Luồng xử lý ảnh AI Vision
                \item B6.3: Xử lý ngoại lệ JSON \& Validation
                \item B6.4: Quét Barcode \& Fallback nhiều lớp
                \item B6.5: Quản trị Rủi ro API
            \end{itemize}
        \end{column}
        
        \begin{column}{0.48\textwidth}
            \textbf{\textcolor{NutriDark}{B7. Xác thực \& Phân quyền (Auth)}}
            \begin{itemize}
                \footnotesize \setlength{\itemsep}{3pt}
                \item B7.1: Phân loại Route theo mức bảo vệ
                \item B7.2: ProtectedRoute hoạt động thế nào?
                \item B7.3: AuthOnlyRoute khác gì ProtectedRoute?
                \item B7.4: Axios interceptor xử lý token
                \item B7.5: Luồng xử lý khi Access Token hết hạn
                \item B7.6: Sử dụng useQuery đọc dữ liệu
                \item B7.7: Sử dụng useMutation ghi dữ liệu
                \item B7.8: Luồng đồng bộ dữ liệu tới Dashboard
                \item B7.9: Vai trò của Custom hook
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}
"""
lines = lines[:645] + [new_content + "\n"] + lines[670:]
with open("slide_baove.tex", "w", encoding="utf-8") as f:
    f.writelines(lines)
