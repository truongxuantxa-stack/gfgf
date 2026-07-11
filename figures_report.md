# Báo cáo rà soát hình ảnh

## Hình 1: Mô hình tổng quan dữ liệu của hệ thống quản lý dinh dưỡng cá nhân (Dòng 409)
- **Label**: `fig:tong_quan_bai_toan`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:tong_quan_bai_toan}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: \textbf{Cuối cùng}, dữ liệu thực phẩm không phải lúc nào cũng đầy đủ trong cơ sở dữ liệu nội bộ. Đối với các sản phẩm đóng gói hoặc sản phẩm mới, hệ thống cần có cơ chế hỗ trợ nhập liệu thông qua tra cứu mã vạch hoặc nhận dạng bảng thành phần dinh dưỡng từ hình ảnh nhằm giảm khối lượng thao tác của người dùng.

## Hình 2: Mô hình liên kết các công nghệ trong hệ thống (Dòng 644)
- **Label**: `fig:cac_cong_nghe`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:cac_cong_nghe}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Hệ thống được xây dựng hoàn toàn trên nền tảng JavaScript ở cả phía máy khách và máy chủ. Việc sử dụng cùng một ngôn ngữ lập trình giúp giảm sự khác biệt giữa Frontend và Backend, đồng thời thuận lợi cho việc tổ chức mã nguồn và chia sẻ các thành phần xử lý.

## Hình 3: Kiến trúc truy cập dữ liệu thông qua Sequelize ORM (Dòng 719)
- **Label**: `fig:data_access_architecture`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:data_access_architecture}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Ngoài ra, Sequelize được sử dụng để thiết lập quan hệ giữa các bảng dữ liệu, quản lý Migration và Seeder, đồng thời hỗ trợ định nghĩa Association giữa các Model nhằm phục vụ các truy vấn dữ liệu có liên kết giữa nhiều bảng. Điều này góp phần đảm bảo tính nhất quán của cơ sở dữ liệu và thuận lợi cho việc mở rộng hệ thống.

## Hình 4: Kiến trúc tổng thể Client - Server của hệ thống (Dòng 825)
- **Label**: `fig:kientruc_tongthe`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:kientruc_tongthe}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Trong mô hình này, người dùng thao tác trên giao diện được xây dựng bằng React thông qua trình duyệt web. Các yêu cầu như đăng nhập, cập nhật hồ sơ sức khỏe, ghi nhận nhật ký ăn uống, theo dõi cân nặng, xây dựng thực đơn hoặc quét thực phẩm được gửi đến Backend thông qua Axios dưới dạng các yêu cầu HTTP. Backend tiếp nhận yêu cầu, thực hiện xác thực người dùng, xử lý nghiệp vụ, truy xuất cơ sở dữ liệu hoặc gọi các dịch vụ bên ngoài khi cần thiết trước khi trả kết quả về cho Frontend dưới dạng dữ liệu JSON.

## Hình 5: Kiến trúc Frontend trong ứng dụng React SPA (Dòng 906)
- **Label**: `fig:kientruc_frontend`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:kientruc_frontend}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Việc trao đổi dữ liệu giữa Frontend và Backend được thực hiện thông qua \textbf{Axios}, đóng vai trò gửi yêu cầu HTTP và nhận dữ liệu phản hồi từ các RESTful API.

## Hình 6: Kiến trúc Backend theo mô hình MVC kết hợp Service (Dòng 981)
- **Label**: `fig:kientruc_backend`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:kientruc_backend}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Việc tách riêng tầng Service giúp Controller chỉ đảm nhiệm vai trò điều phối yêu cầu, trong khi toàn bộ logic nghiệp vụ được quản lý tập trung, góp phần nâng cao khả năng bảo trì, kiểm thử và mở rộng hệ thống.

## Hình 7: Kiến trúc tổng quan cơ sở dữ liệu (Dòng 1060)
- **Label**: `fig:kientruc_csdl`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:kientruc_csdl}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Trong phạm vi chương này chỉ trình bày kiến trúc tổng quan của cơ sở dữ liệu. Thiết kế chi tiết các bảng dữ liệu, mối quan hệ giữa các thực thể và sơ đồ ERD sẽ được trình bày trong Chương 2.

## Hình 8: Biểu đồ Use Case tổng thể của hệ thống (Dòng 1301)
- **Label**: `fig:usecase_tong_the`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:usecase_tong_the}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: \subsection{Biểu đồ Use Case tổng thể}Biểu đồ Use Case tổng thể thể hiện các chức năng chính mà người dùng có thể thực hiện trong hệ thống. Các Use Case được chia thành các nhóm chức năng tương ứng với các nghiệp vụ đã phân tích, bao gồm xác thực người dùng, quản lý hồ sơ sức khỏe, ghi nhận dữ liệu hằng ngày, theo dõi chỉ số cá nhân, sử dụng Scanner, xây dựng thực đơn, xem Dashboard và xuất báo cáo.

## Hình 9: Sơ đồ ERD rút gọn của hệ thống (Dòng 1562)
- **Label**: `fig:erd_rut_gon`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:erd_rut_gon}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Trong phạm vi chương này, phần thiết kế cơ sở dữ liệu chỉ trình bày các nhóm bảng chính, quan hệ giữa các bảng và một số quyết định thiết kế quan trọng. Danh sách trường dữ liệu chi tiết, kiểu dữ liệu, ràng buộc cụ thể và ERD đầy đủ được trình bày trong Phụ lục C.

## Hình 10: Luồng request/response giữa Frontend và Backend (Dòng 1781)
- **Label**: `fig:api_flow`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:api_flow}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Thứ năm, một số API nhạy cảm hoặc phụ thuộc dịch vụ bên ngoài cần được giới hạn tần suất gọi. Các API như đăng nhập, đăng ký và nhận dạng hình ảnh bằng AI Vision cần có cơ chế hạn chế số lượng yêu cầu trong một khoảng thời gian nhằm giảm rủi ro lạm dụng và hạn chế tải không cần thiết cho hệ thống.

## Hình 11: Luồng xác thực API bằng JWT (Dòng 1913)
- **Label**: `fig:jwt-auth-flow`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:jwt-auth-flow}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: \subsection{Thiết kế xác thực API}

## Hình 12: Luồng xử lý một request có xác thực trong hệ thống (Dòng 2011)
- **Label**: `fig:request_auth_flow`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Hình \ref{fig:request_auth_flow} mô tả chi tiết luồng xử lý bên trong hệ thống khi một request có xác thực được gửi lên. Frontend đính kèm Access Token vào header, Middleware kiểm tra tính hợp lệ của token trước khi chuyển request vào Controller. Controller điều phối sang Service để xử lý nghiệp vụ, Service làm việc với Sequelize Model để truy vấn MySQL, kết quả được trả ngược lại Frontend dưới dạng JSON.

## Hình 13: Sơ đồ điều hướng giao diện của hệ thống (Dòng 2322)
- **Label**: `fig:ui-navigation`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:ui-navigation}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Thanh điều hướng được sử dụng để chuyển giữa các chức năng chính. Vùng nội dung chính thay đổi theo trang hiện tại. Các thành phần dùng chung như nút, thẻ thông tin, biểu đồ, modal và biểu mẫu được tái sử dụng giữa nhiều màn hình để giữ giao diện nhất quán.

## Hình 14: Wireframe giao diện Dashboard (Dòng 2402)
- **Label**: `fig:dashboard-ui`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:dashboard-ui}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Dashboard không chỉ hiển thị dữ liệu mà còn đóng vai trò là điểm truy cập nhanh tới một số thao tác thường dùng như thêm thực phẩm, ghi nhận nước uống hoặc xem báo cáo. Vì vậy, giao diện cần ưu tiên khả năng tổng hợp, dễ quan sát và hạn chế số bước thao tác.

## Hình 15: Wireframe giao diện Nhật ký ăn uống và Modal Scanner (Dòng 2505)
- **Label**: `fig:diary-scanner`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Sau khi người dùng xác nhận thêm thực phẩm vào nhật ký, dữ liệu được gửi tới Backend để lưu lại. Các giá trị dinh dưỡng tại thời điểm ghi nhận cần được lưu cùng bản ghi nhật ký nhằm bảo toàn dữ liệu lịch sử khi thông tin thực phẩm gốc thay đổi. Chi tiết về giao diện nhật ký ăn uống và các phương thức quét thông minh được trình bày trong Hình \ref{fig:diary-scanner}.

## Hình 16: Wireframe giao diện chức năng Meal Planner (Dòng 2606)
- **Label**: `fig:meal_planner_ui`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Sau khi hệ thống sinh thực đơn, người dùng có thể thay thế nguyên liệu nếu cần hoặc xác nhận sử dụng kết quả. Kết quả thực đơn có thể được dùng làm dữ liệu đầu vào cho nhật ký ăn uống trong ngày. Do chức năng này liên quan trực tiếp đến thuật toán Meal Planner, giao diện cần thể hiện rõ dữ liệu đầu vào, trạng thái xử lý và kết quả đầu ra để người dùng hiểu được thao tác đang thực hiện. Chi tiết giao diện được minh họa trong Hình \ref{fig:meal_planner_ui}.

## Hình 17: Sơ đồ kiến trúc phân lớp Backend của NutriTrack (Dòng 2741)
- **Label**: `fig:backend_architecture`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:backend_architecture}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Đối với NutriTrack, tầng service giữ vai trò quan trọng vì hệ thống không chỉ thực hiện các thao tác thêm, sửa, xóa dữ liệu. Nhiều chức năng cần tổng hợp dữ liệu theo ngày, tính toán chỉ số dinh dưỡng, đối chiếu với mục tiêu cá nhân và tạo kết quả đầu ra cho giao diện. Vì vậy, controller chủ yếu tiếp nhận request và trả response, còn phần xử lý nghiệp vụ được chuyển xuống service để giảm lặp logic giữa các module.

## Hình 18: Sơ đồ luồng xử lý một request có xác thực. \textit{(Ghi chú: Bước kiểm tra Token ở Middleware bao gồm giải mã JWT và kiểm tra tính hợp lệ của User trong cơ sở dữ liệu). (Dòng 2864)
- **Label**: `fig:auth_flow`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Chi tiết luồng xử lý một request có xác thực được minh họa trong Hình \ref{fig:auth_flow}.

## Hình 19: Sơ đồ tổng quan kiến trúc Frontend của NutriTrack (Dòng 2957)
- **Label**: `fig:frontend_architecture`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:frontend_architecture}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: Frontend không đảm nhiệm trực tiếp các thuật toán dinh dưỡng phức tạp. Các xử lý như Nutrition Core, Adaptive TDEE, Food Scoring, Health Insights và Meal Planner được thực hiện chủ yếu ở Backend để bảo đảm kết quả tính toán thống nhất giữa các màn hình. Frontend nhận dữ liệu đã được xử lý từ API, sau đó tổ chức hiển thị dưới dạng thẻ thông tin, biểu đồ, bảng dữ liệu, modal nhập liệu và thông báo trạng thái. Cách phân chia này làm rõ ranh giới giữa tầng giao diện và tầng nghiệp vụ, đồng thời hạn chế việc lặp lại công thức ở phía client.

## Hình 20: Sơ đồ luồng gọi API ở Frontend (Happy Path) (Dòng 3080)
- **Label**: `fig:luong-goi-api-frontend`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Sự phối hợp và luồng dữ liệu khi gọi API giữa các thành phần ở Frontend (Component, Custom Hook, TanStack Query, Axios) và Backend được mô tả chi tiết trong Hình \ref{fig:luong-goi-api-frontend}.

## Hình 21: Sơ đồ luồng xử lý Nutrition Core (Dòng 3189)
- **Label**: `fig:luong-xu-ly-nutrition-core`
- **Vấn đề**:
  - Sử dụng từ ngữ không chuẩn: như sau
- **Đoạn dẫn hiện tại**: Quá trình tính toán này được mô tả tổng quan qua Hình \ref{fig:luong-xu-ly-nutrition-core}.

## Hình 22: Sơ đồ luồng xử lý Adaptive TDEE (Dòng 3318)
- **Label**: `fig:adaptive_tdee_flow`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Chi tiết luồng xử lý Adaptive TDEE được minh họa trong Hình \ref{fig:adaptive_tdee_flow}.

## Hình 23: Sơ đồ luồng xử lý của module Health Insights (Dòng 3598)
- **Label**: `fig:health_insights_flow`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Health Insights đóng vai trò chuyển dữ liệu định lượng thành thông tin diễn giải ngắn. Các con số như tổng calo, lượng protein, chất xơ hoặc nước uống sẽ có ý nghĩa hơn khi được so sánh với mục tiêu cá nhân. Nhờ đó, người dùng không chỉ xem dữ liệu đã ghi nhận mà còn biết chỉ số nào đang cần chú ý hơn trong ngày (chi tiết luồng xử lý được minh họa trong Hình \ref{fig:health_insights_flow}).

## Hình 24: Sơ đồ luồng xử lý của Meal Planner (Dòng 3755)
- **Label**: `fig:meal_planner_flow`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Chi tiết sơ đồ luồng Meal Planner được thể hiện trong Hình \ref{fig:meal_planner_flow}.

## Hình 25: Sơ đồ luồng xử lý của Hybrid Nutrition Scanner (Dòng 3878)
- **Label**: `fig:hybrid_scanner_flow`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Chi tiết sơ đồ luồng Hybrid Nutrition Scanner được thể hiện trong Hình \ref{fig:hybrid_scanner_flow}.

## Hình 26: Màn hình Onboarding / Tính TDEE (Dòng 4061)
- **Label**: `fig:onboarding`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Đối với nhóm hồ sơ người dùng, kiểm thử tập trung vào luồng onboarding và cập nhật thông tin cá nhân. Người dùng cần cung cấp các thông tin cơ bản như giới tính, ngày sinh, chiều cao, cân nặng, mức độ vận động và mục tiêu. Đây là các dữ liệu đầu vào cần thiết để hệ thống tính BMI, BMR, TDEE, mục tiêu năng lượng và mục tiêu nước. Khi dữ liệu hợp lệ, thông tin được lưu vào cơ sở dữ liệu và trạng thái hoàn thành onboarding được chuyển sang true. Khi dữ liệu nằm ngoài khoảng cho phép, hệ thống trả về thông báo lỗi và không cập nhật bản ghi (xem minh họa trong Hình \ref{fig:onboarding}).

## Hình 27: Màn hình Dashboard (Tổng quan) (Dòng 4072)
- **Label**: `fig:dashboard`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Đối với nhóm nhật ký dinh dưỡng và dashboard, kiểm thử được thực hiện bằng cách thêm món ăn vào từng bữa trong ngày, thay đổi khẩu phần và xóa bản ghi đã thêm. Khi một món ăn được ghi nhận, hệ thống lưu khẩu phần, bữa ăn, ngày sử dụng và các giá trị dinh dưỡng tại thời điểm thêm. Cách lưu này giúp dữ liệu nhật ký giữ nguyên giá trị đã ghi nhận, kể cả khi thông tin món ăn trong cơ sở dữ liệu được chỉnh sửa sau đó. Sau khi nhật ký thay đổi, dashboard cần cập nhật lại tổng năng lượng, protein, carbohydrate, chất béo, lượng nước, năng lượng tiêu hao từ luyện tập và các chỉ số cơ thể liên quan. Kết quả kiểm thử cho thấy dữ liệu hiển thị trên dashboard thay đổi tương ứng với các bản ghi đã thêm hoặc xóa trong nhật ký (chi tiết màn hình Nhật ký và Dashboard được minh họa lần lượt trong Hình \ref{fig:nhat_ky_dinh_duong} và Hình \ref{fig:dashboard}).

## Hình 28: Màn hình nhật ký dinh dưỡng sau khi thêm món ăn vào bữa trong ngày (Dòng 4079)
- **Label**: `fig:nhat_ky_dinh_duong`
- **Vấn đề**:
  - Không tìm thấy `\ref{fig:nhat_ky_dinh_duong}` trong đoạn văn trước hình.
- **Đoạn dẫn hiện tại**: \end{figure}

## Hình 29: Màn hình gợi ý bữa ăn từ chức năng Meal Planner (Dòng 4090)
- **Label**: `fig:meal_planner`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Đối với nhóm Meal Planner, kiểm thử tập trung vào các thao tác lấy cấu hình bữa ăn, cập nhật cấu hình, sinh gợi ý bữa ăn và thay thế nguyên liệu. Kết quả trả về cần có cấu trúc rõ ràng để frontend hiển thị, bao gồm danh sách nguyên liệu, khối lượng hoặc khẩu phần ước tính, tổng năng lượng và các chất dinh dưỡng chính. Trường hợp thay thế nguyên liệu được kiểm tra nhằm bảo đảm hệ thống vẫn trả về một phương án bữa ăn có thể hiển thị sau khi người dùng thay đổi thành phần trong gợi ý ban đầu (xem minh họa trong Hình \ref{fig:meal_planner}).

## Hình 30: Màn hình Hybrid Nutrition Scanner (Quét đồ ăn bằng AI) (Dòng 4099)
- **Label**: `fig:scanner`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Đối với nhóm Hybrid Nutrition Scanner, các trường hợp kiểm thử gồm tra cứu sản phẩm bằng barcode, giải mã barcode từ ảnh, trích xuất thông tin dinh dưỡng từ ảnh, xác nhận đóng góp dữ liệu sản phẩm, tải ảnh sản phẩm và báo cáo dữ liệu sản phẩm sai. Khi dữ liệu ảnh hoặc barcode không đủ điều kiện xử lý, hệ thống trả về thông báo lỗi thay vì ghi nhận dữ liệu chưa được xác nhận. Đối với dữ liệu sản phẩm mới, hệ thống yêu cầu người dùng xác nhận trước khi lưu đóng góp vào cơ sở dữ liệu. Cách xử lý này giúp hạn chế việc lưu các bản ghi sản phẩm thiếu thông tin hoặc chưa đủ độ tin cậy (xem minh họa trong Hình \ref{fig:scanner}).

## Hình 31: Màn hình Food Scoring (Chấm điểm thực phẩm) (Dòng 4186)
- **Label**: `fig:food_scoring`
- **Trạng thái**: Hợp lệ
- **Đoạn dẫn hiện tại**: Đối với Food Scoring và Health Insights, kết quả thực nghiệm cho thấy hệ thống có thể chuyển dữ liệu dinh dưỡng thành điểm số, cảnh báo và gợi ý ngắn gọn. Trong phạm vi dữ liệu thử nghiệm, các món có mật độ protein hoặc chất xơ cao, đồng thời có lượng đường và natri thấp, nhận điểm tốt hơn. Ngược lại, món có nhiều đường, natri hoặc năng lượng cao nhưng ít chất dinh dưỡng có xu hướng bị giảm điểm (xem minh họa màn hình chấm điểm trong Hình \ref{fig:food_scoring}).

