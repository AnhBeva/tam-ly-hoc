from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent


TAPS = [
    {
        "n": 41,
        "file": "Tap-41-Tam-ly-hoc-chinh-tri-va-y-thuc-he.md",
        "title": "Tâm Lý Học Chính Trị Và Ý Thức Hệ",
        "subtitle": "Hiểu vì sao con người chọn phe, bảo vệ niềm tin, sợ hỗn loạn, theo lãnh tụ và biến ý kiến thành bản sắc",
        "core": "Chính trị không chỉ là chính sách; nó là cảm xúc, bản sắc, lợi ích, nỗi sợ và nhu cầu thuộc về được tổ chức thành phe.",
        "why": [
            "Lãnh đạo phải hiểu quyền lực xã hội, niềm tin tập thể và xung đột phe nhóm.",
            "Người thông minh vẫn có thể phi lý khi ý kiến đã dính vào bản sắc.",
            "Ý thức hệ giúp con người đơn giản hóa thế giới, nhưng cũng dễ làm họ mù trước dữ kiện trái ý.",
            "Hiểu tâm lý chính trị giúp đọc xã hội, tổ chức và truyền thông tỉnh táo hơn.",
        ],
        "pillars": [
            ("Bản sắc chính trị", "Khi quan điểm trở thành tôi là ai, phản biện bị cảm nhận như tấn công cá nhân.", "Người này đang bảo vệ dữ kiện hay bảo vệ danh tính?"),
            ("Nhu cầu trật tự", "Con người sợ hỗn loạn nên dễ chọn hệ tư tưởng hứa hẹn chắc chắn.", "Niềm tin này giảm bất định bằng sự thật hay bằng ảo tưởng?"),
            ("Thuộc về phe", "Phe nhóm cho an toàn, ngôn ngữ chung và cảm giác mình không đơn độc.", "Tôi có đang đồng ý để được thuộc về không?"),
            ("Lãnh tụ và biểu tượng", "Lãnh tụ mạnh thường trở thành biểu tượng chứa hy vọng, sợ hãi và phẫn nộ của nhóm.", "Tôi đang nhìn con người thật hay biểu tượng tôi cần tin?"),
            ("Kẻ thù chung", "Nhóm dễ đoàn kết khi có đối tượng để đổ lỗi.", "Ai được lợi khi mọi người cùng ghét một kẻ thù?"),
            ("Tuyên truyền và framing", "Cách đặt khung quyết định cảm xúc trước khi lý trí phân tích.", "Cùng một dữ kiện sẽ khác thế nào nếu đổi cách gọi tên?"),
            ("Cực hóa", "Cực hóa tăng khi con người chỉ sống trong buồng vang đồng quan điểm.", "Tôi còn tiếp xúc với người tử tế nhưng nghĩ khác mình không?"),
        ],
        "tools": [
            ("Bản đồ niềm tin chính trị", ["Niềm tin tôi đang giữ:", "Nỗi sợ phía sau:", "Nhóm tôi thuộc về:", "Dữ kiện tôi né:", "Điều đối phương đúng một phần:", "Cách thảo luận trưởng thành hơn:"]),
            ("Kiểm tra phe nhóm", ["Phe này thưởng điều gì?", "Phe này phạt điều gì?", "Ai không được nói?", "Kẻ thù chung là ai?", "Sự thật nào bị đơn giản hóa?"]),
        ],
        "final": "Muốn hiểu chính trị, đừng bắt đầu từ khẩu hiệu; hãy bắt đầu từ nỗi sợ, bản sắc, lợi ích và nhu cầu thuộc về.",
    },
    {
        "n": 42,
        "file": "Tap-42-Tam-ly-hoc-suc-khoe-va-tam-than.md",
        "title": "Tâm Lý Học Sức Khỏe Và Tâm-Thân",
        "subtitle": "Hiểu stress, giấc ngủ, đau mạn tính, hành vi sức khỏe, bệnh tật và mối liên hệ hai chiều giữa tâm trí và cơ thể",
        "core": "Tâm trí và cơ thể không phải hai hệ tách rời; cảm xúc đổi sinh lý, sinh lý đổi suy nghĩ, thói quen đổi cả hai.",
        "why": [
            "Hiệu suất lãnh đạo phụ thuộc trực tiếp vào năng lượng, hồi phục và sức khỏe thần kinh.",
            "Stress kéo dài làm suy giảm quyết định, cảm xúc, miễn dịch và quan hệ.",
            "Nhiều vấn đề sức khỏe không chỉ cần biết đúng, mà cần thiết kế hành vi đúng.",
            "Hiểu tâm-thân giúp phân biệt tự chăm sóc thực chất với ép cơ thể phục vụ tham vọng.",
        ],
        "pillars": [
            ("Stress sinh tồn", "Stress là hệ thống huy động năng lượng; hữu ích ngắn hạn, phá hủy khi kéo dài.", "Tôi đang dùng cơ thể như tài sản hay như khoản vay?"),
            ("Giấc ngủ", "Ngủ là nền tảng của trí nhớ, cảm xúc, miễn dịch và tự kiểm soát.", "Vấn đề này sẽ khác thế nào nếu tôi ngủ đủ 7 ngày?"),
            ("Đau và cảm xúc", "Đau không chỉ là tín hiệu mô; nó được não khuếch đại hoặc giảm theo sợ hãi, chú ý và an toàn.", "Tôi đang làm đau tăng vì chống lại hay vì hiểu sai nó?"),
            ("Hành vi sức khỏe", "Con người không thay đổi vì biết, mà vì môi trường làm hành vi đúng dễ hơn.", "Hành vi khỏe mạnh nào cần được làm mặc định?"),
            ("Ăn uống và năng lượng", "Ăn uống ảnh hưởng đường huyết, tâm trạng, tập trung và kiểm soát xung động.", "Tôi đang ăn để nuôi năng lượng hay để điều tiết cảm xúc?"),
            ("Bệnh tật và danh tính", "Bệnh có thể làm con người mất vai trò, mất kiểm soát và phải tái định nghĩa bản thân.", "Nếu sức khỏe đổi, tôi còn là ai ngoài năng suất?"),
            ("Hồi phục", "Hồi phục là năng lực chiến lược, không phải phần thưởng sau khi kiệt sức.", "Lịch của tôi có chỗ cho phục hồi thật không?"),
        ],
        "tools": [
            ("Audit năng lượng", ["Giấc ngủ:", "Vận động:", "Ăn uống:", "Stress chính:", "Dấu hiệu cơ thể:", "Một thay đổi nhỏ tuần này:"]),
            ("Thiết kế hành vi sức khỏe", ["Hành vi muốn có:", "Cản trở:", "Tín hiệu kích hoạt:", "Phiên bản 2 phút:", "Môi trường hỗ trợ:", "Cách đo:"]),
        ],
        "final": "Cơ thể là nền vận hành của tâm trí; coi thường cơ thể là làm hỏng hệ điều hành của mọi quyết định.",
    },
    {
        "n": 43,
        "file": "Tap-43-Tam-ly-hoc-phap-ly-va-toi-pham.md",
        "title": "Tâm Lý Học Pháp Lý Và Tội Phạm",
        "subtitle": "Hiểu lời khai, ký ức, động cơ phạm lỗi, rủi ro tái phạm, công lý, trừng phạt và phục hồi",
        "core": "Hành vi sai trái sinh ra từ lựa chọn cá nhân trong bối cảnh động cơ, cơ hội, kiểm soát xung động, nhóm và hệ quả được cảm nhận.",
        "why": [
            "C-level cần hiểu gian lận, vi phạm đạo đức và hành vi nguy hiểm trong tổ chức.",
            "Ký ức và lời khai không phải bản ghi video; chúng dễ bị bóp méo bởi áp lực và gợi ý.",
            "Trừng phạt không đủ nếu hệ thống vẫn thưởng hành vi sai.",
            "Hiểu pháp lý-tội phạm giúp thiết kế kiểm soát, công bằng và phục hồi tốt hơn.",
        ],
        "pillars": [
            ("Ký ức nhân chứng", "Ký ức là tái dựng, không phải ghi hình; câu hỏi dẫn dắt có thể làm nó đổi.", "Ta đang hỏi để tìm sự thật hay để xác nhận giả thuyết?"),
            ("Động cơ phạm lỗi", "Sai trái thường đến từ áp lực, cơ hội và tự biện minh gặp nhau.", "Hệ thống đang tạo áp lực và cơ hội sai ở đâu?"),
            ("Kiểm soát xung động", "Một số hành vi nguy hiểm tăng khi não điều hành yếu, cảm xúc mạnh hoặc chất kích thích hiện diện.", "Điểm nóng nào cần giảm trước khi cần phạt?"),
            ("Gian lận tổ chức", "Gian lận hiếm khi bắt đầu bằng tôi là người xấu; nó bắt đầu bằng lần ngoại lệ có lý do.", "Ngoại lệ nào đang được hợp lý hóa?"),
            ("Công lý và phục hồi", "Công lý trưởng thành vừa bảo vệ nạn nhân, vừa giảm khả năng hại lặp lại.", "Cách xử lý này làm hệ thống an toàn hơn hay chỉ hả giận?"),
            ("Rủi ro tái phạm", "Rủi ro giảm khi động cơ, môi trường, kỹ năng và giám sát đều đổi.", "Nếu người này quay lại cùng môi trường cũ, điều gì sẽ khác?"),
            ("Đạo đức điều tra", "Tìm sự thật cần quy trình, không thể dựa vào trực giác tự tin.", "Quy trình có bảo vệ người vô tội và người bị hại không?"),
        ],
        "tools": [
            ("Tam giác gian lận", ["Áp lực:", "Cơ hội:", "Tự biện minh:", "Kiểm soát còn thiếu:", "Tín hiệu cảnh báo:", "Hành động giảm rủi ro:"]),
            ("Khung xử lý vi phạm", ["Sự kiện:", "Bằng chứng:", "Người bị ảnh hưởng:", "Mức độ cố ý:", "Rủi ro lặp lại:", "Biện pháp bảo vệ:"]),
        ],
        "final": "Muốn giảm sai trái, đừng chỉ hỏi ai xấu; hãy hỏi hệ thống nào đang biến sai trái thành lựa chọn dễ xảy ra.",
    },
    {
        "n": 44,
        "file": "Tap-44-Tam-ly-hoc-the-thao-va-hieu-suat-dinh-cao.md",
        "title": "Tâm Lý Học Thể Thao Và Hiệu Suất Đỉnh Cao",
        "subtitle": "Hiểu tập luyện tinh thần, áp lực thi đấu, flow, phục hồi, mục tiêu, kỷ luật và hiệu suất bền vững",
        "core": "Hiệu suất đỉnh cao không phải lúc nào cũng cố hơn; nó là chu kỳ đúng giữa tập trung, luyện tập, phản hồi, hồi phục và bản lĩnh dưới áp lực.",
        "why": [
            "Thể thao là phòng thí nghiệm rõ nhất về hiệu suất, áp lực và hồi phục.",
            "Lãnh đạo cũng phải trình diễn trong điều kiện rủi ro cao, quan sát nhiều và cảm xúc mạnh.",
            "Người giỏi dễ đốt mình vì nhầm căng thẳng liên tục với cam kết.",
            "Hiểu hiệu suất giúp thiết kế nhịp làm việc bền vững cho cá nhân và đội ngũ.",
        ],
        "pillars": [
            ("Mục tiêu và quy trình", "Kết quả tạo hướng, quy trình tạo kiểm soát hằng ngày.", "Tôi đang kiểm soát hành vi hay ám ảnh bảng điểm?"),
            ("Áp lực thi đấu", "Áp lực làm hẹp chú ý; bản lĩnh là giữ được việc cần làm ngay bây giờ.", "Trong áp lực, tín hiệu neo chú ý của tôi là gì?"),
            ("Flow", "Flow xuất hiện khi kỹ năng gặp thử thách vừa tầm và phản hồi rõ.", "Việc nào đang quá dễ, quá khó hoặc vừa đủ?"),
            ("Tập luyện có chủ đích", "Tiến bộ đến từ luyện phần yếu cụ thể với phản hồi nhanh.", "Kỹ năng nhỏ nào nếu cải thiện sẽ đổi kết quả lớn?"),
            ("Tự thoại", "Lời nói bên trong có thể ổn định hoặc phá hủy hệ thần kinh.", "Câu tôi nói với mình dưới áp lực là gì?"),
            ("Phục hồi", "Không phục hồi thì luyện tập biến thành hao mòn.", "Tôi có đo phục hồi nghiêm túc như đo thành tích không?"),
            ("Đội ngũ hiệu suất cao", "Đội mạnh có vai trò rõ, niềm tin, chuẩn cao và an toàn để sửa lỗi.", "Đội đang tránh lỗi hay học từ lỗi?"),
        ],
        "tools": [
            ("Routine trước áp lực", ["Tình huống áp lực:", "Dấu hiệu cơ thể:", "Câu tự thoại:", "Hơi thở/neo chú ý:", "Hành động đầu tiên:", "Cách review sau đó:"]),
            ("Bảng luyện tập có chủ đích", ["Kỹ năng:", "Điểm yếu cụ thể:", "Bài tập:", "Phản hồi:", "Tần suất:", "Chỉ số tiến bộ:"]),
        ],
        "final": "Hiệu suất cao bền vững là nghệ thuật biết lúc nào ép, lúc nào sửa, lúc nào nghỉ và lúc nào chỉ cần làm đúng động tác kế tiếp.",
    },
    {
        "n": 45,
        "file": "Tap-45-Tam-ly-hoc-nghe-thuat-bieu-tuong-va-cau-chuyen.md",
        "title": "Tâm Lý Học Nghệ Thuật, Biểu Tượng Và Câu Chuyện",
        "subtitle": "Hiểu vì sao hình ảnh, âm nhạc, nghi lễ, biểu tượng và narrative có thể chạm sâu hơn lý lẽ",
        "core": "Con người không chỉ sống bằng dữ kiện; con người sống bằng câu chuyện, biểu tượng và cảm xúc giúp họ biết mình là ai.",
        "why": [
            "Lãnh đạo cần truyền ý nghĩa, không chỉ truyền KPI.",
            "Biểu tượng có thể kết nối nhanh với tầng cảm xúc và bản sắc.",
            "Câu chuyện giúp não nhớ, cảm và hành động tốt hơn bảng dữ liệu khô.",
            "Hiểu nghệ thuật giúp xây văn hóa, thương hiệu và thông điệp có chiều sâu.",
        ],
        "pillars": [
            ("Câu chuyện", "Câu chuyện biến sự kiện rời rạc thành ý nghĩa có hướng.", "Câu chuyện này làm con người thấy mình là ai?"),
            ("Biểu tượng", "Biểu tượng nén nhiều ý nghĩa vào một hình ảnh, nghi thức hoặc vật thể.", "Biểu tượng nào đang đại diện cho giá trị thật?"),
            ("Cảm xúc thẩm mỹ", "Cái đẹp làm con người mở ra, chú ý sâu hơn và nhớ lâu hơn.", "Trải nghiệm này làm người xem cảm gì trước khi hiểu gì?"),
            ("Nghi lễ", "Nghi lễ biến giá trị trừu tượng thành hành động lặp lại có ý nghĩa.", "Giá trị quan trọng nào cần một nghi lễ cụ thể?"),
            ("Ẩn dụ", "Ẩn dụ giúp hiểu điều phức tạp qua điều quen thuộc.", "Ẩn dụ nào đang dẫn suy nghĩ của tôi?"),
            ("Thương hiệu như myth", "Thương hiệu mạnh không chỉ nói tính năng; nó nói vai trò khách hàng muốn trở thành.", "Khách hàng muốn trở thành ai khi chọn mình?"),
            ("Câu chuyện giả", "Narrative nguy hiểm khi nó đẹp hơn sự thật và che hành vi xấu.", "Câu chuyện này soi sáng hay che đậy thực tế?"),
        ],
        "tools": [
            ("Canvas câu chuyện", ["Nhân vật:", "Vấn đề:", "Lực cản:", "Chuyển hóa:", "Giá trị:", "Hành động muốn tạo:"]),
            ("Audit biểu tượng văn hóa", ["Biểu tượng/nghi lễ:", "Ý nghĩa tuyên bố:", "Hành vi thật:", "Cảm xúc tạo ra:", "Điều cần giữ/sửa:"]),
        ],
        "final": "Dữ kiện thuyết phục trí óc, nhưng câu chuyện và biểu tượng mới thường làm con người nhớ, tin và bước đi cùng nhau.",
    },
    {
        "n": 46,
        "file": "Tap-46-Tam-ly-hoc-moi-truong-va-khong-gian-song.md",
        "title": "Tâm Lý Học Môi Trường Và Không Gian Sống",
        "subtitle": "Hiểu cách ánh sáng, tiếng ồn, mật độ, thiên nhiên, bố cục và không gian làm đổi cảm xúc, hành vi và quan hệ",
        "core": "Không gian là một hệ điều khiển hành vi thầm lặng: nó làm một số lựa chọn dễ hơn, một số cảm xúc mạnh hơn và một số quan hệ gần hoặc xa hơn.",
        "why": [
            "Con người không chỉ bị ảnh hưởng bởi ý chí, mà bởi môi trường bao quanh mỗi ngày.",
            "Văn phòng, nhà ở và thành phố có thể tăng hoặc giảm stress, tập trung và kết nối.",
            "Thiết kế không gian tốt là thiết kế hành vi không cần nhắc nhở liên tục.",
            "C-level ra quyết định về văn phòng, nhịp làm việc và môi trường sống của nhiều người.",
        ],
        "pillars": [
            ("Ánh sáng", "Ánh sáng ảnh hưởng nhịp sinh học, tỉnh táo, tâm trạng và giấc ngủ.", "Không gian này đang giúp hay phá nhịp sinh học?"),
            ("Tiếng ồn", "Tiếng ồn làm não cảnh giác, giảm tập trung và tăng kích thích.", "Việc nào cần yên tĩnh thật sự?"),
            ("Mật độ và riêng tư", "Quá đông làm tăng phòng vệ; quá cô lập làm giảm kết nối.", "Không gian này cho con người quyền gần và quyền lui chưa?"),
            ("Thiên nhiên", "Yếu tố tự nhiên giúp phục hồi chú ý và giảm stress.", "Mỗi ngày tôi có điểm chạm với thiên nhiên không?"),
            ("Bố cục hành vi", "Vị trí đồ vật quyết định hành vi mặc định nhiều hơn ý chí.", "Hành vi tốt đã được đặt trong tầm tay chưa?"),
            ("Không gian quyền lực", "Bàn ghế, cửa, khoảng cách và phòng họp truyền tín hiệu địa vị.", "Không gian này làm người khác dám nói thật hay thu mình?"),
            ("Nhà như hệ phục hồi", "Nhà không chỉ để ở; nó phải giúp hệ thần kinh trở về an toàn.", "Nhà tôi đang phục hồi hay tiếp tục kích thích tôi?"),
        ],
        "tools": [
            ("Audit không gian", ["Không gian:", "Cảm xúc khi bước vào:", "Hành vi được khuyến khích:", "Hành vi bị cản:", "Yếu tố gây stress:", "Một chỉnh sửa nhỏ:"]),
            ("Thiết kế môi trường hành vi", ["Hành vi muốn tăng:", "Tín hiệu môi trường:", "Vật cản cần bỏ:", "Vị trí mới:", "Cách đo thay đổi:"]),
        ],
        "final": "Muốn đổi hành vi bền, đừng chỉ huấn luyện con người; hãy sửa môi trường đang âm thầm huấn luyện họ mỗi ngày.",
    },
    {
        "n": 47,
        "file": "Tap-47-Tam-ly-hoc-cong-dong-va-chua-lanh-tap-the.md",
        "title": "Tâm Lý Học Cộng Đồng Và Chữa Lành Tập Thể",
        "subtitle": "Hiểu niềm tin xã hội, vốn xã hội, mất mát tập thể, phân cực, nghi lễ chữa lành và sức mạnh cộng đồng",
        "core": "Con người không chữa lành một mình hoàn toàn; nhiều vết thương và nguồn lực nằm trong cộng đồng, ký ức chung và cách xã hội đối xử với nhau.",
        "why": [
            "Tổ chức và xã hội có sang chấn, mất niềm tin và ký ức tập thể.",
            "Cộng đồng mạnh giúp con người chịu khủng hoảng tốt hơn cá nhân đơn độc.",
            "Lãnh đạo cần biết hàn gắn niềm tin sau xung đột, sa thải, khủng hoảng hoặc bất công.",
            "Chữa lành tập thể không phải khẩu hiệu cảm xúc; nó cần sự thật, công nhận, sửa chữa và nghi lễ.",
        ],
        "pillars": [
            ("Vốn xã hội", "Niềm tin, mạng lưới và chuẩn hợp tác giúp cộng đồng vận hành ít tốn năng lượng hơn.", "Niềm tin đang được tích lũy hay tiêu hao?"),
            ("Sang chấn tập thể", "Biến cố chung có thể để lại cảnh giác, im lặng và chia rẽ qua nhiều năm.", "Cộng đồng này đã trải qua điều gì chưa được gọi tên?"),
            ("Công nhận nỗi đau", "Không công nhận làm vết thương chuyển thành cay đắng hoặc hoài nghi.", "Ai cần được nghe rằng điều họ chịu là có thật?"),
            ("Sửa chữa", "Xin lỗi không đủ nếu không có thay đổi hành vi, trách nhiệm và bồi đắp niềm tin.", "Hành động nào chứng minh hệ thống đã học?"),
            ("Nghi lễ cộng đồng", "Nghi lễ giúp con người đánh dấu mất mát, chuyển giai đoạn và tái cam kết.", "Cột mốc nào cần được đánh dấu tử tế?"),
            ("Phân cực xã hội", "Phân cực tăng khi nhóm mất tiếp xúc nhân tính của nhau.", "Làm sao tạo tiếp xúc an toàn mà không phủ nhận khác biệt?"),
            ("Lãnh đạo cộng đồng", "Lãnh đạo chữa lành là người giữ sự thật và hy vọng cùng lúc.", "Tôi có đang trấn an quá nhanh trước khi nghe đủ không?"),
        ],
        "tools": [
            ("Bản đồ niềm tin cộng đồng", ["Cộng đồng:", "Niềm tin đã mất:", "Sự kiện gốc:", "Nhóm bị ảnh hưởng:", "Sự thật cần nói:", "Hành động sửa chữa:"]),
            ("Thiết kế nghi lễ chuyển hóa", ["Mất mát/cột mốc:", "Ai tham gia:", "Điều cần công nhận:", "Biểu tượng:", "Cam kết mới:", "Hành động sau nghi lễ:"]),
        ],
        "final": "Cộng đồng không hồi phục bằng quên đi; cộng đồng hồi phục khi sự thật được nói, nỗi đau được công nhận và hành vi mới được duy trì.",
    },
    {
        "n": 48,
        "file": "Tap-48-Tam-ly-hoc-giao-duc-gia-dinh-va-nuoi-day-con-sau.md",
        "title": "Tâm Lý Học Giáo Dục Gia Đình Và Nuôi Dạy Con Sâu",
        "subtitle": "Hiểu gắn bó, kỷ luật, tự chủ, học tập, kỳ vọng, giá trị gia đình và cách nuôi con thành người vững bên trong",
        "core": "Nuôi dạy con là quá trình xây hệ thần kinh, bản sắc, năng lực tự chủ và cảm giác được yêu mà vẫn có giới hạn.",
        "why": [
            "Người thành công dễ vô tình biến con thành dự án hoặc biểu tượng gia đình.",
            "Gia đình là môi trường tâm lý đầu tiên dạy trẻ về an toàn, giá trị và quyền lực.",
            "Kỷ luật sâu không phải kiểm soát; nó là dạy trẻ tự điều chỉnh.",
            "Hiểu giáo dục gia đình giúp lãnh đạo tốt hơn cả ở nhà lẫn trong tổ chức.",
        ],
        "pillars": [
            ("Gắn bó an toàn", "Trẻ cần cảm giác được thấy, được đáp ứng và được bảo vệ để dám khám phá.", "Con có thấy mình được yêu ngay cả khi chưa đạt không?"),
            ("Kỷ luật và giới hạn", "Giới hạn tốt làm trẻ an toàn; kiểm soát quá mức làm trẻ sợ hoặc nổi loạn.", "Quy tắc này dạy năng lực hay chỉ tạo phục tùng?"),
            ("Tự chủ", "Mục tiêu không phải đứa trẻ ngoan trước mặt cha mẹ, mà là người biết tự dẫn mình.", "Con đang học tự quyết hay học làm vừa lòng?"),
            ("Kỳ vọng", "Kỳ vọng có thể nâng trẻ lên hoặc làm trẻ sống trong nợ cảm xúc.", "Kỳ vọng này phục vụ con hay phục vụ hình ảnh gia đình?"),
            ("Học tập sâu", "Học tốt cần tò mò, sai được, phản hồi và cảm giác năng lực tăng dần.", "Con đang yêu học hay sợ điểm số?"),
            ("Giá trị gia đình", "Giá trị thật là điều trẻ thấy người lớn làm khi mệt, giận hoặc có lợi ích.", "Gia đình đang dạy giá trị nào bằng hành vi thật?"),
            ("Cha mẹ tự chữa", "Nhiều phản ứng với con là vết thương cũ của cha mẹ bị kích hoạt.", "Tôi đang nuôi con hiện tại hay phản ứng với tuổi thơ của mình?"),
        ],
        "tools": [
            ("Audit phản ứng làm cha mẹ", ["Tình huống:", "Cảm xúc của tôi:", "Ký ức/vết thương bị chạm:", "Nhu cầu của con:", "Giới hạn cần giữ:", "Cách phản ứng trưởng thành hơn:"]),
            ("Bản đồ giá trị gia đình", ["Giá trị muốn dạy:", "Hành vi cha mẹ chứng minh:", "Nghi lễ gia đình:", "Cách xử lý sai lầm:", "Điều cần ngừng làm:"]),
        ],
        "final": "Đứa trẻ không cần cha mẹ hoàn hảo; nó cần người lớn đủ ổn để yêu thương, giữ giới hạn và sửa sai khi làm tổn thương.",
    },
    {
        "n": 49,
        "file": "Tap-49-Tam-ly-hoc-to-chuc-nang-cao.md",
        "title": "Tâm Lý Học Tổ Chức Nâng Cao",
        "subtitle": "Hiểu quyền lực ngầm, hệ miễn dịch tổ chức, chính trị nội bộ, thay đổi quy mô lớn và văn hóa cấp sâu",
        "core": "Tổ chức là một hệ tâm lý sống: nó có ký ức, phòng vệ, nỗi sợ, thói quen, quyền lực và cách tự bảo vệ trước thay đổi.",
        "why": [
            "C-level không chỉ quản lý người, mà quản lý hệ thống tạo hành vi.",
            "Thay đổi thất bại thường vì đụng vào quyền lực, bản sắc và lợi ích ẩn.",
            "Văn hóa cấp sâu nằm ở điều được thưởng, được sợ, được im lặng và được hợp lý hóa.",
            "Hiểu tổ chức nâng cao giúp chẩn đoán đúng trước khi can thiệp lớn.",
        ],
        "pillars": [
            ("Hệ miễn dịch tổ chức", "Tổ chức chống lại thay đổi để giữ ổn định, quyền lực và bản sắc cũ.", "Thay đổi này đe dọa ai và đe dọa điều gì?"),
            ("Quyền lực ngầm", "Quyền lực thật không luôn nằm trên sơ đồ; nó nằm ở thông tin, quan hệ và khả năng chặn việc.", "Ai có thể làm việc dừng lại mà không cần chức danh?"),
            ("Văn hóa cấp sâu", "Văn hóa thật là phản ứng mặc định khi có áp lực, sai lầm và xung đột.", "Khi căng thẳng, tổ chức trở thành ai?"),
            ("Chính trị nội bộ", "Chính trị là quản lý lợi ích, vị thế và liên minh trong điều kiện nguồn lực giới hạn.", "Liên minh nào đang định hình quyết định?"),
            ("Thay đổi quy mô lớn", "Thay đổi cần lý do, năng lực, biểu tượng, người dẫn, nhịp và chiến thắng nhỏ.", "Người ta mất gì nếu thay đổi thành công?"),
            ("Tổ chức học tập", "Tổ chức học khi lỗi được nhìn thấy sớm, không bị che để giữ mặt.", "Tin xấu có đi lên đủ nhanh không?"),
            ("Mệt mỏi tổ chức", "Quá nhiều ưu tiên và thay đổi làm hệ thống tê liệt.", "Điều gì cần dừng để điều quan trọng sống được?"),
        ],
        "tools": [
            ("Chẩn đoán tổ chức sâu", ["Triệu chứng:", "Nỗi sợ hệ thống:", "Quyền lực ngầm:", "Điều bị im lặng:", "Lợi ích bị đe dọa:", "Can thiệp nhỏ nhất:"]),
            ("Bản đồ thay đổi", ["Thay đổi:", "Vì sao thật:", "Ai mất gì:", "Ai được gì:", "Biểu tượng mới:", "Chiến thắng 30 ngày:", "Rủi ro phản kháng:"]),
        ],
        "final": "Muốn đổi tổ chức, đừng chỉ đổi cấu trúc; hãy hiểu hệ thống đang sợ mất gì khi nó phải trở thành phiên bản mới.",
    },
    {
        "n": 50,
        "file": "Tap-50-Ban-do-toi-hau-ve-con-nguoi-xa-hoi-va-y-nghia.md",
        "title": "Bản Đồ Tối Hậu Về Con Người, Xã Hội Và Ý Nghĩa",
        "subtitle": "Tích hợp 50 tập thành một bản đồ thực dụng: cơ thể, cảm xúc, nhận thức, quan hệ, văn hóa, tổ chức, xã hội và ý nghĩa",
        "core": "Con người là hệ nhiều tầng: sinh học, cảm xúc, nhận thức, thói quen, quan hệ, nhóm, văn hóa, tổ chức, xã hội và ý nghĩa liên tục tác động qua lại.",
        "why": [
            "Sau nhiều chuyên ngành, điều quan trọng nhất là biết tích hợp thay vì học rời rạc.",
            "Một vấn đề con người hiếm khi chỉ có một nguyên nhân tâm lý.",
            "C-level cần bản đồ để biết can thiệp ở tầng nào: cá nhân, quan hệ, hệ thống hay ý nghĩa.",
            "Tập cuối giúp biến kiến thức thành phương pháp quan sát và hành động.",
        ],
        "pillars": [
            ("Tầng sinh học", "Cơ thể, não, giấc ngủ, stress và năng lượng là nền của mọi năng lực tâm lý.", "Vấn đề này có phần sinh lý nào đang bị bỏ qua?"),
            ("Tầng cảm xúc", "Cảm xúc là tín hiệu nhu cầu, nguy cơ và giá trị, không phải nhiễu cần loại bỏ.", "Cảm xúc này đang bảo vệ điều gì?"),
            ("Tầng nhận thức", "Niềm tin, thiên kiến và câu chuyện quyết định cách ta hiểu thực tại.", "Câu chuyện nào đang lọc dữ kiện?"),
            ("Tầng thói quen", "Hành vi bền vững đến từ cue, reward, môi trường và bản sắc.", "Hành vi này được hệ thống nào duy trì?"),
            ("Tầng quan hệ", "Con người được hình thành và được kích hoạt trong quan hệ.", "Mô hình quan hệ nào đang lặp lại?"),
            ("Tầng nhóm và văn hóa", "Nhóm tạo chuẩn, thuộc về, phe phái và điều được phép nghĩ.", "Chuẩn nhóm nào đang điều khiển hành vi?"),
            ("Tầng tổ chức và xã hội", "Hệ thống thưởng-phạt, quyền lực, luật chơi và môi trường tạo hành vi hàng loạt.", "Nếu đổi hệ thống, hành vi sẽ đổi ra sao?"),
            ("Tầng ý nghĩa", "Con người chịu khổ tốt hơn khi biết vì sao và thuộc về điều lớn hơn bản thân.", "Ý nghĩa nào đủ lớn để dẫn hành động này?"),
        ],
        "tools": [
            ("Bản đồ chẩn đoán 8 tầng", ["Vấn đề:", "Sinh học:", "Cảm xúc:", "Nhận thức:", "Thói quen:", "Quan hệ:", "Nhóm/văn hóa:", "Tổ chức/xã hội:", "Ý nghĩa:", "Tầng cần can thiệp trước:"]),
            ("Công thức hành động tích hợp", ["Sự thật cần nhìn:", "Tầng gốc:", "Can thiệp nhỏ:", "Người cần tham gia:", "Cách đo:", "Rủi ro đạo đức:"]),
        ],
        "final": "Hiểu con người sâu không phải biết nhiều thuật ngữ; đó là nhìn đúng tầng, hỏi đúng câu và can thiệp đủ nhỏ nhưng trúng hệ thống.",
    },
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
    lines.extend(
        [
            "",
            f"**Một câu cần nhớ:** {tap['core']}",
            "",
            "**Mục tiêu tập này:** sau khi học xong, bạn biết nhìn chủ đề này như một hệ thống lực tâm lý, không chỉ như hiện tượng bề mặt.",
            "",
            "---",
            "",
            "## 1. First Principles: Bản Chất Cốt Lõi",
            "",
            f"**Bản chất:** {tap['core']}",
            "",
            "Mọi chủ đề tâm lý đều có 4 lớp cần nhìn:",
            "",
            "| Lớp | Câu hỏi | Ý nghĩa thực tiễn |",
            "|---|---|---|",
            "| Sinh học | Cơ thể và hệ thần kinh đang ở trạng thái nào? | Nếu nền sinh lý sai, lý trí yếu đi. |",
            "| Cảm xúc | Nỗi sợ, nhu cầu, hy vọng nào đang lái hành vi? | Cảm xúc là dữ liệu về điều con người đang bảo vệ. |",
            "| Bản sắc | Việc này đụng vào câu chuyện tôi là ai không? | Khi đụng bản sắc, dữ kiện thường thua phòng vệ. |",
            "| Hệ thống | Môi trường đang thưởng hoặc phạt điều gì? | Hành vi lặp lại vì hệ thống cho phép nó lặp lại. |",
            "",
            "```text",
            "Câu hỏi gốc:",
            "1. Con người đang cần gì?",
            "2. Họ đang sợ mất gì?",
            "3. Họ đang thuộc về nhóm/câu chuyện nào?",
            "4. Hệ thống đang làm hành vi nào trở nên dễ xảy ra?",
            "```",
            "",
            "---",
            "",
        ]
    )

    for idx, (title, essence, question) in enumerate(tap["pillars"], 2):
        lines.extend(
            [
                f"## {idx}. {title}",
                "",
                f"### Bản chất",
                "",
                essence,
                "",
                render_table(
                    [
                        ("Tín hiệu cần quan sát", "Hành vi lặp lại, cảm xúc mạnh, câu chuyện được kể nhiều lần", "Điều gì cứ quay lại?"),
                        ("Rủi ro hiểu sai", "Chỉ nhìn lời nói mà bỏ qua động cơ và hệ thống", "Tôi đang tin narrative quá nhanh không?"),
                        ("Can thiệp thực dụng", "Đổi câu hỏi, đổi môi trường, đổi nhịp phản hồi hoặc đổi ranh giới", "Can thiệp nhỏ nhất là gì?"),
                    ]
                ),
                "",
                "```text",
                "Câu hỏi ứng dụng:",
                f"- {question}",
                "- Dữ kiện nào ủng hộ và dữ kiện nào phản biện nhận định của tôi?",
                "- Nếu bỏ ego của tôi ra, tôi sẽ nhìn vấn đề này thế nào?",
                "```",
                "",
                f"**Nguyên tắc:** {title} chỉ được hiểu đúng khi nhìn cùng lúc con người bên trong và bối cảnh bên ngoài.",
                "",
                "---",
                "",
            ]
        )

    lines.extend(
        [
            f"## {len(tap['pillars']) + 2}. Công Cụ Thực Hành",
            "",
        ]
    )
    for tool_name, fields in tap["tools"]:
        lines.extend([f"### {tool_name}", "", "```text"])
        lines.extend(fields)
        lines.extend(["```", ""])

    lines.extend(
        [
            "---",
            "",
            f"## {len(tap['pillars']) + 3}. Lộ Trình Thực Hành 4 Tuần",
            "",
            "| Tuần | Trọng tâm | Việc làm cụ thể |",
            "|---|---|---|",
            "| 1 | Quan sát | Chọn một tình huống thật liên quan đến tập này và ghi lại dữ kiện, cảm xúc, người liên quan. |",
            "| 2 | Gọi tên | Dùng các khái niệm trong tập để đặt tên đúng lực tâm lý đang vận hành. |",
            "| 3 | Can thiệp nhỏ | Thay một câu hỏi, một ranh giới, một nhịp họp, một thiết kế môi trường hoặc một hành vi. |",
            "| 4 | Review | So sánh trước-sau: điều gì đổi, điều gì không đổi, tầng nào cần can thiệp tiếp. |",
            "",
            "---",
            "",
            f"## {len(tap['pillars']) + 4}. Bảng Tóm Tắt First Principles",
            "",
            "| Khái niệm | Bản chất | Câu hỏi cần nhớ |",
            "|---|---|---|",
        ]
    )
    for title, essence, question in tap["pillars"]:
        lines.append(f"| {title} | {essence} | {question} |")

    lines.extend(
        [
            "",
            "---",
            "",
            f"## {len(tap['pillars']) + 5}. Một Câu Để Nhớ Toàn Bộ Tập {n}",
            "",
            f"> {tap['final']}",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    for tap in TAPS:
        path = ROOT / tap["file"]
        path.write_text(render_tap(tap), encoding="utf-8")
        print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
