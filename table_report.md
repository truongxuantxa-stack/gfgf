## Line 511: Các yêu cầu chính của hệ thống
- **Label**: tab:yeu_cau_he_thong
- **Status**: NEEDS_FIX
- **Context**: Bên cạnh chức năng lưu trữ, hệ thống cần có khả năng tổng hợp và phân tích dữ liệu để hỗ trợ người dùng theo dõi quá trình thực hiện mục tiêu dinh dưỡng. Các kết quả phân tích cần được trình bày dưới dạng trực quan thông qua các chỉ số tổng hợp, biểu đồ và báo cáo.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 564: Tổng hợp yêu cầu chức năng của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Nhóm chức năng thứ sáu là xây dựng thực đơn và xuất báo cáo. Meal Planner cần hỗ trợ tạo gợi ý thực đơn dựa trên mục tiêu dinh dưỡng và dữ liệu thực phẩm. Chức năng báo cáo PDF cần tổng hợp dữ liệu theo khoảng thời gian, giúp người dùng xem lại kết quả theo tuần hoặc tháng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 607: Tổng hợp yêu cầu phi chức năng của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Về khả năng bảo trì và mở rộng, hệ thống cần được tổ chức theo kiến trúc phân lớp. Backend cần tách biệt các thành phần định tuyến, kiểm tra xác thực, xử lý yêu cầu, xử lý nghiệp vụ và truy cập cơ sở dữ liệu. Frontend cần được chia thành các trang, component và hook để thuận lợi cho việc tái sử dụng và mở rộng. Cách tổ chức này giúp giảm phụ thuộc giữa các phần của hệ thống và hỗ trợ quá trình phát triển các chức năng mới.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 774: Danh sách công nghệ sử dụng trong hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Ngoài ra, hệ thống còn sử dụng các thư viện hỗ trợ xây dựng biểu đồ thống kê, xuất báo cáo PDF, gửi thư điện tử và xử lý tập tin theo yêu cầu của từng chức năng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1123: Tổng hợp yêu cầu chức năng của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Bên cạnh các chức năng ghi nhận dữ liệu, hệ thống cần thực hiện các xử lý tính toán và phân tích như Nutrition Core, Adaptive TDEE, Food Scoring, Health Insights và Meal Planner. Các kết quả xử lý được sử dụng để hiển thị trên Dashboard, hỗ trợ xây dựng thực đơn và xuất báo cáo PDF theo khoảng thời gian.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1168: Tổng hợp yêu cầu phi chức năng của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Về khả năng mở rộng và bảo trì, hệ thống cần được tổ chức theo kiến trúc phân lớp, tách biệt Frontend, Backend và cơ sở dữ liệu. Backend cần phân tách Router, Middleware, Controller, Service và Model. Frontend cần tổ chức theo trang, component và custom hook để thuận lợi cho việc tái sử dụng và mở rộng chức năng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1211: Tổng hợp các luồng nghiệp vụ chính của hệ thống
- **Label**: tab:nghiep_vu_chinh
- **Status**: NEEDS_FIX
- **Context**: Dữ liệu hồ sơ được Backend kiểm tra và lưu vào cơ sở dữ liệu. Từ các thông tin này, hệ thống tính toán các chỉ số nền tảng như BMI, BMR, TDEE, mục tiêu năng lượng, tỷ lệ chất đa lượng và mục tiêu nước. BMR được sử dụng để ước lượng mức năng lượng cơ thể tiêu hao trong trạng thái nghỉ, làm cơ sở cho việc tính toán TDEE và mục tiêu năng lượng cá nhân \cite{mifflin1990}. Sau khi hoàn tất Onboarding, người dùng được chuyển tới các màn hình chức năng chính như Dashboard, nhật ký ăn uống, Meal Planner, cân nặng, luyện tập và hồ sơ cá nhân.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1275: Tác nhân và hệ thống liên quan
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Ngoài tác nhân người dùng, một số chức năng của hệ thống có sử dụng các hệ thống bên ngoài như Open Food Facts API và Gemini AI Vision. Các hệ thống này không phải là tác nhân nghiệp vụ chính vì người dùng không tương tác trực tiếp với chúng. Chúng được Backend gọi trong quá trình xử lý nghiệp vụ nhằm hỗ trợ tra cứu và nhận dạng dữ liệu thực phẩm.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1391: Danh sách Use Case chính
- **Label**: tab:danh_sach_usecase
- **Status**: NEEDS_FIX
- **Context**: Hình \ref{fig:usecase_tong_the} trình bày biểu đồ Use Case tổng thể của hệ thống. Tác nhân chính của hệ thống là Người dùng, thực hiện các nhóm chức năng gồm đăng ký, đăng nhập, quản lý hồ sơ sức khỏe, ghi nhận nhật ký ăn uống, ghi nhận nước uống, theo dõi cân nặng, ghi nhận luyện tập, sử dụng Hybrid Nutrition Scanner, xem Dashboard, xây dựng thực đơn và xuất báo cáo PDF. Hai hệ thống bên ngoài gồm Open Food Facts API và Gemini AI Vision được liên kết với nhóm Use Case Hybrid Nutrition Scanner để hỗ trợ tra cứu sản phẩm theo mã vạch và nhận dạng bảng thành phần dinh dưỡng từ hình ảnh.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1447: Đặc tả rút gọn Use Case đăng nhập
- **Label**: tab:uc_dang_nhap
- **Status**: NEEDS_FIX
- **Context**: Một điểm quan trọng trong Use Case này là hệ thống cần lưu lại giá trị dinh dưỡng tại thời điểm ghi nhật ký. Cách xử lý này giúp dữ liệu lịch sử không bị thay đổi khi thông tin thực phẩm gốc được chỉnh sửa sau đó (Chi tiết xem Bảng \ref{tab:uc_ghi_nhat_ky}).
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1481: Đặc tả rút gọn Use Case ghi nhật ký ăn uống
- **Label**: tab:uc_ghi_nhat_ky
- **Status**: NEEDS_FIX
- **Context**: Với luồng nhận dạng bảng thành phần dinh dưỡng, người dùng gửi ảnh bảng thông tin sản phẩm. Hệ thống sử dụng Gemini AI Vision để trích xuất dữ liệu dinh dưỡng, sau đó kiểm tra và chuẩn hóa kết quả trước khi sử dụng (Chi tiết xem Bảng \ref{tab:uc_scanner}).
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1515: Đặc tả rút gọn Use Case sử dụng Hybrid Nutrition Scanner
- **Label**: tab:uc_scanner
- **Status**: NEEDS_FIX
- **Context**: Các quan hệ này cần được thể hiện trong biểu đồ Use Case tổng thể và tiếp tục được làm rõ trong phần thiết kế cơ sở dữ liệu, thiết kế API và thiết kế giao diện.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1652: Phân nhóm bảng dữ liệu của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Báo cáo PDF không được thiết kế thành một nhóm bảng riêng. Dữ liệu báo cáo được tổng hợp trực tiếp từ hồ sơ người dùng, nhật ký ăn uống, nước uống, cân nặng, luyện tập và các dữ liệu phân tích tại thời điểm xuất báo cáo.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1687: Tóm tắt khóa chính và khóa ngoại của một số bảng chính
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Đối với Scanner, một sản phẩm trong ScannedProduct có thể có nhiều bản ghi đóng góp trong ProductContribution. Mỗi đóng góp liên kết với một người dùng và một sản phẩm được quét. Nếu sản phẩm đã được chuẩn hóa thành dữ liệu thực phẩm sử dụng chung, ScannedProduct có thể liên kết tùy chọn với Food.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 1882: Cấu trúc phản hồi API
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Cách thiết kế phản hồi thống nhất giúp giảm sự phức tạp trong xử lý lỗi ở Frontend. Các thành phần giao diện có thể dựa vào trường success, data, message và errors để xác định trạng thái xử lý.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 2152: Các nhóm API chính của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Cách thiết kế này giúp bảo vệ các API nghiệp vụ, đồng thời giảm việc yêu cầu người dùng đăng nhập lại trong quá trình sử dụng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 2189: Một số endpoint tiêu biểu của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Auth & /api/v1/auth & Đăng ký, đăng nhập, đăng xuất, làm mới Token, lấy thông tin người dùng hiện tại \\ Dashboard & /api/v1/dashboard & Lấy dữ liệu tổng hợp phục vụ Dashboard \\ Diary & /api/v1/diary & Quản lý nhật ký ăn uống và thực phẩm tùy chỉnh \\ Profile & /api/v1/profile & Quản lý hồ sơ sức khỏe, macro, dị ứng và onboarding \\ Weight & /api/v1/weight & Quản lý dữ liệu cân nặng \\ Water & /api/v1/water & Quản lý dữ liệu nước uống \\ Exercise & /api/v1/exercise & Quản lý dữ liệu luyện tập \\ Meal Planner & /api/v1/meal-planner & Cấu hình bữa ăn, lấy nguyên liệu, sinh thực đơn và thay thế nguyên liệu \\ Adaptive TDEE & /api/v1/adaptive-tdee & Quản lý trạng thái và lịch sử tính toán Adaptive TDEE \\ Scanner & /api/v1/scanner & Quét mã vạch, nhận dạng bảng thành phần và lưu dữ liệu sản phẩm \\ Report & /api/v1/report & Xuất báo cáo PDF \\
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 2241: Một số mã trạng thái API
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Auth & POST & /api/v1/auth/register & Đăng ký tài khoản mới \\ Auth & POST & /api/v1/auth/login & Đăng nhập và nhận Access Token \\ Auth & POST & /api/v1/auth/refresh-token & Làm mới Access Token \\ Dashboard & GET & /api/v1/dashboard?date=YYYY-MM-DD & Lấy dữ liệu tổng hợp cho Dashboard theo ngày \\ Diary & GET & /api/v1/diary & Lấy nhật ký ăn uống theo ngày \\ Diary & POST & /api/v1/diary/entries & Thêm thực phẩm vào nhật ký \\ Diary & GET & /api/v1/diary/foods/search & Tìm kiếm thực phẩm \\ Profile & POST & /api/v1/profile/onboarding & Lưu thông tin khởi tạo hồ sơ \\ Profile & PUT & /api/v1/profile/macros & Cập nhật cấu hình macro \\ Weight & POST & /api/v1/weight & Thêm bản ghi cân nặng \\ Water & POST & /api/v1/water & Ghi nhận lượng nước uống \\ Exercise & POST & /api/v1/exercise & Thêm hoạt động luyện tập \\ Meal Planner & POST & /api/v1/meal-planner/generate & Sinh gợi ý thực đơn \\ Adaptive TDEE & GET & /api/v1/adaptive-tdee/status & Lấy trạng thái Adaptive TDEE \\ Scanner & POST & /api/v1/scanner/barcode-lookup & Tra cứu sản phẩm theo mã vạch \\ Scanner & POST & /api/v1/scanner/ai-vision & Nhận dạng bảng thành phần dinh dưỡng từ ảnh \\ Scanner & POST & /api/v1/scanner/confirm-contribution & Xác nhận và lưu dữ liệu sản phẩm đóng góp \\ Report & GET & /api/v1/report/pdf?range=week & Xuất báo cáo PDF theo tuần \\
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 2669: Tổng hợp một số màn hình chức năng của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: \end{tikzpicture} }% end scalebox \caption{Wireframe giao diện chức năng Meal Planner} \label{fig:meal_planner_ui} \end{figure}
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 2814: Một số nhóm API chính của Backend
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Các phương thức HTTP được sử dụng theo ý nghĩa của từng thao tác. Thao tác đọc dữ liệu sử dụng GET, thao tác tạo dữ liệu sử dụng POST, thao tác cập nhật sử dụng PUT hoặc PATCH, còn thao tác xóa sử dụng DELETE. Cách tổ chức này giúp API dễ kiểm tra, dễ tích hợp với Frontend và giữ được sự thống nhất khi hệ thống mở rộng thêm chức năng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3031: Vai trò của một số thành phần chính trong Frontend
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Sau các thao tác làm thay đổi dữ liệu, Frontend gọi invalidateQueries để cập nhật lại các dữ liệu liên quan. Ví dụ, khi thêm món ăn vào nhật ký, dữ liệu nhật ký và dashboard của ngày hiện tại cần được làm mới. Khi thêm vận động, dữ liệu exercise và dashboard cũng cần được cập nhật. Cách xử lý này giúp dữ liệu giữa các màn hình giữ được sự nhất quán, tránh trường hợp một màn hình đã thay đổi nhưng màn hình khác vẫn hiển thị dữ liệu cũ.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3127: Dữ liệu đầu vào và kết quả xử lý của Nutrition Core
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Trong nhóm dữ liệu đầu vào, mức độ vận động được sử dụng để lựa chọn hệ số hoạt động thể chất khi tính TDEE. Việc đưa trường này vào hồ sơ người dùng giúp hệ thống ánh xạ dữ liệu khai báo của người dùng sang hệ số PAL phục vụ tính toán nhu cầu năng lượng hằng ngày \cite{fao_who_unu_2001}.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3222: Dữ liệu đầu vào của Adaptive TDEE
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Khoảng thời gian tính toán được tổ chức theo tuần, bắt đầu từ thứ Hai và kết thúc sau bảy ngày. Việc chọn chu kỳ tuần giúp giảm ảnh hưởng của dao động ngắn hạn trong một ngày, chẳng hạn thay đổi nước, muối hoặc thời điểm cân. Đồng thời, chu kỳ tuần đủ ngắn để hệ thống phản hồi với thay đổi của người dùng, nhưng không quá ngắn đến mức kết quả bị chi phối bởi một vài bản ghi đơn lẻ.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3249: Các trạng thái chính của log Adaptive TDEE
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: \enlargethispage{4\baselineskip}
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3387: trình bày các nhóm dữ liệu chính được sử dụng trong Food Scoring.
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Cách chuẩn hóa này giúp so sánh các thực phẩm có mức năng lượng khác nhau trên cùng một cơ sở. Ví dụ, một thực phẩm có tổng protein cao nhưng năng lượng rất lớn chưa chắc có mật độ protein tốt hơn một thực phẩm có ít protein hơn nhưng năng lượng thấp hơn. Vì vậy, thuật toán không đánh giá thực phẩm theo tổng lượng tuyệt đối, mà dựa trên lượng dinh dưỡng thu được trong 100 kcal.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3480: trình bày các nhóm dữ liệu đầu vào chính của Health Insights.
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Trong mã nguồn, hàm getHealthInsights nhận các nhóm dữ liệu chính như consumed, metrics, mealGroups, waterTotal, waterGoal, gender, isHistorical và clientHour. Trong đó, consumed chứa dữ liệu dinh dưỡng đã tổng hợp; metrics chứa mục tiêu cá nhân; mealGroups cho biết người dùng đã ghi nhận những bữa nào; clientHour hỗ trợ xác định thời điểm trong ngày theo phía người dùng. Đây là các dữ liệu cần thiết để hệ thống không chỉ biết người dùng ăn bao nhiêu, mà còn biết nên đưa ra cảnh báo vào thời điểm nào.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3517: tóm tắt cơ chế phân tầng trong Health Insights.
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Khi năng lượng đạt từ 70\% mục tiêu trở lên, hệ thống chuyển sang tầng vi lượng. Lúc này, mức năng lượng và đa lượng đã có đủ cơ sở để đánh giá chi tiết hơn. Hệ thống bắt đầu kiểm tra các yếu tố như chất xơ, canxi, sắt, vitamin C và vitamin A. Cách phân tầng này giúp Health Insights không đưa ra cùng một loại cảnh báo trong mọi thời điểm, mà lựa chọn nội dung phù hợp với mức độ đầy đủ của dữ liệu trong ngày.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3668: trình bày các nhóm xử lý chính trong Meal Planner.
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Ví dụ, nếu một bữa chiếm 30\% tổng mục tiêu trong ngày, thì năng lượng, protein, carbohydrate và chất béo của bữa đó cũng được tính theo tỷ lệ tương ứng. Cách làm này giúp Meal Planner không tạo khẩu phần rời rạc, mà luôn bám theo mục tiêu tổng thể của người dùng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3795: Luồng tra cứu mã vạch trong Hybrid Nutrition Scanner
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Nếu cả cơ sở dữ liệu cục bộ và Open Food Facts đều không tìm thấy dữ liệu, hệ thống trả về trạng thái không tìm thấy. Khi đó, Frontend có thể chuyển người dùng sang luồng AI Vision để chụp ảnh bảng dinh dưỡng. Luồng này đóng vai trò dự phòng cho những sản phẩm chưa có trong cơ sở dữ liệu mã vạch.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3926: Một số cơ chế bảo mật và xử lý lỗi trong Backend
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Bên cạnh xác thực, hệ thống áp dụng giới hạn request cho các route đăng nhập và đăng ký. Trong mã nguồn, nhóm route này được giới hạn 20 request trong 15 phút cho mỗi IP. Nếu vượt quá số lần cho phép, server trả về lỗi yêu cầu thử lại sau. Ngoài ra, chức năng AI Vision trong Scanner cũng có giới hạn request riêng theo người dùng, nhằm hạn chế việc gửi quá nhiều ảnh trong thời gian ngắn.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 3985: Môi trường phần mềm và công cụ thực nghiệm
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Hệ thống được kiểm thử trên môi trường phát triển cục bộ nhằm kiểm tra khả năng hoạt động của các chức năng chính trước khi đánh giá kết quả thực nghiệm. Backend được khởi chạy bằng Node.js, sử dụng Express để định nghĩa API và Sequelize ORM để thao tác với cơ sở dữ liệu MySQL. Frontend được xây dựng bằng React và Vite, sử dụng Axios để gửi yêu cầu HTTP đến backend, TanStack Query để quản lý dữ liệu lấy từ máy chủ và React Router để điều hướng giữa các trang chức năng. Các chức năng yêu cầu đăng nhập được kiểm thử thông qua cơ chế xác thực bằng access token và refresh token.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 4080: Kết quả kiểm thử chức năng chính của hệ thống
- **Label**: tab:kq_kiem_thu_chuc_nang
- **Status**: NEEDS_FIX
- **Context**: Nhìn chung, các nhóm chức năng chính của hệ thống đã đáp ứng được các luồng kiểm thử cơ bản trong phạm vi môi trường cục bộ. Các route yêu cầu đăng nhập chỉ được xử lý khi request có access token hợp lệ. Các thao tác thêm, sửa, xóa dữ liệu được kiểm tra theo phạm vi người dùng hiện tại, qua đó hạn chế truy cập dữ liệu của tài khoản khác. Các lỗi thường gặp như thiếu dữ liệu đầu vào, dữ liệu ngoài khoảng cho phép, token không hợp lệ, endpoint không tồn tại và gửi request vượt giới hạn đều được phản hồi bằng cấu trúc JSON thống nhất. Kết quả kiểm thử chức năng là cơ sở để tiếp tục đánh giá các thuật toán xử lý chính trong mục 4.3.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 4124: Kết quả thực nghiệm các thuật toán chính
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Dữ liệu thực nghiệm được chuẩn bị theo các tình huống thường gặp trong quá trình sử dụng hệ thống. Với Nutrition Core, dữ liệu đầu vào gồm giới tính, tuổi, chiều cao, cân nặng, mức độ vận động và mục tiêu cá nhân. Với Adaptive TDEE, dữ liệu đầu vào gồm nhật ký năng lượng và cân nặng theo tuần. Với Food Scoring, dữ liệu thực phẩm được kiểm tra theo các chỉ số năng lượng, protein, carbohydrate, chất béo, chất xơ, đường và natri. Với Health Insights, dữ liệu nhật ký trong ngày được dùng để sinh cảnh báo hoặc gợi ý. Với Meal Planner, hệ thống được thử với các mục tiêu năng lượng và macro khác nhau. Với Hybrid Nutrition Scanner, dữ liệu thực nghiệm gồm barcode và ảnh bảng thành phần dinh dưỡng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 4170: Tổng hợp đánh giá kết quả thực nghiệm
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Đối với Meal Planner, thực nghiệm tập trung vào khả năng tạo khẩu phần theo mục tiêu năng lượng và macro của bữa ăn. Hệ thống trả về danh sách nguyên liệu, khối lượng hoặc khẩu phần ước tính, tổng năng lượng và các chất dinh dưỡng chính. Khi tổ hợp nguyên liệu không tạo được kết quả hợp lệ, hệ thống không ghi nhận khẩu phần sai lệch mà trả về thông báo để người dùng thay đổi lựa chọn. Đối với Hybrid Nutrition Scanner, hai luồng chính được kiểm tra gồm tra cứu barcode và nhận dạng ảnh nhãn dinh dưỡng. Khi barcode khớp với dữ liệu đã có, hệ thống trả về thông tin sản phẩm tương ứng. Khi dữ liệu được trích xuất từ ảnh còn thiếu hoặc không đạt điều kiện kiểm tra hợp lệ, hệ thống yêu cầu xác nhận trước khi lưu vào cơ sở dữ liệu. Nhìn chung, các thuật toán chính đã xử lý được các tình huống dữ liệu cơ bản và trả về kết quả phù hợp với mục tiêu của từng chức năng. Nutrition Core đóng vai trò tính toán nền tảng, Adaptive TDEE hỗ trợ điều chỉnh theo dữ liệu thực tế, Food Scoring đánh giá chất lượng món ăn, Health Insights chuyển dữ liệu thành cảnh báo, Meal Planner tạo khẩu phần theo mục tiêu và Scanner hỗ trợ thu thập dữ liệu thực phẩm. Kết quả thực nghiệm cũng cho thấy chất lượng dữ liệu đầu vào vẫn là yếu tố ảnh hưởng trực tiếp đến kết quả xử lý.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 4194: Hạn chế và hướng phát triển của hệ thống
- **Label**: 
- **Status**: MISSING_LABEL
- **Context**: Đối với các thuật toán xử lý, Nutrition Core, Adaptive TDEE, Food Scoring, Health Insights và Meal Planner đều phụ thuộc vào độ đầy đủ của dữ liệu đầu vào. Nếu người dùng ghi nhật ký ăn uống không thường xuyên, nhập sai cân nặng hoặc bỏ qua dữ liệu luyện tập, kết quả tổng hợp và các gợi ý có thể bị sai lệch. Riêng Meal Planner đã hỗ trợ loại trừ thực phẩm dị ứng và ghim nguyên liệu khi sinh gợi ý bữa ăn, nhưng kết quả vẫn phụ thuộc vào độ phong phú của dữ liệu nguyên liệu, mẫu bữa ăn và cấu hình bữa ăn. Chức năng Hybrid Nutrition Scanner cũng chịu ảnh hưởng bởi chất lượng ảnh, góc chụp, độ rõ của nhãn sản phẩm và cách trình bày thông tin dinh dưỡng trên bao bì. Vì vậy, kết quả trích xuất từ ảnh cần tiếp tục được kiểm soát bằng bước xác nhận của người dùng.
- **Has Ref**: False
- **Has Non-Standard Word**: False

## Line 4222: Tổng hợp nội dung đánh giá trong Chương 4
- **Label**: tab:tong_hop_chuong_4
- **Status**: NEEDS_FIX
- **Context**: Dữ liệu thực nghiệm chủ yếu được kiểm tra trên môi trường cục bộ & Triển khai thử nghiệm trên môi trường máy chủ và kiểm tra với nhiều tài khoản người dùng \\ Cơ sở dữ liệu thực phẩm và sản phẩm đóng gói còn phụ thuộc vào dữ liệu nhập sẵn & Mở rộng nguồn dữ liệu thực phẩm và bổ sung cơ chế kiểm duyệt dữ liệu do người dùng đóng góp \\ Kết quả Adaptive TDEE phụ thuộc vào nhật ký cân nặng và năng lượng nhiều ngày & Bổ sung cơ chế nhắc nhập dữ liệu và đánh giá độ tin cậy của từng giai đoạn theo dõi \\ Meal Planner đã có loại trừ dị ứng và ghim nguyên liệu, nhưng còn phụ thuộc vào dữ liệu nguyên liệu và mẫu bữa ăn & Mở rộng mẫu bữa ăn, bổ sung ràng buộc về khẩu vị, ngân sách, thời gian chuẩn bị và mục tiêu theo từng giai đoạn \\ Scanner phụ thuộc vào chất lượng ảnh, barcode và thông tin trên nhãn sản phẩm & Cải thiện bước kiểm tra dữ liệu sau nhận dạng và quy trình xác nhận trước khi lưu \\ Báo cáo PDF mới tập trung vào dữ liệu theo tuần và tháng & Bổ sung biểu đồ xu hướng dài hạn và so sánh giữa các giai đoạn theo dõi \\
- **Has Ref**: False
- **Has Non-Standard Word**: False

