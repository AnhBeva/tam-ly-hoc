from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent


TAPS = [
    {
        "n": 51,
        "file": "Tap-51-Tam-ly-hoc-dai-cuong-ban-do-nen-cua-tam-tri.md",
        "title": "Tâm Lý Học Đại Cương: Bản Đồ Nền Của Tâm Trí",
        "subtitle": "Nắm các cấu phần gốc của tâm lý học: cảm giác, tri giác, chú ý, trí nhớ, tư duy, cảm xúc, động cơ và hành vi",
        "core": "Tâm lý học đại cương là bản đồ nền giúp ta biết một hiện tượng con người đang thuộc tầng nào trước khi giải thích hoặc can thiệp.",
        "why": [
            "Không có nền đại cương, người học dễ nhảy thẳng vào kỹ thuật và hiểu rời rạc.",
            "C-level cần bản đồ để biết vấn đề thuộc não bộ, nhận thức, cảm xúc, động cơ, quan hệ hay hệ thống.",
            "Đại cương giúp phân biệt quan sát, giả thuyết, diễn giải và kết luận.",
            "Đây là lớp nền để đọc mọi nhánh tâm lý khác tỉnh táo hơn.",
        ],
        "pillars": [
            ("Cảm giác và tri giác", "Cảm giác là dữ liệu thô; tri giác là não tổ chức dữ liệu thành ý nghĩa.", "Tôi đang thấy dữ kiện hay thấy diễn giải của não?"),
            ("Chú ý", "Chú ý là cổng vào của nhận thức; thứ không được chú ý thường không được xử lý sâu.", "Tôi đang cho điều gì quyền chiếm não mình?"),
            ("Trí nhớ", "Trí nhớ là tái dựng có chọn lọc, không phải bản ghi nguyên vẹn.", "Ký ức này có thể bị cảm xúc hiện tại sửa lại không?"),
            ("Tư duy", "Tư duy là thao tác với thông tin để hiểu, dự đoán và quyết định.", "Tôi đang dùng mô hình nào để nghĩ?"),
            ("Cảm xúc", "Cảm xúc là tín hiệu về nhu cầu, nguy cơ và giá trị.", "Cảm xúc này đang báo điều gì cần bảo vệ?"),
            ("Động cơ", "Động cơ là lực kéo hành vi về phía nhu cầu, mục tiêu hoặc tránh đau.", "Người này thật sự đang muốn gì hoặc tránh gì?"),
            ("Hành vi", "Hành vi là phần nhìn thấy của hệ tâm lý bên trong và môi trường bên ngoài.", "Hành vi này đang được hệ thống nào duy trì?"),
        ],
        "tools": [
            ("Bản đồ 7 tầng hiện tượng", ["Hiện tượng:", "Cảm giác/tri giác:", "Chú ý:", "Trí nhớ:", "Tư duy:", "Cảm xúc:", "Động cơ:", "Hành vi:", "Giả thuyết cần kiểm chứng:"]),
            ("Checklist chống kết luận vội", ["Tôi thấy dữ kiện nào?", "Tôi đang diễn giải gì?", "Có cách giải thích khác không?", "Tầng nào chưa được xem xét?", "Cần quan sát thêm gì?"]),
        ],
        "final": "Muốn hiểu sâu một con người, trước hết phải biết mình đang nhìn tầng nào của hệ tâm trí.",
    },
    {
        "n": 52,
        "file": "Tap-52-Tam-ly-nhan-thuc-nang-cao.md",
        "title": "Tâm Lý Nhận Thức Nâng Cao: Chú Ý, Tri Giác, Ngôn Ngữ, Giải Quyết Vấn Đề",
        "subtitle": "Hiểu cách não xử lý thông tin, tạo mô hình, dùng ngôn ngữ, chịu tải nhận thức và giải quyết vấn đề phức tạp",
        "core": "Nhận thức là hệ xử lý thông tin có giới hạn; muốn nghĩ tốt phải thiết kế thông tin, môi trường và câu hỏi phù hợp với giới hạn đó.",
        "why": [
            "Lãnh đạo thường thất bại không vì thiếu dữ liệu, mà vì dữ liệu quá tải, sai khung hoặc sai câu hỏi.",
            "Sản phẩm, đào tạo và quản trị đều phụ thuộc vào cách con người chú ý, hiểu và nhớ.",
            "Ngôn ngữ định hình cách con người phân loại thực tại.",
            "Hiểu tải nhận thức giúp giảm sai lầm trong quyết định và truyền thông.",
        ],
        "pillars": [
            ("Tải nhận thức", "Não chỉ xử lý được một lượng thông tin hữu hạn tại một thời điểm.", "Tôi có đang bắt người khác xử lý quá nhiều cùng lúc không?"),
            ("Mental models", "Con người hiểu thế giới qua mô hình đơn giản hóa.", "Mô hình nào đang làm tôi thấy đúng nhưng có thể sai?"),
            ("Tri giác có dự đoán", "Não không chỉ nhận dữ liệu; nó dự đoán rồi sửa dự đoán.", "Kỳ vọng nào đang làm tôi nhìn lệch?"),
            ("Ngôn ngữ", "Từ ngữ không chỉ mô tả thực tại, mà còn tạo khung để nghĩ về thực tại.", "Nếu đổi tên vấn đề, suy nghĩ có đổi không?"),
            ("Giải quyết vấn đề", "Vấn đề khó cần tách mục tiêu, ràng buộc, giả định và feedback.", "Vấn đề thật là gì, không phải triệu chứng là gì?"),
            ("Insight", "Insight thường đến khi não tái cấu trúc vấn đề thay vì cố cùng một hướng.", "Tôi cần thêm dữ liệu hay cần đổi khung?"),
            ("Sai lầm nhận thức", "Sai lầm thường là kết quả của shortcut hữu ích trong bối cảnh sai.", "Shortcut này từng đúng ở đâu nhưng sai ở đây?"),
        ],
        "tools": [
            ("Canvas giải quyết vấn đề", ["Vấn đề:", "Mục tiêu:", "Ràng buộc:", "Giả định:", "Dữ kiện thiếu:", "Mô hình đang dùng:", "Khung thay thế:", "Thử nghiệm nhỏ:"]),
            ("Audit tải nhận thức", ["Thông tin cần truyền:", "Điều bắt buộc nhớ:", "Điều có thể bỏ:", "Thứ tự trình bày:", "Ví dụ trực quan:", "Cách kiểm tra đã hiểu:"]),
        ],
        "final": "Nghĩ tốt không chỉ là thông minh; đó là biết giảm tải, đổi khung và kiểm tra mô hình đang dùng.",
    },
    {
        "n": 53,
        "file": "Tap-53-Tam-ly-dong-co-vi-sao-con-nguoi-muon-tri-hoan-va-ben-bi.md",
        "title": "Tâm Lý Động Cơ: Vì Sao Con Người Muốn, Trì Hoãn Và Bền Bỉ",
        "subtitle": "Hiểu nhu cầu, mục tiêu, phần thưởng, tự chủ, ý nghĩa, trì hoãn, grit và thiết kế động lực bền vững",
        "core": "Động cơ là năng lượng định hướng hành vi; nó mạnh khi nhu cầu thật, ý nghĩa, năng lực và môi trường cùng kéo về một hướng.",
        "why": [
            "Không hiểu động cơ thì quản trị chỉ còn ép, thưởng, phạt hoặc truyền cảm hứng ngắn hạn.",
            "Người trưởng thành trì hoãn không chỉ vì lười, mà vì sợ, mơ hồ, quá tải hoặc thiếu ý nghĩa.",
            "Động lực bền cần tự chủ, cảm giác tiến bộ và mục đích đáng làm.",
            "C-level cần thiết kế hệ thống làm người tốt muốn làm việc tốt.",
        ],
        "pillars": [
            ("Nhu cầu", "Con người hành động để đáp ứng nhu cầu sinh tồn, thuộc về, năng lực, tự chủ và ý nghĩa.", "Nhu cầu nào đang bị thiếu?"),
            ("Mục tiêu", "Mục tiêu rõ định hướng chú ý và năng lượng.", "Mục tiêu này có đủ rõ để hành động hôm nay không?"),
            ("Phần thưởng", "Phần thưởng kéo hành vi, nhưng có thể phá động cơ nội tại nếu thiết kế sai.", "Ta đang thưởng kết quả hay thưởng hành vi tạo kết quả?"),
            ("Tự chủ", "Con người bền hơn khi cảm thấy mình có quyền chọn và có tiếng nói.", "Tôi đang trao quyền hay chỉ giao việc?"),
            ("Năng lực", "Động lực tăng khi người ta thấy mình tiến bộ thật.", "Feedback có giúp họ thấy tiến bộ không?"),
            ("Trì hoãn", "Trì hoãn thường là điều tiết cảm xúc ngắn hạn.", "Tôi đang né cảm xúc nào bằng trì hoãn?"),
            ("Bền bỉ", "Bền bỉ đến từ ý nghĩa, nhịp phục hồi, môi trường và bản sắc.", "Hệ nào giúp tôi tiếp tục khi cảm hứng mất?"),
        ],
        "tools": [
            ("Bản đồ động cơ", ["Hành vi muốn có:", "Nhu cầu thật:", "Nỗi sợ:", "Phần thưởng hiện tại:", "Ý nghĩa:", "Cản trở:", "Thiết kế môi trường:"]),
            ("Chống trì hoãn", ["Việc đang né:", "Cảm xúc khó chịu:", "Bước nhỏ 5 phút:", "Ai cần biết cam kết:", "Phần thưởng sau hành động:", "Thời điểm review:"]),
        ],
        "final": "Động lực bền không đến từ hô hào; nó đến từ nhu cầu đúng, mục tiêu rõ, tiến bộ thật và môi trường biết nâng hành vi tốt.",
    },
    {
        "n": 54,
        "file": "Tap-54-Tam-ly-tham-van-nghe-thuat-ho-tro-nguoi-khac.md",
        "title": "Tâm Lý Tham Vấn: Nghệ Thuật Hỗ Trợ Người Khác Mà Không Làm Thay",
        "subtitle": "Hiểu khác biệt giữa tham vấn, trị liệu, coaching; biết lắng nghe, phản chiếu, giữ ranh giới và chuyển tuyến khi cần",
        "core": "Tham vấn là tạo không gian an toàn để người khác hiểu mình rõ hơn, tự ra quyết định tốt hơn và nhận hỗ trợ phù hợp mà không bị kiểm soát.",
        "why": [
            "Lãnh đạo và cha mẹ thường muốn sửa người khác quá nhanh.",
            "Tham vấn giúp hỗ trợ mà không áp đặt, cứu hộ hoặc làm thay.",
            "Biết giới hạn giúp tránh nhầm vai giữa bạn bè, lãnh đạo, coach và chuyên gia lâm sàng.",
            "Đây là năng lực nền cho coaching, mentoring, HR và gia đình.",
        ],
        "pillars": [
            ("Liên minh hỗ trợ", "Người được hỗ trợ cần cảm thấy an toàn, được tôn trọng và không bị phán xét.", "Người này có thấy đủ an toàn để nói thật không?"),
            ("Lắng nghe phản chiếu", "Phản chiếu giúp người khác nghe lại chính mình rõ hơn.", "Tôi đang phản chiếu hay đang giảng đạo?"),
            ("Câu hỏi mở", "Câu hỏi tốt mở nhận thức thay vì ép câu trả lời.", "Câu hỏi này giúp họ tự thấy gì?"),
            ("Ranh giới", "Hỗ trợ không có nghĩa là chịu trách nhiệm thay đời sống của người khác.", "Phần nào là trách nhiệm của tôi, phần nào là của họ?"),
            ("Không làm hại", "Nguyên tắc đầu tiên là không làm tăng tổn thương, phụ thuộc hoặc xấu hổ.", "Can thiệp này có thể gây hại gì?"),
            ("Chuyển tuyến", "Khi có nguy cơ an toàn, rối loạn nặng hoặc suy giảm chức năng, cần chuyên gia.", "Dấu hiệu nào vượt quá vai trò của tôi?"),
            ("Tự chăm sóc người hỗ trợ", "Người hỗ trợ cũng cần ranh giới và phục hồi.", "Tôi có đang kiệt sức vì vai cứu hộ không?"),
        ],
        "tools": [
            ("Khung buổi hỗ trợ 30 phút", ["Mở an toàn:", "Vấn đề chính:", "Cảm xúc:", "Điều đã thử:", "Nguồn lực:", "Bước nhỏ:", "Khi nào cần chuyên gia:"]),
            ("Checklist chuyển tuyến", ["Có ý nghĩ tự hại/hại người không?", "Có mất chức năng sống không?", "Có sang chấn nặng không?", "Có lệ thuộc chất không?", "Có cần bác sĩ/chuyên gia không?"]),
        ],
        "final": "Hỗ trợ trưởng thành không phải kéo người khác đi theo ý mình; đó là giúp họ đủ rõ và đủ an toàn để tự bước phần của họ.",
    },
    {
        "n": 55,
        "file": "Tap-55-Tam-ly-hoc-duong-va-tuoi-thieu-nien.md",
        "title": "Tâm Lý Học Đường Và Tuổi Thiếu Niên",
        "subtitle": "Hiểu học sinh trong hệ sinh thái gia đình, bạn bè, trường học, mạng xã hội, bản sắc và áp lực thành tích",
        "core": "Trẻ vị thành niên không chỉ là người lớn thu nhỏ; các em đang tái thiết não bộ, bản sắc, quan hệ và nhu cầu độc lập trong một hệ áp lực mạnh.",
        "why": [
            "Tuổi thiếu niên là giai đoạn nhiều rủi ro và nhiều cơ hội can thiệp sớm.",
            "Vấn đề học đường thường nằm trong hệ sinh thái, không chỉ trong đứa trẻ.",
            "Cha mẹ thành công dễ áp mô hình thành tích của mình lên con.",
            "Hiểu học đường giúp phối hợp gia đình, giáo viên và chuyên gia tốt hơn.",
        ],
        "pillars": [
            ("Não vị thành niên", "Hệ cảm xúc phát triển nhanh hơn kiểm soát điều hành.", "Ta đang kỳ vọng tự chủ vượt quá độ chín não không?"),
            ("Bản sắc", "Tuổi thiếu niên là giai đoạn thử vai và tìm câu trả lời tôi là ai.", "Trẻ có không gian thử và sai an toàn không?"),
            ("Bạn bè", "Bạn bè trở thành nguồn thuộc về và đánh giá rất mạnh.", "Nhóm bạn đang củng cố hành vi nào?"),
            ("Áp lực thành tích", "Thành tích có thể tạo động lực hoặc làm trẻ đồng nhất giá trị với điểm số.", "Trẻ đang học vì tò mò hay vì sợ mất giá trị?"),
            ("Bắt nạt và loại trừ", "Bị loại trừ xã hội có thể gây đau tâm lý sâu.", "Có dấu hiệu cô lập hoặc xấu hổ kéo dài không?"),
            ("Mạng xã hội", "Mạng xã hội khuếch đại so sánh, bản sắc và phần thưởng tức thì.", "Nền tảng nào đang dạy trẻ về giá trị bản thân?"),
            ("Phối hợp hệ sinh thái", "Can thiệp tốt cần gia đình, trường học và trẻ cùng nhìn một vấn đề.", "Ai cần cùng ngồi vào bàn?"),
        ],
        "tools": [
            ("Bản đồ học đường", ["Vấn đề:", "Trẻ cảm thấy gì:", "Gia đình:", "Giáo viên:", "Bạn bè:", "Mạng xã hội:", "Nguồn lực:", "Bước phối hợp:"]),
            ("Cuộc trò chuyện với tuổi teen", ["Mở bằng quan sát:", "Hỏi cảm nhận:", "Không vội sửa:", "Cùng đặt ranh giới:", "Chọn một bước nhỏ:", "Hẹn review:"]),
        ],
        "final": "Muốn giúp tuổi teen, đừng chỉ sửa hành vi; hãy hiểu não đang lớn, bản sắc đang hình thành và hệ xung quanh đang dạy điều gì.",
    },
    {
        "n": 56,
        "file": "Tap-56-Tam-ly-tieu-dung-thuong-hieu-va-marketing.md",
        "title": "Tâm Lý Tiêu Dùng, Thương Hiệu Và Marketing",
        "subtitle": "Hiểu nhu cầu khách hàng, cảm xúc mua, định vị, giá, social proof, trải nghiệm và đạo đức ảnh hưởng",
        "core": "Khách hàng không mua sản phẩm thuần túy; họ mua cách sản phẩm giải quyết đau, tạo ý nghĩa, giảm rủi ro và giúp họ trở thành phiên bản mong muốn.",
        "why": [
            "C-level cần hiểu khách hàng thật thay vì chỉ nhìn phân khúc trên slide.",
            "Marketing hiệu quả bắt đầu từ nhu cầu, cảm xúc và bối cảnh ra quyết định.",
            "Thương hiệu mạnh là ký ức và niềm tin được lặp lại nhất quán.",
            "Hiểu tâm lý tiêu dùng giúp bán tốt mà không thao túng.",
        ],
        "pillars": [
            ("Nhu cầu khách hàng", "Nhu cầu thật thường sâu hơn tính năng được nói ra.", "Khách hàng đang đau vì điều gì?"),
            ("Giảm rủi ro", "Mua hàng là chấp nhận rủi ro tiền, thời gian, danh tiếng và cơ hội.", "Điều gì làm họ sợ chọn sai?"),
            ("Định vị", "Định vị là chỗ đứng rõ trong tâm trí khách hàng.", "Mình muốn được nhớ bằng một câu nào?"),
            ("Giá", "Giá không chỉ là số; nó là tín hiệu giá trị, rủi ro và vị thế.", "Giá đang nói gì về mình?"),
            ("Social proof", "Con người dùng lựa chọn của người khác để giảm bất định.", "Bằng chứng xã hội nào là thật và có đạo đức?"),
            ("Trải nghiệm", "Trải nghiệm tạo ký ức qua đỉnh cảm xúc, điểm đau và kết thúc.", "Khoảnh khắc nào khách hàng sẽ nhớ?"),
            ("Đạo đức marketing", "Ảnh hưởng đúng làm khách hàng rõ hơn; thao túng làm họ mất tự chủ.", "Thông điệp này tăng hay giảm quyền tự chủ của khách hàng?"),
        ],
        "tools": [
            ("Customer psychology canvas", ["Khách hàng:", "Pain:", "Fear:", "Desired identity:", "Risk:", "Trigger mua:", "Bằng chứng:", "Thông điệp chính:"]),
            ("Audit thương hiệu", ["Muốn được nhớ vì:", "Điểm khác biệt thật:", "Cảm xúc tạo ra:", "Bằng chứng:", "Điểm trải nghiệm yếu:", "Rủi ro đạo đức:"]),
        ],
        "final": "Marketing trưởng thành không phải làm người khác muốn thứ họ không cần; đó là giúp đúng người thấy rõ giá trị thật vào đúng thời điểm.",
    },
    {
        "n": 57,
        "file": "Tap-57-Human-factors-UX-va-tuong-tac-nguoi-may.md",
        "title": "Human Factors, UX Và Tương Tác Người-Máy",
        "subtitle": "Hiểu giới hạn con người khi dùng sản phẩm, hệ thống, AI, thiết bị và quy trình có rủi ro cao",
        "core": "Hệ thống tốt không bắt con người thích nghi với máy; nó thiết kế quanh giới hạn chú ý, trí nhớ, sai sót, thao tác và bối cảnh thật của con người.",
        "why": [
            "Nhiều lỗi bị gọi là lỗi người dùng thật ra là lỗi thiết kế hệ thống.",
            "AI, app, thiết bị và quy trình càng mạnh càng cần human factors.",
            "UX tốt làm hành động đúng dễ, hành động sai khó và hậu quả rõ.",
            "C-level sản phẩm cần biết thiết kế cho con người thật, không phải người dùng lý tưởng.",
        ],
        "pillars": [
            ("Affordance", "Thiết kế nên gợi ý người dùng có thể làm gì.", "Nhìn vào đây, người dùng biết phải làm gì không?"),
            ("Feedback", "Mỗi hành động cần phản hồi rõ để người dùng biết hệ thống đã hiểu.", "Sau thao tác, người dùng có biết chuyện gì xảy ra không?"),
            ("Tải nhận thức", "Giao diện tốt giảm nhớ, giảm lựa chọn thừa và giảm chuyển ngữ cảnh.", "Có thể bỏ hoặc nhóm thông tin nào?"),
            ("Lỗi người dùng", "Lỗi là dữ liệu về điểm hệ thống không phù hợp con người.", "Lỗi này có thể được ngăn trước không?"),
            ("An toàn", "Hệ rủi ro cao cần xác nhận, undo, cảnh báo đúng lúc và fail-safe.", "Nếu người dùng sai, hệ thống bảo vệ thế nào?"),
            ("AI interaction", "AI cần minh bạch về giới hạn, nguồn, bất định và quyền quyết định của con người.", "Người dùng có biết khi nào không nên tin AI không?"),
            ("Đo UX", "UX phải được kiểm bằng hành vi thật, không chỉ ý kiến.", "Người dùng có hoàn thành việc trong bối cảnh thật không?"),
        ],
        "tools": [
            ("UX risk review", ["Tác vụ chính:", "Người dùng:", "Bối cảnh:", "Điểm dễ sai:", "Hậu quả:", "Feedback:", "Undo/fail-safe:", "Metric:"]),
            ("Heuristic check", ["Rõ trạng thái hệ thống?", "Ngôn ngữ quen thuộc?", "Có undo?", "Nhất quán?", "Giảm nhớ?", "Thông báo lỗi hữu ích?", "Có kiểm thử với người thật?"]),
        ],
        "final": "Thiết kế tốt là khi hệ thống đủ hiểu con người để người dùng không phải gồng mình hiểu hệ thống.",
    },
    {
        "n": 58,
        "file": "Tap-58-Tam-ly-truyen-thong-tin-gia-va-anh-huong-dai-chung.md",
        "title": "Tâm Lý Truyền Thông, Tin Giả Và Ảnh Hưởng Đại Chúng",
        "subtitle": "Hiểu framing, lan truyền, cảm xúc đám đông, tin giả, thuật toán, niềm tin và trách nhiệm truyền thông",
        "core": "Truyền thông không chỉ chuyển thông tin; nó định khung chú ý, cảm xúc, niềm tin và hành vi của đám đông.",
        "why": [
            "Lãnh đạo cần hiểu cách thông tin lan truyền trong tổ chức và xã hội.",
            "Tin giả đánh vào cảm xúc, bản sắc và tốc độ chia sẻ trước khi lý trí kiểm chứng.",
            "Thuật toán làm thông tin không còn trung lập về mặt chú ý.",
            "Truyền thông có đạo đức là làm người khác rõ hơn, không chỉ phản ứng mạnh hơn.",
        ],
        "pillars": [
            ("Framing", "Cách đặt khung quyết định cảm xúc và cách hiểu dữ kiện.", "Khung này làm người nghe thấy vấn đề là gì?"),
            ("Lan truyền cảm xúc", "Thông tin kích hoạt sợ hãi, phẫn nộ hoặc hy vọng thường lan nhanh.", "Cảm xúc nào đang kéo lượt chia sẻ?"),
            ("Tin giả", "Tin giả sống bằng sự hợp ý, tốc độ và thiếu kiểm chứng.", "Tôi muốn tin điều này vì nó đúng hay vì nó hợp phe?"),
            ("Thuật toán", "Nền tảng tối ưu chú ý, không tự động tối ưu sự thật.", "Hệ thống đang thưởng nội dung nào?"),
            ("Niềm tin cộng đồng", "Truyền thông kém làm mất niềm tin lâu dài.", "Thông điệp này có làm niềm tin xã hội tốt hơn không?"),
            ("Khủng hoảng truyền thông", "Khủng hoảng cần sự thật, tốc độ, trách nhiệm và hành động sửa.", "Điều gì phải nói ngay, điều gì cần xác minh?"),
            ("Đạo đức ảnh hưởng", "Ảnh hưởng đúng tăng hiểu biết; tuyên truyền xấu giảm tự chủ.", "Tôi có đang che dữ kiện để thắng cảm xúc không?"),
        ],
        "tools": [
            ("Fact-check nhanh", ["Nguồn gốc:", "Bằng chứng:", "Nguồn độc lập:", "Cảm xúc bị kích hoạt:", "Ai được lợi:", "Có nên chia sẻ không:"]),
            ("Thông điệp khủng hoảng", ["Sự thật đã biết:", "Điều chưa biết:", "Người bị ảnh hưởng:", "Trách nhiệm:", "Hành động đang làm:", "Cập nhật tiếp theo:"]),
        ],
        "final": "Trong thời đại dư thông tin, người trưởng thành không chỉ hỏi tin này có hấp dẫn không, mà hỏi nó có làm mình gần sự thật hơn không.",
    },
    {
        "n": 59,
        "file": "Tap-59-Tam-ly-tich-cuc-hanh-phuc-strengths-resilience-flourishing.md",
        "title": "Tâm Lý Tích Cực: Hạnh Phúc, Strengths, Resilience Và Flourishing",
        "subtitle": "Hiểu đời sống tốt đẹp không chỉ là hết bệnh: điểm mạnh, ý nghĩa, quan hệ, thành tựu, biết ơn và khả năng phục hồi",
        "core": "Tâm lý tích cực trưởng thành không phủ nhận đau khổ; nó nghiên cứu điều làm con người sống có sức mạnh, ý nghĩa và chất lượng hơn.",
        "why": [
            "Người thành công vẫn có thể trống rỗng nếu chỉ tối ưu thành tích.",
            "Tổ chức khỏe cần không chỉ giảm burnout mà còn tăng meaning, mastery và belonging.",
            "Tích cực giả nguy hiểm vì phủ nhận đau khổ; tích cực khoa học nhìn cả nguồn lực và thực tế.",
            "Đây là phần cân bằng giữa chữa lành và phát triển.",
        ],
        "pillars": [
            ("Well-being", "Hạnh phúc bền gồm cảm xúc tích cực, ý nghĩa, quan hệ, dấn thân và thành tựu.", "Đời sống tôi đang thiếu trụ nào?"),
            ("Strengths", "Điểm mạnh là năng lực tự nhiên tạo năng lượng và giá trị khi dùng đúng bối cảnh.", "Điểm mạnh nào tôi dùng quá mức hoặc thiếu mức?"),
            ("Resilience", "Phục hồi là khả năng quay lại và học sau nghịch cảnh.", "Nguồn lực nào giúp tôi đứng dậy?"),
            ("Biết ơn", "Biết ơn huấn luyện chú ý thấy điều đang có thay vì chỉ thiếu.", "Tôi đang xem điều gì là hiển nhiên?"),
            ("Flow", "Flow là trạng thái dấn thân sâu khi thử thách và kỹ năng cân bằng.", "Việc nào làm tôi sống động hơn?"),
            ("Ý nghĩa", "Ý nghĩa đến từ giá trị, đóng góp, quan hệ và câu chuyện đời sống.", "Điều gì đáng để tôi chịu khó?"),
            ("Tích cực giả", "Tích cực giả phủ nhận đau khổ và làm người khác xấu hổ vì chưa ổn.", "Tôi đang nâng đỡ hay đang bắt người khác phải vui?"),
        ],
        "tools": [
            ("PERMA review", ["Positive emotion:", "Engagement:", "Relationships:", "Meaning:", "Achievement:", "Trụ yếu nhất:", "Hành động 7 ngày:"]),
            ("Strengths audit", ["Điểm mạnh:", "Khi dùng tốt:", "Khi dùng quá mức:", "Bối cảnh phù hợp:", "Cách dùng để phục vụ người khác:"]),
        ],
        "final": "Sống tốt không phải lúc nào cũng vui; đó là có đủ nguồn lực, quan hệ và ý nghĩa để sống thật qua cả lúc vui lẫn lúc khó.",
    },
    {
        "n": 60,
        "file": "Tap-60-Tam-ly-thuc-nghiem-va-tu-duy-khoa-hoc-khi-hieu-con-nguoi.md",
        "title": "Tâm Lý Thực Nghiệm Và Tư Duy Khoa Học Khi Hiểu Con Người",
        "subtitle": "Hiểu giả thuyết, thí nghiệm, tương quan, nhân quả, effect size, replication, bias và cách ứng dụng nghiên cứu thận trọng",
        "core": "Tư duy khoa học trong tâm lý là kỷ luật không tin quá nhanh vào trực giác, câu chuyện hay một nghiên cứu đơn lẻ.",
        "why": [
            "Tâm lý học dễ bị đơn giản hóa thành mẹo, trào lưu và khẳng định quá mức.",
            "C-level cần biết đọc nghiên cứu để không mua sai mô hình hoặc can thiệp kém bằng chứng.",
            "Thực nghiệm giúp phân biệt điều nghe hợp lý với điều thật sự tạo khác biệt.",
            "Tập này là lớp bảo hiểm chống lạm dụng tâm lý học.",
        ],
        "pillars": [
            ("Giả thuyết", "Giả thuyết tốt có thể kiểm chứng và có khả năng bị bác bỏ.", "Điều tôi tin có thể bị chứng minh sai không?"),
            ("Tương quan", "Hai biến đi cùng nhau không chứng minh biến này gây ra biến kia.", "Có biến thứ ba nào giải thích cả hai không?"),
            ("Nhân quả", "Nhân quả cần thiết kế kiểm soát, so sánh và loại trừ giải thích khác.", "Thiết kế nào cho phép nói về nguyên nhân?"),
            ("Effect size", "Ý nghĩa thống kê không đồng nghĩa tác động thực tế lớn.", "Hiệu ứng này lớn đủ để đáng áp dụng không?"),
            ("Replication", "Kết quả đáng tin hơn khi được lặp lại bởi nhóm độc lập.", "Kết quả này đã được lặp lại chưa?"),
            ("Bias nghiên cứu", "Mẫu, đo lường, phân tích và công bố đều có thể tạo lệch.", "Mẫu nghiên cứu có giống bối cảnh của tôi không?"),
            ("Ứng dụng thận trọng", "Nghiên cứu tạo giả thuyết ứng dụng, không thay thế đo trong bối cảnh thật.", "Tôi sẽ thử nhỏ và đo lại thế nào?"),
        ],
        "tools": [
            ("Research reading checklist", ["Câu hỏi nghiên cứu:", "Mẫu:", "Thiết kế:", "Đo lường:", "Kết quả:", "Effect size:", "Giới hạn:", "Ứng dụng thận trọng:"]),
            ("Thử nghiệm tổ chức", ["Giả thuyết:", "Nhóm thử:", "Nhóm so sánh:", "Chỉ số:", "Thời gian:", "Rủi ro đạo đức:", "Tiêu chí dừng/scale:"]),
        ],
        "final": "Hiểu con người bằng khoa học là biết nghi ngờ chính điều mình rất muốn tin.",
    },
]


REFERENCES = [
    ("APA Psychology Topics", "https://www.apa.org/topics/"),
    ("OpenStax Psychology 2e", "https://openstax.org/books/psychology-2e/pages/index"),
    ("Noba Project - Introduction to Psychology", "https://nobaproject.com/textbooks/introduction-to-psychology-the-full-noba-collection"),
    ("MIT OpenCourseWare - Introduction to Psychology", "https://ocw.mit.edu/courses/9-00-introduction-to-psychology-fall-2004/"),
]


def render_table(rows: list[tuple[str, str, str]]) -> str:
    out = ["| Thành phần | Bản chất | Câu hỏi ứng dụng |", "|---|---|---|"]
    for a, b, c in rows:
        out.append(f"| {a} | {b} | {c} |")
    return "\n".join(out)


def render_tap(tap: dict) -> str:
    n = tap["n"]
    lines: list[str] = [
        f"# Tập {n}: {tap['title']}",
        "",
        f"**{tap['subtitle']}**",
        "",
        "**Giáo trình ngắn gọn, trực quan, first principles, dành cho người trưởng thành và lãnh đạo cấp cao.**",
        "",
        "---",
        "",
        f"## 0. Vì Sao C-level Cần Học {tap['title']}?",
        "",
    ]
    for item in tap["why"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        f"**Một câu cần nhớ:** {tap['core']}",
        "",
        "**Mục tiêu tập này:** sau khi học xong, bạn có một mô hình thực dụng để quan sát, kiểm chứng và áp dụng chủ đề này trong đời sống thật.",
        "",
        "---",
        "",
        "## 1. First Principles: Bản Chất Cốt Lõi",
        "",
        f"**Bản chất:** {tap['core']}",
        "",
        "| Lớp cần nhìn | Câu hỏi | Ý nghĩa thực tiễn |",
        "|---|---|---|",
        "| Cơ chế | Điều gì đang vận hành bên trong? | Tránh chỉ nhìn bề mặt. |",
        "| Bối cảnh | Môi trường nào đang tác động? | Hành vi không tách khỏi hệ thống. |",
        "| Bằng chứng | Dữ kiện nào kiểm chứng được? | Giảm suy diễn và cảm tính. |",
        "| Đạo đức | Can thiệp này có làm người khác rõ hơn và tự chủ hơn không? | Tránh thao túng. |",
        "",
        "```text",
        "Câu hỏi gốc:",
        "1. Hiện tượng thật là gì?",
        "2. Tầng nào đang bị bỏ sót?",
        "3. Dữ kiện nào ủng hộ hoặc phản biện?",
        "4. Can thiệp nhỏ nhất, đo được là gì?",
        "```",
        "",
        "---",
        "",
    ])

    for idx, (title, essence, question) in enumerate(tap["pillars"], 2):
        lines.extend([
            f"## {idx}. {title}",
            "",
            "### Bản chất",
            "",
            essence,
            "",
            render_table([
                ("Dấu hiệu", "Hành vi, cảm xúc hoặc mô hình lặp lại", "Tôi đang thấy tín hiệu nào?"),
                ("Rủi ro hiểu sai", "Đơn giản hóa một hiện tượng nhiều tầng", "Tôi có đang kết luận quá nhanh không?"),
                ("Ứng dụng", "Đổi câu hỏi, môi trường, phản hồi hoặc ranh giới", "Can thiệp nhỏ nhất là gì?"),
            ]),
            "",
            "```text",
            "Câu hỏi ứng dụng:",
            f"- {question}",
            "- Dữ kiện nào có thể kiểm chứng?",
            "- Nếu áp dụng sai, ai chịu chi phí?",
            "```",
            "",
            f"**Nguyên tắc:** {title} chỉ hữu ích khi được dùng để làm con người rõ hơn, tự chủ hơn và bớt bị hệ thống vô thức kéo đi.",
            "",
            "---",
            "",
        ])

    lines.extend([f"## {len(tap['pillars']) + 2}. Công Cụ Thực Hành", ""])
    for tool_name, fields in tap["tools"]:
        lines.extend([f"### {tool_name}", "", "```text"])
        lines.extend(fields)
        lines.extend(["```", ""])

    lines.extend([
        "---",
        "",
        f"## {len(tap['pillars']) + 3}. Lộ Trình Thực Hành 4 Tuần",
        "",
        "| Tuần | Trọng tâm | Việc làm cụ thể |",
        "|---|---|---|",
        "| 1 | Quan sát | Chọn một tình huống thật và ghi lại dữ kiện, cảm xúc, hành vi. |",
        "| 2 | Gọi tên | Dùng khái niệm trong tập để đặt tên đúng lực tâm lý. |",
        "| 3 | Can thiệp nhỏ | Thay một câu hỏi, một thiết kế môi trường hoặc một nhịp phản hồi. |",
        "| 4 | Review | Đo lại kết quả, rủi ro và điều cần học tiếp. |",
        "",
        "---",
        "",
        f"## {len(tap['pillars']) + 4}. Bảng Tóm Tắt First Principles",
        "",
        "| Khái niệm | Bản chất | Câu hỏi cần nhớ |",
        "|---|---|---|",
    ])
    for title, essence, question in tap["pillars"]:
        lines.append(f"| {title} | {essence} | {question} |")

    lines.extend([
        "",
        "---",
        "",
        f"## {len(tap['pillars']) + 5}. Tài Liệu Tham Khảo Gợi Ý",
        "",
    ])
    for label, url in REFERENCES:
        lines.append(f"- [{label}]({url})")

    lines.extend([
        "",
        "---",
        "",
        f"## {len(tap['pillars']) + 6}. Một Câu Để Nhớ Toàn Bộ Tập {n}",
        "",
        f"> {tap['final']}",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    for tap in TAPS:
        path = ROOT / tap["file"]
        path.write_text(render_tap(tap), encoding="utf-8")
        print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
