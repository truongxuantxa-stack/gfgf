import sys

file_path = 'slide_baove.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the start of backup slides
start_idx = -1
for i, line in enumerate(lines):
    if line.strip() == '% --- BACKUP SLIDES ---':
        start_idx = i
        break

if start_idx == -1:
    print('Could not find backup slides section.')
    sys.exit(1)

new_content = r'''% --- BACKUP SLIDES ---
\appendix
\begin{frame}[plain]
    \begin{tikzpicture}[remember picture, overlay]
        \fill[NutriDark] (current page.south west) rectangle (current page.north east);
        \node[text=white, font=\LARGE\bfseries, align=center] at (current page.center) {BACKUP SLIDES\\[0.3cm]\large \normalfont\textcolor{NutriLightGray}{Phân tích Chuyên sâu Kỹ thuật \& Thuật toán}};
    \end{tikzpicture}
\end{frame}

% --- BACKUP B1 ---
\begin{frame}{BACKUP B1.1: Toán học đằng sau Meal Planner (Mô hình hóa)}
    \textbf{1. Mô hình hóa bài toán — Hệ phương trình tuyến tính $A\mathbf{x} = \mathbf{b}$}
    \vspace{0.2cm}
    
    Cho 3 nguyên liệu (Carb, Protein, Fat), mỗi nguyên liệu có hàm lượng macro per 100g. Cần tìm khối lượng $w_1, w_2, w_3$ (đơn vị: 100g) sao cho tổng macro đạt mục tiêu bữa ăn:

    $$ \begin{bmatrix} p_1 & p_2 & p_3 \\ c_1 & c_2 & c_3 \\ f_1 & f_2 & f_3 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} P_{target} \\ C_{target} \\ F_{target} \end{bmatrix} $$

    \begin{itemize}
        \small
        \item $p_i, c_i, f_i$: Hàm lượng Protein, Carbs, Fat (g/100g) của nguyên liệu $i$.
        \item $P_{target}, C_{target}, F_{target}$: Mục tiêu macro đã trừ phần rau (rau cố định 200g).
        \item \textbf{Nguồn code:} Hàm \texttt{solveLinearSystem3x3(A, b)} trong \texttt{mealPlanner.service.js}.
    \end{itemize}
\end{frame}

\begin{frame}[fragile]{BACKUP B1.2: Thuật toán Khử Gauss + Partial Pivoting}
    \textbf{2. Thuật toán: Khử Gauss + Partial Pivoting}
    
    \begin{block}{Các bước thực hiện}
        \footnotesize
        \textbf{Bước 1 — Forward Elimination:} For col = 0 $\rightarrow$ 2:\\
        \ \ ① \textbf{Partial Pivoting:} Tìm hàng có $|A[\text{row}][\text{col}]|$ lớn nhất $\rightarrow$ hoán vị lên.\\
        \ \ ② Nếu $|pivot| < 10^{-10} \rightarrow$ Ma trận suy biến $\rightarrow$ return null.\\
        \ \ ③ \textbf{Khử:} $A[\text{row}][\text{col}] \rightarrow 0$ cho mọi row $>$ col.\\
        \vspace{0.2cm}
        \textbf{Bước 2 — Back Substitution:}\\
        \ \ For i = 2 $\rightarrow$ 0:\\
        \ \ \ \ $x[i] = (b'[i] - \sum A'[i][j]\cdot x[j]) / A'[i][i]$
    \end{block}
    
    \begin{itemize}
        \small
        \item \textbf{Partial Pivoting} chọn phần tử trội nhất trong cột để tránh chia cho số rất nhỏ $\rightarrow$ giảm sai số số học floating-point.
        \item \textbf{Ngưỡng suy biến} ($|pivot| < 10^{-10}$): Xảy ra khi 2 nguyên liệu có tỷ lệ macro giống nhau (ví dụ: 2 loại gạo) $\rightarrow$ vô số nghiệm hoặc vô nghiệm.
    \end{itemize}
\end{frame}

\begin{frame}{BACKUP B1.3: Tại sao chọn Gauss? (So sánh phương pháp)}
    \textbf{3. So sánh các phương pháp}
    \vspace{0.2cm}
    
    \resizebox{\textwidth}{!}{
    \renewcommand{\arraystretch}{1.3}
    \begin{tabular}{llll}
        \toprule
        \textbf{Tiêu chí} & \textbf{Khử Gauss (Đang dùng)} & \textbf{Vét cạn (Brute-force)} & \textbf{Quy hoạch tuyến tính (LP)} \\
        \midrule
        \textbf{Độ phức tạp} & \textbf{$O(n^3)$, với $n=3 \rightarrow O(1)$ hằng số} & $O(k^n)$ ($k$ = số mức rời rạc) & $O(n^{2.5})$ $\rightarrow$ overhead cao \\
        \textbf{Nghiệm} & \textbf{Chính xác} (nghiệm thực) & Xấp xỉ (phụ thuộc bước nhảy) & Chính xác nhưng cần solver \\
        \textbf{Thư viện ngoài} & \textbf{Không} (self-contained) & Không & Cần \texttt{glpk} hoặc \texttt{lp\_solve} \\
        \textbf{Phát hiện suy biến} & \textbf{Có} (pivot check) & Không & Có \\
        \textbf{Phù hợp} & \textcolor{NutriGreen!80!black}{\textbf{Tối ưu cho $n=3$ cố định, real-time}} & \textcolor{red}{\textbf{Quá chậm}} & \textcolor{red}{\textbf{Overkill cho $n=3$}} \\
        \bottomrule
    \end{tabular}
    }
    
    \vspace{0.3cm}
    \textbf{Kết luận:} Với $n=3$ cố định, Gauss chạy trong thời gian hằng số $O(1)$, không cần thư viện ngoài, và cho nghiệm chính xác — lựa chọn tối ưu nhất.
\end{frame}

\begin{frame}{BACKUP B1.4: Xử lý ngoại lệ (Edge Cases)}
    \textbf{4. Xử lý ngoại lệ (Edge Cases)}
    \vspace{0.2cm}
    
    Sau khi giải ra $w_1, w_2, w_3$, hệ thống validate bằng \texttt{validateSolution()}:
    
    \begin{itemize}
        \small
        \item \textbf{Nghiệm âm} ($w_i < 0$): Xảy ra khi một nguyên liệu "đóng góp ngược" (ví dụ: thịt mỡ chứa quá nhiều fat làm lấn át phần fat riêng) $\rightarrow$ Đề xuất đổi sang nguồn protein nạc hơn.
        \item \textbf{Quá nhỏ} ($< 10$g, trừ dầu/fat): Lượng quá ít để chế biến, không mang tính thực tế.
        \item \textbf{Quá lớn} ($> 500$g, trừ rau): Khẩu phần ăn một bữa quá lớn, vượt mức tiêu hóa thông thường.
        \item \textbf{Cơ chế Retry:} Tối đa 15 lần với các tổ hợp thực phẩm thay thế, hệ thống sẽ lưu lại \texttt{bestAttempt} (phương án có tổng sai lệch calo nhỏ nhất) nếu không tìm được nghiệm hoàn hảo.
    \end{itemize}
\end{frame}

% --- BACKUP B2 ---
\begin{frame}{BACKUP B2.1: Thuật toán Chấm Điểm — Triage 3 Tầng}
    \textbf{1. Kiến trúc thuật toán — Triage 3 Tầng (Calorie-Gated)}
    \vspace{0.1cm}
    
    \textbf{Ý tưởng cốt lõi:} Không có ý nghĩa cảnh báo "thiếu Vitamin C" khi người dùng mới ăn 300 kcal (dưới 50\% mục tiêu). Cần ưu tiên cảnh báo theo tháp nhu cầu.
    
    \vspace{0.3cm}
    \begin{center}
    \begin{tikzpicture}[>=Stealth,
        box/.style={draw=NutriDark, fill=NutriLightGray, rounded corners, inner sep=6pt, text width=10cm, align=left}]
        
        \node[box] (t1) {\textbf{calPct $< 50\% \rightarrow$ Tầng 1: SINH TỒN}\\Chỉ cảnh báo thiếu Calo (Mute vi chất).};
        \node[box, below=0.3cm of t1] (t2) {\textbf{calPct $< 70\% \rightarrow$ Tầng 2: ĐA LƯỢNG}\\Xét Protein, Fat (Mute vi chất).};
        \node[box, below=0.3cm of t2] (t3) {\textbf{calPct $\ge 70\% \rightarrow$ Tầng 3: VI LƯỢNG}\\Xét đầy đủ 8 chỉ số (Xơ, Ca, Fe, VitC, VitA...).};
        
        \draw[->, thick] (t1) -- (t2);
        \draw[->, thick] (t2) -- (t3);
    \end{tikzpicture}
    \end{center}
    \vspace{0.1cm}
    \small \textit{Nguồn code: Hàm \texttt{getCalorieLevel(calPct)} và \texttt{getHealthInsights()} trong \texttt{suggestion.service.js}.}
\end{frame}

\begin{frame}[fragile]{BACKUP B2.2: Weighted Penalty — Hàm phạt biến thiên}
    \textbf{2. Weighted Penalty — Hàm phạt biến thiên tuyến tính}
    \vspace{0.1cm}
    
    Thay vì trừ điểm cố định (ví dụ: thiếu Protein luôn trừ 15 điểm), hệ thống \textbf{tính trọng số dựa trên mức độ sai lệch thực tế}:
    
    \begin{block}{\small Công thức \texttt{getWeightedPenalty()}}
        \footnotesize
        \texttt{deviation = isExcess ? (ratio - 1) : (1 - ratio)}\\
        \texttt{deviation $\le$ 0\%  $\rightarrow$ basePenalty $\times$ 0.5 (vi phạm nhẹ / đã giải quyết)}\\
        \texttt{deviation $>$ 20\% $\rightarrow$ basePenalty $\times$ 1.0 (sai lệch vừa)}\\
        \texttt{deviation $>$ 40\% $\rightarrow$ basePenalty $\times$ 1.8 (sai lệch lớn)}\\
        \texttt{deviation $>$ 60\% $\rightarrow$ basePenalty $\times$ 2.5 (sai lệch nghiêm trọng)}
    \end{block}
    
    \textbf{Ví dụ thực tế:}
    \begin{itemize}
        \item Protein thiếu 25\% $\rightarrow$ penalty là $15 \times 1.0 = 15$ điểm.
        \item Protein thiếu 60\% $\rightarrow$ penalty là $15 \times 2.5 = 37.5$ điểm.
    \end{itemize}
    \textit{$\rightarrow$ Phản ánh chính xác mức độ nghiêm trọng của sự thiếu hụt/dư thừa.}
\end{frame}

\begin{frame}[fragile]{BACKUP B2.3: Context-Awareness}
    \textbf{3. Context-Awareness — Nhận biết ngữ cảnh thời gian thực}
    \vspace{0.1cm}
    
    \begin{block}{\small Cổng logic kiểm tra (Gate)}
        \footnotesize
        \texttt{const isDayComplete = isHistorical || currentHour >= 20 ||}\\
        \texttt{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (hasSang \&\& hasTrua \&\& hasToi);}\\
        \texttt{const shouldWarnDeficiency = isDayComplete \&\& consumed.calories > 0;}
    \end{block}
    
    \begin{itemize}
        \small
        \item \textbf{Cảnh báo DƯ THỪA} (muối, đường, calo vượt): Kích hoạt \textbf{MỌI LÚC}. (Ví dụ: Ăn mặn lúc sáng vẫn cần phải biết ngay).
        \item \textbf{Cảnh báo THIẾU HỤT}: Chỉ kích hoạt khi \texttt{isDayComplete = true}. (Tránh false positive khi người dùng mới chỉ ăn sáng xong).
        \item \textbf{\texttt{clientHour}}: Được truyền từ Frontend để hệ thống Backend xử lý đúng ngữ cảnh thời gian, tránh sai lệch múi giờ (Ví dụ: Server ở múi giờ UTC 13:30, nhưng người dùng ở VN đang là 20:30).
    \end{itemize}
\end{frame}

\begin{frame}{BACKUP B2.4: Sliding Multiplier \& Hard Cap}
    \textbf{4. Sliding Calorie Multiplier (Nhân toàn bộ điểm)}
    
    \begin{columns}[T]
        \begin{column}{0.5\textwidth}
            \resizebox{\textwidth}{!}{
            \renewcommand{\arraystretch}{1.2}
            \begin{tabular}{lll}
                \toprule
                \textbf{Calo đạt (\%)} & \textbf{Multiplier} & \textbf{Ý nghĩa} \\
                \midrule
                $< 30\%$ & \textbf{$\times 0.3$} & Ngày nhịn ăn $\rightarrow$ điểm thấp \\
                $< 50\%$ & \textbf{$\times 0.5$} & Ăn quá ít \\
                $< 70\%$ & \textbf{$\times 0.7$} & Dưới mức tối ưu \\
                $70 - 110\%$ & \textbf{$\times 1.0$} & Lý tưởng \\
                $> 110\%$ & \textbf{$\times 0.85$} & Vượt nhẹ \\
                $> 130\%$ & \textbf{$\times 0.6$} & Ăn quá nhiều (Binge) \\
                \bottomrule
            \end{tabular}
            }
        \end{column}
        
        \begin{column}{0.48\textwidth}
            \textbf{Sugar Toxicity Multiplier:}
            \begin{itemize}
                \small
                \item Đường $> 200\%$ mức khuyến cáo của AHA $\rightarrow \times 0.7$ (nhân thêm).
            \end{itemize}
            
            \vspace{0.2cm}
            \textbf{Hard Cap (Trần cứng):}
            \begin{itemize}
                \small
                \item \texttt{avgMicroRatio < 0.20}: Trần 50 điểm (Vi chất quá kém).
                \item \texttt{fiberRatio < 0.30}: Trần 60 điểm (Thiếu xơ nghiêm trọng).
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}{BACKUP B2.5: Điểm thưởng \& Độ phức tạp}
    \textbf{5. Điểm thưởng (Bonus Rules)}
    \begin{itemize}
        \item Calo đạt 90–110\% mục tiêu: \textbf{+5 điểm}.
        \item Đạt mục tiêu Protein: \textbf{+3 điểm}.
        \item Uống đủ nước mục tiêu: \textbf{+5 điểm}.
        \item Đạt mục tiêu Chất xơ: \textbf{+2 điểm}.
    \end{itemize}
    
    \vspace{0.3cm}
    \textbf{6. Độ phức tạp tính toán (Complexity)}
    \begin{itemize}
        \item \textbf{Health Insights:} $O(N)$ — duyệt qua $N=8$ chỉ số dinh dưỡng cố định $\rightarrow O(1)$.
        \item \textbf{Daily Health Score:} $O(I)$ — duyệt mảng insights (tối đa $\approx 15$) $\rightarrow O(1)$.
        \item \textbf{Food Scoring:} $O(1)$ per food item — tính mật độ dinh dưỡng và 8 tiêu chí.
        \item \textbf{Weekly Food Report:} $O(M)$ — $M$ là số entry trong tuần (chấm điểm từng món).
    \end{itemize}
\end{frame}

% --- BACKUP B3 ---
\begin{frame}{BACKUP B3.1: EMA \& Bộ Lọc Thông Thấp (Bài toán)}
    \textbf{1. Bài toán: Tách Tín hiệu khỏi Nhiễu}
    \vspace{0.1cm}
    
    Cân nặng hàng ngày bao gồm \textbf{Tín hiệu (Signal)} và \textbf{Nhiễu (Noise)}:
    \begin{itemize}
        \item \textbf{Signal:} Xu hướng thay đổi mỡ thực sự của cơ thể (thay đổi rất chậm, khoảng $0.1 - 0.2$ kg/tuần).
        \item \textbf{Noise:} Dao động nước trong cơ thể, lượng thức ăn chưa tiêu hóa ($\pm 0.5 - 1.5$ kg/ngày).
    \end{itemize}
    
    \textbf{Mục tiêu:} Loại bỏ nhiễu, giữ lại tín hiệu cốt lõi $\rightarrow$ tính $\Delta\text{Weight}$ chính xác $\rightarrow$ ước tính TDEE thực tế.
    
    \vspace{0.3cm}
    \textbf{2. EMA = Bộ lọc thông thấp bậc 1 (First-order IIR Low-pass Filter)}
    
    $$ EMA_t = \alpha \cdot W_t + (1 - \alpha) \cdot EMA_{t-1} $$
    
    \textbf{Diễn giải tần số:}
    \begin{itemize}
        \item Tín hiệu tần số \textbf{thấp} (xu hướng dài hạn) $\rightarrow$ \textbf{Đi qua (pass)}.
        \item Tín hiệu tần số \textbf{cao} (nhiễu theo ngày) $\rightarrow$ \textbf{Bị suy giảm (attenuated)}.
    \end{itemize}
\end{frame}

\begin{frame}{BACKUP B3.2: Tần số cắt \& Trọng số $\alpha$}
    \textbf{3. Tần số cắt (Cutoff frequency)}
    \vspace{0.1cm}
    
    Công thức tần số cắt:
    $$ f_c = \frac{\alpha}{2\pi \cdot \Delta t \cdot (1 - \alpha)} $$
    
    Với $\alpha = 0.1$, khoảng thời gian $\Delta t = 1$ ngày:
    $$ f_c \approx \frac{0.1}{2\pi \times 0.9} \approx 0.0177 \text{ chu kỳ/ngày} \approx \frac{1}{56} \text{ chu kỳ/ngày} $$
    $\rightarrow$ Hệ thống chỉ giữ lại các biến đổi có chu kỳ $> 56$ ngày (xu hướng thực sự), lọc hết mọi dao động ngắn hạn.
    
    \vspace{0.3cm}
    \textbf{4. Tại sao chọn $\alpha = 0.1$?}
    
    \begin{itemize}
        \item $\alpha = 0.3$: Phản ứng nhanh nhưng \textbf{Nhiễu lọt qua} nhiều $\rightarrow$ TDEE nhảy loạn.
        \item \textbf{$\alpha = 0.1$: Cân bằng hoàn hảo} $\rightarrow$ Lọc tốt nước dư, nhưng vẫn nhạy vừa đủ.
        \item $\alpha = 0.05$: Quá mượt $\rightarrow$ Phản ứng cực chậm, trễ tín hiệu 3-4 tuần.
    \end{itemize}
\end{frame}

\begin{frame}{BACKUP B3.3: Warm-up 14 ngày \& Anti-Smoothing Kép}
    \textbf{5. Warm-up 14 ngày — Tại sao cần?}
    \begin{itemize}
        \small
        \item \textbf{Vấn đề:} Nếu khởi tạo EMA bằng cân nặng đầu tiên (VD: 80.0kg, cân lúc vừa uống 2L nước) $\rightarrow$ tất cả giá trị EMA sau đó đều bị thiên lệch (bias).
        \item \textbf{Giải pháp:} EMA cần "hội tụ". Hệ thống truy xuất dữ liệu cân của \textbf{14 ngày trước} tuần hiện tại, tính EMA liên tục. Giá trị \texttt{startWeight} chỉ được lấy khi EMA đã "chạy ấm" tới ngày đầu tuần.
    \end{itemize}
    
    \vspace{0.3cm}
    \textbf{6. Anti-Smoothing Kép (Chống làm mượt 2 lần)}
    \begin{itemize}
        \small
        \item \textbf{Vấn đề:} \texttt{rollingTDEE} là trung bình trượt 4 tuần. Nếu dùng \texttt{log.rollingTDEE} (đã là trung bình) để tính rolling cho tuần mới $\rightarrow$ gây ra \textbf{smoothing kép} (average of averages) $\rightarrow$ thuật toán mất độ nhạy.
        \item \textbf{Giải pháp:} Luôn dùng \texttt{log.calculatedTDEE} (giá trị tuần thô, chưa smooth) khi tính tổng rolling.
    \end{itemize}
\end{frame}

\begin{frame}[fragile]{BACKUP B3.4: Guardrails \& Phát hiện Plateau \& Cron Job}
    \textbf{7. Guardrails — Cơ chế an toàn}
    \begin{itemize}
        \scriptsize
        \item \textbf{TDEE clamp:} Giới hạn $TDEE_{tĩnh} \pm 30\%$ để ngăn outlier từ dữ liệu sai.
        \item \textbf{Minimum data:} Yêu cầu $\ge 5$ ngày nhật ký + $\ge 2$ lần cân để đảm bảo ý nghĩa thống kê.
        \item \textbf{Min valid weeks:} Cần đủ $\ge 2$ tuần hợp lệ mới cập nhật Adaptive TDEE cho User.
        \item \textbf{Confidence:} 7 ngày (High), 6 ngày (Medium), 5 ngày (Low) $\rightarrow$ Minh bạch độ tin cậy.
    \end{itemize}
    
    \vspace{0.1cm}
    \textbf{8. Phát hiện Plateau (Chững cân)}
    \begin{block}{\scriptsize Logic phát hiện}
        \scriptsize
        \texttt{if (adaptiveTDEE < staticTDEE * 0.88) \{} \\
        \texttt{\ \ isPlateauing = true;}\\
        \texttt{\ \ Đề xuất giảm targetCalories;}\\
        \texttt{\ \ Thông báo: "Cơ thể đang thích ứng chuyển hóa";}\\
        \texttt{\}}
    \end{block}
    
    \vspace{0.1cm}
    \textbf{9. Cron Job tự động:} Chạy mỗi Thứ Hai lúc 3:00 sáng. Duyệt $U$ user, độ phức tạp $O(U \cdot D)$ (với $D$ số entry/tuần).
\end{frame}

% --- BACKUP B4 ---
\begin{frame}{BACKUP B4.1: Sơ đồ CSDL — 9 Bảng Chính}
    \textbf{Các bảng dữ liệu chính trong hệ thống}
    \vspace{0.2cm}
    
    \resizebox{\textwidth}{!}{
    \renewcommand{\arraystretch}{1.3}
    \begin{tabular}{lll}
        \toprule
        \textbf{Bảng} & \textbf{Vai trò chính} & \textbf{Trường đặc biệt \& Ghi chú} \\
        \midrule
        \textbf{Users} & Tài khoản \& hồ sơ & \texttt{adaptiveTDEE}, \texttt{isOnboarded}, \texttt{goal} \\
        \textbf{Foods} & Danh mục thực phẩm & \texttt{dataSource}, \texttt{deletedAt} (Soft delete) \\
        \textbf{DiaryEntries} & Nhật ký ăn uống & \texttt{caloriesSnapshot} (Bảo toàn lịch sử quá khứ) \\
        \textbf{WeightLogs} & Lịch sử cân nặng & \texttt{note} (Ghi chú bối cảnh: sáng/tối) \\
        \textbf{WaterLogs} & Lịch sử uống nước & \texttt{amount} (ml) \\
        \textbf{ExerciseLogs} & Lịch sử vận động & \texttt{caloriesBurned} (kcal) \\
        \textbf{MealPlans} & Kế hoạch bữa ăn & \texttt{items} (JSON kết quả thuật toán Khử Gauss) \\
        \textbf{AdaptiveTDEELog} & Lịch sử TDEE & \texttt{calculatedTDEE}, \texttt{rollingTDEE}, \texttt{confidence} \\
        \textbf{UserGoals} & Mục tiêu dinh dưỡng & \texttt{targetCalories}, \texttt{macros}, \texttt{waterGoal} \\
        \bottomrule
    \end{tabular}
    }
\end{frame}

\begin{frame}{BACKUP B4.2: Quan hệ \& Điểm thiết kế nổi bật}
    \textbf{Quan hệ giữa các bảng:}
    \begin{itemize}
        \item \textbf{Users (1) $\rightarrow$ (N):} DiaryEntries, WeightLogs, WaterLogs, ExerciseLogs, MealPlans, AdaptiveTDEELog.
        \item \textbf{DiaryEntries (N) $\rightarrow$ (1):} Foods (thông qua khóa ngoại \texttt{foodId}).
        \item \textbf{Foods:} Nếu \texttt{userId} là \texttt{NULL} thì đó là thực phẩm của hệ thống (OpenFoodFacts/Admin). Nếu có \texttt{userId} thì là thực phẩm cá nhân.
    \end{itemize}
    
    \vspace{0.3cm}
    \textbf{Điểm thiết kế kiến trúc nổi bật:}
    \begin{itemize}
        \item \textbf{Snapshot Pattern (Hình ảnh chụp):} \texttt{DiaryEntries} sao chép lưu trực tiếp \texttt{caloriesSnapshot, proteinSnapshot...} tại thời điểm ghi nhận. Nếu tương lai Admin sửa thực phẩm trong \texttt{Foods}, dữ liệu quá khứ của người dùng không bị ảnh hưởng.
        \item \textbf{Soft Delete (Paranoid Mode):} Sequelize set \texttt{deletedAt} khi xóa, không xóa dữ liệu vật lý. Tránh vi phạm khóa ngoại và vẫn giữ được khả năng truy xuất báo cáo cũ.
    \end{itemize}
\end{frame}

% --- BACKUP B5 ---
\begin{frame}{BACKUP B5.1: Food Scoring — Mật độ Dinh dưỡng}
    \textbf{1. Nguyên lý Mật độ Dinh dưỡng (Nutrient Density per 100 kcal)}
    \begin{itemize}
        \small
        \item Tại sao dùng per 100 kcal mà không dùng per 100g? So sánh 100g rau (25 kcal) với 100g bánh ngọt (400 kcal) theo khối lượng là thiếu công bằng.
        \item Chuẩn hóa trên 100 kcal để so sánh: \textit{"Với cùng một lượng năng lượng nạp vào, món nào cung cấp nhiều vi/đa lượng hơn?"}
    \end{itemize}
    
    $$ density_i = value_i \times \frac{100}{calories} $$
    
    \vspace{0.2cm}
    \textbf{2. Cấu trúc chấm điểm — 3 Lớp}
    \begin{itemize}
        \small
        \item \textbf{Lớp 0 (Cơ sở):} Khởi điểm 50 điểm (Thang 0-100).
        \item \textbf{Lớp 1 (Đa lượng):} Cộng/trừ $\pm 25$ điểm. (+25 cho Protein $\ge 5$g, Xơ $\ge 1.25$g; -25 cho Muối $>150$mg, Đường $>5$g).
        \item \textbf{Lớp 2 (Vi lượng):} Thưởng tối đa +10 điểm cho mỗi vi chất (Vit A, Vit C, Canxi, Sắt) nếu đạt ngưỡng.
        \item \textbf{Lớp 3 (Hard Caps):} Trần cứng không thể vượt qua, đánh đè lên mọi điểm cộng.
    \end{itemize}
\end{frame}

\begin{frame}{BACKUP B5.2: Double Medical Protection (Bảo vệ y khoa kép)}
    \textbf{3. Hard Cap — Bảo vệ Y khoa Kép}
    \vspace{0.1cm}
    
    \begin{itemize}
        \small
        \item \textbf{Vấn đề:} Một món ăn có thể giàu Protein (+25) và giàu Xơ (+25) nhưng \textbf{cực kỳ mặn} (Sodium $> 300$mg/100kcal hoặc $> 1000$mg tuyệt đối). Nếu chỉ cộng trừ tuyến tính, điểm cuối cùng vẫn cao $\rightarrow$ sai lầm nguy hiểm.
        \item \textbf{Giải pháp:} Mọi điểm cộng đều vô nghĩa khi vi phạm ngưỡng y khoa an toàn.
    \end{itemize}
    
    \resizebox{\textwidth}{!}{
    \renewcommand{\arraystretch}{1.3}
    \begin{tabular}{lll}
        \toprule
        \textbf{Hard Cap} & \textbf{Ngưỡng kích hoạt} & \textbf{Hiệu ứng} \\
        \midrule
        \textcolor{red}{\textbf{Trần 40}} & \textbf{Sodium density $> 300$mg \textit{HOẶC} tuyệt đối $> 1000$mg} & \textbf{Điểm bị kéo xuống $\le 40$ bất chấp macro} \\
        \textbf{Trần 50} & $\ge 3/4$ vi chất có ratio $< 0.10$ & "Calo rỗng", không miễn trừ thịt/protein \\
        \textbf{Trần 60} & Sodium danger ($> 150$mg/100kcal) & Hơi mặn \\
        \textbf{Trần 60} & Fiber ratio $< 0.30$ (thiếu xơ) & Không áp dụng cho nhóm thịt/protein \\
        \bottomrule
    \end{tabular}
    }
\end{frame}

\begin{frame}{BACKUP B5.3: Pipeline Khai Thác Thói Quen (Habit Extraction)}
    \textbf{4. Thuật toán Habit Extraction (Xử lý $M$ entries trong 30 ngày)}
    
    \vspace{0.2cm}
    \begin{center}
    \begin{tikzpicture}[>=Stealth,
        box/.style={draw=NutriDark, fill=NutriLightGray, rounded corners, inner sep=4pt, text width=11.5cm}]
        
        \node[box] (b1) {\textbf{Bước 1: Aggregation} — Duyệt $M$ entries, gộp theo \texttt{foodId} thành $N$ món (HashMap) $O(M)$.};
        \node[box, below=0.2cm of b1] (b2) {\textbf{Bước 2: Scoring} — Gọi \texttt{scoreFoodItem()} để lấy \texttt{qualityScore} cho $N$ món $O(N)$.};
        \node[box, below=0.2cm of b2] (b3) {\textbf{Bước 3: Filtering} — Lọc các món có \texttt{count} $\ge 4$ lần/tháng (đủ tần suất thành "thói quen") $O(N)$.};
        \node[box, below=0.2cm of b3] (b4) {\textbf{Bước 4: Branching} — Chia nhánh:\\$\ge 70$: \textbf{TỐT} \hspace{1cm} $60-69$: \textbf{NEUTRAL (Im lặng)} \hspace{1cm} $< 60$: \textbf{XẤU} $O(N)$.};
        \node[box, below=0.2cm of b4] (b5) {\textbf{Bước 5: Multi-Criteria Sort} — Nhóm TỐT sort điểm DESC, nhóm XẤU sort điểm ASC. $O(N \log N)$.};
        \node[box, below=0.2cm of b5] (b6) {\textbf{Bước 6: Top-K Selection} — Chỉ lấy Top 5 cho mỗi nhóm để giảm cognitive load cho User.};
        
        \draw[->, thick] (b1) -- (b2);
        \draw[->, thick] (b2) -- (b3);
        \draw[->, thick] (b3) -- (b4);
        \draw[->, thick] (b4) -- (b5);
        \draw[->, thick] (b5) -- (b6);
    \end{tikzpicture}
    \end{center}
\end{frame}

\begin{frame}{BACKUP B5.4: Vùng Neutral, Weekly Verdict \& Độ phức tạp}
    \textbf{5. Vùng Neutral (60–69 điểm) — Thiết kế có chủ đích}
    \begin{itemize}
        \item Món ăn đạt $60-69$ điểm (VD: Cơm Gà Hải Nam 65đ) "không xuất sắc nhưng không vi phạm".
        \item Nếu khen thì không xứng, chê thì oan. Cố ý đưa vào vùng \textbf{Im lặng (Neutral)} để giảm noise cho User, giúp tập trung vào các thói quen cực kỳ Tốt hoặc cực kỳ Xấu.
    \end{itemize}
    
    \vspace{0.2cm}
    \textbf{6. Thống kê tổng hợp (Weekly Verdict)}
    \begin{itemize}
        \item \texttt{avgQualityScore}: Điểm chất lượng trung bình \textbf{có trọng số} (món ăn nhiều $\rightarrow$ ảnh hưởng nhiều).
        \item \texttt{redFlagPercentage}: Tỷ lệ \% bữa ăn sử dụng thực phẩm kém.
        \item \textbf{Verdict:} Xuất sắc (redFlag $\le 15\%$ \& avg $\ge 75$), Khá ($\le 30\%$ \& $\ge 65$), Cần lưu ý ($\le 50\%$ \& $\ge 50$), và Tệ.
    \end{itemize}
    
    \vspace{0.2cm}
    \textbf{7. Độ phức tạp tổng thể}
    \begin{itemize}
        \item Toàn bộ pipeline tính toán mất $O(M + N \log N)$. Chạy hoàn tất $< 2$ms với $M \approx 300, N \approx 50$.
    \end{itemize}
\end{frame}

\end{document}
'''

lines = lines[:start_idx]
lines.append(new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Updated backup slides successfully.')
