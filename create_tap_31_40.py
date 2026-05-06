from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent


TAPS = [
    {
        "n": 31,
        "file": "Tap-31-Tam-ly-vo-thuc-va-nhung-dong-co-an.md",
        "title": "Tâm Lý Vô Thức Và Những Động Cơ Ẩn",
        "subtitle": "Hiểu phần con người không tự thấy: phòng vệ sâu, phóng chiếu, chuyển di, ham muốn bị che giấu và các mô hình lặp lại",
        "why": [
            "Người thông minh vẫn không hiểu hết động cơ thật của mình.",
            "Nhiều phản ứng hiện tại là tiếng vọng của quan hệ cũ, tổn thương cũ hoặc nhu cầu chưa được gọi tên.",
            "C-level dễ nhầm phân tích sắc bén với tự hiểu mình, trong khi vô thức vẫn có thể lái quyết định.",
            "Hiểu vô thức giúp đọc hành vi sâu hơn mà không vội phán xét hoặc tự lừa mình.",
        ],
        "remember": "Vô thức không phải phần thần bí; nó là phần động cơ, ký ức, sợ hãi và ham muốn đang vận hành trước khi ta kịp gọi tên.",
        "sections": [
            ("First Principles: Vô Thức Là Gì?", "Vô thức là phần xử lý tâm lý nằm ngoài nhận biết trực tiếp nhưng vẫn ảnh hưởng đến cảm xúc, lựa chọn và quan hệ.", [("Không biết mình muốn gì", "Hành vi mâu thuẫn với lời nói"), ("Không biết mình sợ gì", "Phòng vệ, né tránh, kiểm soát"), ("Không biết mình lặp lại gì", "Chọn lại mô hình quan hệ cũ")], ["Tôi đang nói một điều nhưng làm điều gì khác?", "Phản ứng này đang bảo vệ nhu cầu nào?", "Có mô hình nào lặp lại nhiều lần trong đời tôi?"]),
            ("Cơ Chế Phòng Vệ Sâu", "Phòng vệ giúp ta tránh đau, xấu hổ hoặc sự thật khó chịu; vấn đề là ta thường tin phòng vệ đó là lý trí.", [("Hợp lý hóa", "Tạo lý do đẹp cho động cơ chưa đẹp"), ("Phóng chiếu", "Thấy ở người khác điều mình không nhận ở mình"), ("Trí thức hóa", "Phân tích để khỏi cảm nhận"), ("Lý tưởng hóa", "Nhìn người khác quá hoàn hảo rồi thất vọng mạnh")], ["Tôi đang né cảm xúc nào bằng lý luận?", "Tôi khó chịu với ai vì họ chạm vào phần nào trong tôi?", "Tôi có đang biến người khác thành biểu tượng thay vì con người thật?"]),
            ("Phóng Chiếu: Khi Ta Thấy Mình Trong Người Khác", "Ta dễ gán cho người khác động cơ, lỗi hoặc cảm xúc mà chính mình khó chấp nhận.", [("Nghi người khác thao túng", "Có thể mình đang sợ bị kiểm soát"), ("Ghét người khoe thành tích", "Có thể mình cũng cần được công nhận"), ("Thấy ai cũng yếu", "Có thể mình không cho phép mình yếu")], ["Điều tôi ghét ở người này có tồn tại trong tôi không?", "Tôi đang phản ứng với họ hay với phần bị chối bỏ của tôi?", "Nếu bớt phán xét, dữ kiện thật là gì?"]),
            ("Chuyển Di: Quan Hệ Cũ Đi Vào Quan Hệ Mới", "Ta có thể phản ứng với sếp, vợ/chồng, nhân sự hoặc đối tác như thể họ là nhân vật cũ trong đời mình.", [("Sếp phản biện", "Cảm giác bị cha/mẹ phê bình"), ("Người thân im lặng", "Cảm giác bị bỏ rơi"), ("Nhân sự không nghe", "Cảm giác mất kiểm soát xưa")], ["Tình huống này giống ai trong quá khứ?", "Cường độ cảm xúc có lớn hơn sự kiện hiện tại không?", "Tôi có đang bắt người hiện tại trả nợ cảm xúc cũ không?"]),
            ("Ham Muốn Bị Che Giấu", "Không phải ham muốn nào cũng dễ chấp nhận, nên tâm trí có thể che nó bằng lý do nghe cao đẹp.", [("Muốn quyền lực", "Nói là vì tổ chức"), ("Muốn được ngưỡng mộ", "Nói là truyền cảm hứng"), ("Muốn trả đũa", "Nói là giữ tiêu chuẩn")], ["Nếu thành thật 100%, tôi muốn điều gì?", "Tôi được lợi gì khi giữ câu chuyện đẹp này?", "Động cơ này có phần nào chính đáng và phần nào cần kiểm soát?"]),
            ("Mô Hình Lặp Lại", "Vô thức thường lộ ra qua điều ta lặp lại dù đã tự hứa sẽ khác.", [("Chọn người khó yêu", "Xác nhận niềm tin mình không đủ giá trị"), ("Làm quá sức", "Chứng minh mình xứng đáng"), ("Kiểm soát", "Tránh cảm giác bất an")], ["Tôi đang lặp lại điều gì trong quan hệ/công việc?", "Mô hình này từng giúp tôi sống sót thế nào?", "Cái giá hiện tại là gì?"]),
            ("Vô Thức Trong Lãnh Đạo", "Quyền lực làm động cơ ẩn có hậu quả lớn hơn vì nó ảnh hưởng đến nhiều người.", [("Tự ái bị chạm", "Ra quyết định để giữ mặt"), ("Sợ bị phản bội", "Tập trung quyền lực quá mức"), ("Cần được ngưỡng mộ", "Tạo văn hóa chiều lòng lãnh đạo")], ["Tôi đang dùng quyền lực để xử lý vấn đề hay xử lý cảm xúc cũ?", "Ai có thể nói tôi đang tự lừa mình?", "Quyết định này còn hợp lý nếu ego của tôi không liên quan không?"]),
            ("Cách Làm Việc Với Vô Thức", "Không thể ép vô thức lộ ra bằng lý trí thuần túy; cần quan sát lặp lại, cảm xúc, giấc mơ, phản ứng cơ thể và phản hồi từ người tin cậy.", [("Quan sát mô hình", "Nhìn điều lặp lại"), ("Gọi tên cảm xúc", "Giảm tự động hóa"), ("Nhận phản hồi", "Mượn mắt người khác"), ("Trị liệu/coaching sâu", "Có không gian an toàn để nhìn sự thật")], ["Tôi cần quan sát mô hình nào trong 30 ngày?", "Tôi có người phản chiếu đủ an toàn không?", "Khi nào tôi cần chuyên gia?"]),
        ],
        "tools": [
            ("Bản đồ động cơ ẩn", ["Hành vi lặp lại:", "Lý do tôi thường kể:", "Cảm xúc thật:", "Nhu cầu thật:", "Điều tôi sợ nếu nhìn thẳng:", "Hành vi trưởng thành hơn:"]),
            ("Kiểm tra phóng chiếu", ["Người làm tôi phản ứng mạnh:", "Điều tôi gán cho họ:", "Dữ kiện thật:", "Phần nào có thể là của tôi:", "Cách phản ứng công bằng hơn:"]),
        ],
        "weeks": ["Quan sát một mô hình lặp lại.", "Ghi lại 3 lần phản ứng quá mạnh.", "Hỏi một người tin cậy về điểm mù của mình.", "Chọn một hành vi mới thay cho phòng vệ cũ."],
        "summary": [("Vô thức", "Động cơ ngoài nhận biết trực tiếp", "Điều gì đang lái tôi mà tôi chưa thấy?"), ("Phòng vệ", "Tránh đau hoặc xấu hổ", "Tôi đang né cảm xúc nào?"), ("Phóng chiếu", "Gán phần của mình cho người khác", "Điều tôi ghét có phần nào trong tôi?"), ("Chuyển di", "Quan hệ cũ đi vào hiện tại", "Tôi đang phản ứng với ai thật sự?"), ("Mô hình lặp lại", "Vô thức lộ qua sự lặp", "Tôi cứ tạo lại kết quả nào?")],
        "final": "Muốn tự do hơn, không chỉ cần biết mình nghĩ gì; cần đủ can đảm để nhìn phần mình đang che giấu khỏi chính mình.",
    },
    {
        "n": 32,
        "file": "Tap-32-Tam-ly-tu-ai-narcissism-va-cai-toi-mong-manh.md",
        "title": "Tâm Lý Tự Ái, Narcissism Và Cái Tôi Mong Manh",
        "subtitle": "Hiểu nhu cầu được ngưỡng mộ, sợ bị xem thường, cái tôi dễ vỡ và cách quyền lực khuếch đại tự ái",
        "why": ["Tự ái là một trong những lực tâm lý mạnh nhất trong lãnh đạo và quan hệ.", "Người thành công dễ đồng nhất giá trị bản thân với hình ảnh, vị trí và thành tựu.", "Narcissism không chỉ là khoe khoang; nó có thể là cái tôi mong manh được bọc bằng tự tin.", "Hiểu tự ái giúp bảo vệ sự thật, quan hệ và văn hóa tổ chức."],
        "remember": "Tự ái là nỗi đau khi hình ảnh về mình bị đe dọa; narcissism là khi đời sống xoay quanh việc bảo vệ hoặc phóng đại hình ảnh đó.",
        "sections": [
            ("First Principles: Tự Ái Là Gì?", "Tự ái là hệ thống bảo vệ giá trị bản thân khi ta cảm thấy bị xem nhẹ, sai, kém hoặc mất vị thế.", [("Tự trọng lành mạnh", "Biết giá trị nhưng vẫn học được"), ("Tự ái mong manh", "Cần được xác nhận liên tục"), ("Narcissism", "Bản thân trở thành trung tâm của thực tại")], ["Tôi có thể nhận sai mà không sụp đổ không?", "Tôi đang bảo vệ giá trị hay hình ảnh?", "Tôi cần ai ngưỡng mộ mình để thấy ổn?"]),
            ("Narcissism Lành Mạnh Và Độc Hại", "Một mức tự tin và tham vọng lành mạnh giúp con người tạo giá trị; độc hại khi người khác bị dùng làm gương phản chiếu cho cái tôi.", [("Lành mạnh", "Tự tin, có mục tiêu, vẫn tôn trọng người khác"), ("Độc hại", "Cần hơn thua, thiếu đồng cảm, không nhận sai"), ("Ẩn", "Bên ngoài khiêm tốn, bên trong rất dễ tổn thương")], ["Thành công của tôi có làm người khác nhỏ lại không?", "Tôi có cần thắng mọi cuộc nói chuyện không?", "Tôi có thể vui khi người khác tỏa sáng không?"]),
            ("Cái Tôi Mong Manh Ở Người Thành Công", "Càng nhiều thành tựu, con người càng dễ sợ mất hình ảnh đã xây.", [("Sợ bị phát hiện không đủ giỏi", "Làm quá sức"), ("Sợ bị thay thế", "Không trao quyền"), ("Sợ mất ngưỡng mộ", "Tạo sân khấu cá nhân")], ["Nếu không còn vai trò này, tôi thấy mình là ai?", "Tôi đang xây năng lực hay xây tượng đài?", "Tôi có đang dùng tổ chức để giữ hình ảnh?"]),
            ("Tự Ái Trong Phản Hồi", "Phản hồi chạm vào khoảng cách giữa con người thật và hình ảnh ta muốn giữ.", [("Phản công", "Bảo vệ mặt mũi"), ("Biện minh", "Giữ cảm giác đúng"), ("Im lặng lạnh", "Trừng phạt người chạm vào tự ái")], ["Tôi nghe phản hồi để học hay để phòng vệ?", "Phần nào trong phản hồi đúng dù khó chịu?", "Tôi có đang phạt người nói thật không?"]),
            ("Narcissism Trong Quyền Lực", "Quyền lực cho người tự ái khả năng biến nhu cầu cá nhân thành văn hóa tổ chức.", [("Cần trung thành", "Thưởng người chiều ý"), ("Không chịu phản biện", "Tắt sự thật"), ("Ưa hào quang", "Ưu tiên truyền thông hơn thực chất")], ["Tổ chức đang phục vụ khách hàng hay phục vụ hình ảnh lãnh đạo?", "Ai được thăng tiến: người nói thật hay người tán dương?", "Tin xấu có đến sớm không?"]),
            ("Quan Hệ Với Người Tự Ái Mạnh", "Không nên cố chữa họ bằng tình cảm hoặc lý luận nếu họ không có năng lực tự soi.", [("Charm ban đầu", "Tạo hấp dẫn"), ("Devalue", "Hạ thấp khi bạn không còn phục vụ cái tôi"), ("Gaslight nhẹ", "Làm bạn nghi ngờ cảm nhận")], ["Tôi có bị kéo vào việc chứng minh giá trị không?", "Ranh giới nào cần rõ?", "Hành vi lặp lại quan trọng hơn lời hứa nào?"]),
            ("Tự Chữa Tự Ái", "Mục tiêu không phải xóa cái tôi, mà làm cái tôi đủ vững để chịu được sự thật.", [("Nhận sai nhỏ", "Tập không sụp đổ"), ("Công nhận người khác", "Giảm trung tâm bản thân"), ("Tách giá trị khỏi thành tích", "Tăng tự do nội tâm")], ["Tôi có thể nói câu 'tôi sai' ở đâu?", "Tôi có thể để ai khác nhận credit không?", "Điều gì làm tôi có giá trị ngoài thành công?"]),
        ],
        "tools": [("Audit tự ái", ["Tình huống làm tôi tự ái:", "Hình ảnh bị đe dọa:", "Phòng vệ tôi dùng:", "Sự thật cần nghe:", "Phản ứng trưởng thành hơn:"]), ("Kiểm tra narcissism trong lãnh đạo", ["Ai dám phản biện tôi?", "Tôi có nhận sai công khai không?", "Tôi có cần được ngưỡng mộ không?", "Tổ chức có đang chiều cảm xúc của tôi không?"])],
        "weeks": ["Ghi 3 lần tự ái bị chạm.", "Thực hành nhận một phản hồi mà không biện minh.", "Công nhận công khai đóng góp của người khác.", "Tách một quyết định khỏi nhu cầu giữ hình ảnh."],
        "summary": [("Tự ái", "Đau khi hình ảnh bị đe dọa", "Hình ảnh nào đang bị chạm?"), ("Narcissism", "Đời sống xoay quanh cái tôi", "Người khác có bị dùng làm gương không?"), ("Cái tôi mong manh", "Bên ngoài mạnh, bên trong dễ vỡ", "Tôi có chịu được sự thật không?"), ("Quyền lực", "Khuếch đại tự ái", "Tổ chức có dám nói thật không?")],
        "final": "Cái tôi trưởng thành không cần lúc nào cũng lớn; nó cần đủ vững để không bóp méo sự thật khi bị chạm.",
    },
    {
        "n": 33,
        "file": "Tap-33-Dark-psychology-thao-tung-va-cach-tu-bao-ve.md",
        "title": "Dark Psychology, Thao Túng Và Cách Tự Bảo Vệ",
        "subtitle": "Nhận diện thao túng, gaslighting, charm giả, quyền lực ngầm và các kiểu người nguy hiểm trong quan hệ, đối tác và tổ chức",
        "why": ["Không phải ai hiểu tâm lý cũng dùng nó có đạo đức.", "C-level cần nhận diện người giỏi nhưng nguy hiểm trước khi họ gây chi phí hệ thống.", "Thao túng thường bắt đầu bằng sự hấp dẫn, giúp đỡ hoặc lý tưởng chung.", "Tự bảo vệ cần dữ kiện, ranh giới, hệ thống và người phản chiếu."],
        "remember": "Thao túng là tác động làm người khác mất rõ ràng, mất tự chủ hoặc nghi ngờ chính cảm nhận của mình để phục vụ lợi ích của người thao túng.",
        "sections": [
            ("First Principles: Thao Túng Là Gì?", "Thao túng không chỉ là nói dối; nó là thiết kế cảm xúc, thông tin và áp lực để người khác chọn theo hướng họ không thật sự hiểu hoặc không tự do.", [("Ảnh hưởng lành mạnh", "Tăng rõ ràng và tự chủ"), ("Thao túng", "Giảm rõ ràng và tự chủ"), ("Cưỡng ép", "Dùng sợ hãi hoặc hậu quả trực tiếp")], ["Người kia có hiểu đủ không?", "Họ có thể nói không không?", "Kỹ thuật này có cần che giấu mới hiệu quả không?"]),
            ("Dark Triad Ở Mức Thực Dụng", "Ba cụm đặc điểm cần nhận diện là tự ái độc hại, thao lược và lạnh cảm xúc.", [("Narcissism", "Cần ngưỡng mộ, không chịu sai"), ("Machiavellianism", "Tính toán, dùng người như quân cờ"), ("Psychopathy nhẹ", "Thiếu hối lỗi, lạnh với hậu quả của người khác")], ["Người này có nhận trách nhiệm không?", "Họ đối xử với người yếu thế thế nào?", "Họ có lịch sử làm người khác kiệt sức không?"]),
            ("Charm Giả Và Love Bombing", "Người thao túng thường tạo kết nối nhanh để hạ phòng vệ.", [("Khen quá mức", "Tạo cảm giác đặc biệt"), ("Chia sẻ thân mật quá sớm", "Tạo nợ cảm xúc"), ("Hứa tương lai lớn", "Kéo vào cam kết trước khi có dữ kiện")], ["Tốc độ thân mật có bất thường không?", "Hành động có khớp lời nói theo thời gian không?", "Tôi có đang thấy mình đặc biệt quá nhanh không?"]),
            ("Gaslighting", "Gaslighting làm bạn nghi ngờ trí nhớ, cảm nhận hoặc năng lực phán đoán của mình.", [("Phủ nhận sự kiện", "Chuyện đó chưa từng xảy ra"), ("Đảo lỗi", "Bạn quá nhạy cảm"), ("Làm mơ hồ", "Không ai khác thấy vậy")], ["Tôi có dữ kiện ghi lại không?", "Người khác độc lập nhìn sự kiện thế nào?", "Tôi có ngày càng mất tự tin khi ở gần họ không?"]),
            ("Thao Túng Trong Tổ Chức", "Thao túng tổ chức thường đi qua thông tin, phe nhóm, credit, tin đồn và tiếp cận lãnh đạo.", [("Giữ thông tin", "Tạo phụ thuộc"), ("Chia để trị", "Làm các bên nghi nhau"), ("Quản trị hình ảnh", "Gần lãnh đạo, xa sự thật")], ["Ai được lợi khi thông tin mơ hồ?", "Người này làm hệ thống rõ hơn hay rối hơn?", "Có nhiều người rời đi vì cùng một người không?"]),
            ("Tự Bảo Vệ", "Tự bảo vệ không phải hoang tưởng; đó là thiết kế ranh giới, dữ kiện và quyền quyết định chậm lại.", [("Ghi lại dữ kiện", "Chống mơ hồ"), ("Không quyết khi bị ép", "Giữ tự chủ"), ("Tham khảo người độc lập", "Chống cô lập"), ("Ranh giới rõ", "Không đàm phán với sự lạm dụng")], ["Tôi có đang bị ép quyết nhanh không?", "Tôi có bị cô lập khỏi người phản chiếu không?", "Ranh giới không thỏa hiệp là gì?"]),
            ("Sa Thải/Chấm Dứt Với Người Nguy Hiểm", "Người thao túng mạnh thường leo thang khi mất quyền kiểm soát; cần quy trình, pháp lý và truyền thông rõ.", [("Không đối đầu cảm tính", "Giảm phản ứng trả đũa"), ("Dựa vào dữ kiện", "Không tranh luận narrative"), ("Bảo vệ người bị ảnh hưởng", "Tăng an toàn hệ thống")], ["Quy trình có đủ chắc không?", "Ai cần được bảo vệ?", "Thông điệp nào đủ rõ mà không vi phạm bảo mật?"]),
        ],
        "tools": [("Checklist thao túng", ["Có ép quyết nhanh không?", "Có làm tôi nghi ngờ cảm nhận không?", "Có cô lập tôi khỏi người khác không?", "Có lời nói và hành vi lệch nhau không?", "Có lịch sử nạn nhân lặp lại không?"]), ("Bản đồ bảo vệ", ["Dữ kiện cần ghi:", "Người phản chiếu độc lập:", "Ranh giới:", "Điều kiện dừng:", "Kênh pháp lý/quy trình cần dùng:"])],
        "weeks": ["Nhận diện một mô hình thao túng nhẹ từng gặp.", "Tập ghi dữ kiện thay vì tranh luận cảm xúc.", "Thiết kế ranh giới với một người khó.", "Review một quan hệ/đối tác bằng checklist thao túng."],
        "summary": [("Thao túng", "Giảm rõ ràng và tự chủ", "Tôi có thể nói không không?"), ("Gaslighting", "Làm nghi ngờ cảm nhận", "Dữ kiện độc lập là gì?"), ("Dark Triad", "Tự ái, thao lược, lạnh cảm xúc", "Người này có hối lỗi thật không?"), ("Tự bảo vệ", "Dữ kiện + ranh giới + hệ thống", "Tôi cần bảo vệ điều gì ngay?")],
        "final": "Tin người là cần thiết, nhưng tin mà không có dữ kiện, ranh giới và thời gian kiểm chứng là trao quyền cho người biết diễn.",
    },
    {
        "n": 34,
        "file": "Tap-34-Tam-ly-tinh-yeu-hon-nhan-va-than-mat.md",
        "title": "Tâm Lý Tình Yêu, Hôn Nhân Và Thân Mật",
        "subtitle": "Hiểu gắn bó trưởng thành, thân mật cảm xúc, quyền lực, tình dục, phản bội và cách xây quan hệ sâu sau thành công",
        "why": ["Quan hệ thân mật là nơi vết thương và nhu cầu gắn bó hiện rõ nhất.", "Người thành công dễ giỏi kiểm soát công việc nhưng khó yếu mềm trong tình yêu.", "Hôn nhân cần cả tình cảm, kỹ năng xung đột, tình dục, tiền bạc, ranh giới và ý nghĩa chung.", "Hiểu thân mật giúp sống bớt cô đơn dù có nhiều thành tựu."],
        "remember": "Thân mật trưởng thành là khả năng được nhìn thấy thật, được tự do thật và vẫn chọn quay về với nhau.",
        "sections": [
            ("First Principles: Tình Yêu Là Gì?", "Tình yêu không chỉ là cảm xúc; nó là hệ thống gắn bó, lựa chọn, chăm sóc, ham muốn, tin cậy và cam kết được lặp lại.", [("Hấp dẫn", "Kéo hai người lại gần"), ("Gắn bó", "Tạo cảm giác an toàn"), ("Cam kết", "Giữ quan hệ qua thay đổi"), ("Sửa chữa", "Phục hồi sau tổn thương")], ["Tôi đang yêu người thật hay hình ảnh?", "Quan hệ này có an toàn và tự do không?", "Chúng tôi có biết sửa chữa không?"]),
            ("Thân Mật Cảm Xúc", "Thân mật là được biết đến mà không phải diễn vai.", [("Chia sẻ thật", "Nói nhu cầu và sợ hãi"), ("Được đón nhận", "Không bị làm nhục"), ("Phản hồi dịu", "Sự thật không thành vũ khí")], ["Tôi có cho người kia thấy phần yếu không?", "Tôi có làm họ an toàn khi họ thật không?", "Chúng tôi nói về việc khó hay chỉ vận hành gia đình?"]),
            ("Quyền Lực Trong Hôn Nhân", "Tiền, thời gian, tình dục, cha mẹ, con cái và sự nghiệp đều tạo quyền lực.", [("Tiền", "Ai có tiếng nói?"), ("Thời gian", "Ai được ưu tiên?"), ("Gia đình hai bên", "Ai đặt ranh giới?"), ("Sự nghiệp", "Ai hy sinh?")], ["Quyền lực có được nói rõ không?", "Ai đang âm thầm chịu thiệt?", "Công bằng của chúng tôi là gì?"]),
            ("Tình Dục Và Kết Nối", "Tình dục không chỉ là sinh lý; nó liên quan đến an toàn, ham muốn, tự trọng, quyền lực và cảm giác được chọn.", [("Ham muốn giảm", "Có thể do stress, giận ngầm, mệt, mất kết nối"), ("Tình dục như nghĩa vụ", "Tạo xa cách"), ("Tình dục như kết nối", "Cần an toàn và hiện diện")], ["Chúng tôi có nói được về tình dục không?", "Có cảm xúc chưa xử lý đang làm tắt ham muốn không?", "Cơ thể tôi đang cần gì?"]),
            ("Phản Bội", "Phản bội phá vỡ thực tại chung: người bị phản bội không chỉ mất niềm tin, mà mất cả cảm giác mình hiểu đời mình.", [("Sự kiện", "Điều đã xảy ra"), ("Ý nghĩa", "Tôi có bị lừa không?"), ("Niềm tin", "Tôi còn an toàn không?")], ["Sự thật đã đủ rõ chưa?", "Người gây tổn thương có nhận trách nhiệm không?", "Có điều kiện nào để xây lại niềm tin không?"]),
            ("Vòng Lặp Xung Đột Vợ Chồng", "Nhiều cặp không cãi về nội dung mà cãi trong cùng một vòng lặp gắn bó.", [("Một người đòi gần", "Người kia thấy bị ép"), ("Một người rút", "Người kia thấy bị bỏ"), ("Cả hai phòng vệ", "Không ai thấy nhu cầu thật")], ["Vòng lặp của chúng tôi là gì?", "Tôi càng làm gì thì người kia càng sợ gì?", "Một hành vi phá vòng lặp là gì?"]),
            ("Tình Yêu Sau Thành Công", "Sau khi có tiền, vị trí hoặc gia đình ổn định, câu hỏi chuyển từ tồn tại sang kết nối thật.", [("Bận rộn", "Né thân mật"), ("Vai trò cha/mẹ", "Quên vai người yêu"), ("Thành công bên ngoài", "Cô đơn bên trong")], ["Chúng tôi còn tò mò về nhau không?", "Lần cuối nói chuyện không logistics là khi nào?", "Quan hệ này đang cần hồi sinh điều gì?"]),
        ],
        "tools": [("Bản đồ thân mật", ["Tôi thấy an toàn khi:", "Tôi đóng lại khi:", "Tôi cần được yêu bằng:", "Tôi cần ranh giới ở:", "Một cuộc nói chuyện cần có:"]), ("Review hôn nhân/quan hệ", ["Kết nối:", "Công bằng:", "Tình dục:", "Tiền bạc:", "Gia đình hai bên:", "Xung đột lặp lại:", "Một hành vi sửa chữa:"])],
        "weeks": ["Nói một nhu cầu thật thay vì một lời trách.", "Có một buổi nói chuyện không bàn logistics.", "Đặt một ranh giới về thời gian/cha mẹ/tiền bạc.", "Thực hiện một hành vi sửa chữa lặp lại 7 ngày."],
        "summary": [("Tình yêu", "Gắn bó + lựa chọn + chăm sóc", "Tôi yêu người thật hay hình ảnh?"), ("Thân mật", "Được thấy thật và vẫn an toàn", "Tôi có dám thật không?"), ("Quyền lực", "Ai có tiếng nói và ai hy sinh", "Công bằng thật là gì?"), ("Phản bội", "Phá vỡ thực tại chung", "Điều kiện xây lại niềm tin là gì?")],
        "final": "Quan hệ sâu không cần hai người hoàn hảo; nó cần hai người đủ thật, đủ tử tế và đủ kỷ luật để sửa chữa.",
    },
    {
        "n": 35,
        "file": "Tap-35-Tam-ly-gioi-nam-tinh-nu-tinh-va-vai-tro-xa-hoi.md",
        "title": "Tâm Lý Giới, Nam Tính, Nữ Tính Và Vai Trò Xã Hội",
        "subtitle": "Hiểu khác biệt giới một cách tỉnh táo: sinh học, văn hóa, quyền lực, hấp dẫn, gia đình, lãnh đạo và trưởng thành",
        "why": ["Giới ảnh hưởng đến kỳ vọng, hành vi, thân mật, quyền lực và bản sắc.", "Cần học chủ đề này cẩn thận để tránh định kiến đơn giản hóa.", "Nam giới và nữ giới đều chịu áp lực vai trò xã hội khác nhau.", "Hiểu giới giúp lãnh đạo, yêu thương và nuôi dạy con công bằng hơn."],
        "remember": "Giới không phải chiếc hộp cố định; nó là giao điểm giữa sinh học, văn hóa, vai trò, quyền lực và lựa chọn cá nhân.",
        "sections": [
            ("First Principles: Giới Là Gì?", "Giới cần được nhìn đa tầng: cơ thể sinh học, bản sắc, vai trò xã hội, kỳ vọng văn hóa và quyền lực.", [("Sinh học", "Cơ thể, hormone, sinh sản"), ("Văn hóa", "Chuẩn nam/nữ được dạy"), ("Bản sắc", "Cách một người hiểu chính mình"), ("Vai trò", "Điều xã hội kỳ vọng")], ["Tôi đang nói về sinh học hay văn hóa?", "Niềm tin này là dữ kiện hay định kiến?", "Vai trò nào đang làm người này mất tự do?"]),
            ("Nam Tính Trưởng Thành", "Nam tính trưởng thành không phải là thống trị; nó là sức mạnh có trách nhiệm, ranh giới, bảo vệ và khả năng cảm xúc.", [("Chưa trưởng thành", "Cứng, né yếu mềm, cần thắng"), ("Trưởng thành", "Vững, biết cảm, biết chịu trách nhiệm"), ("Độc hại", "Dùng quyền lực để che sợ hãi")], ["Tôi có đồng nhất mạnh mẽ với không được yếu không?", "Tôi bảo vệ hay kiểm soát?", "Tôi có biết xin lỗi không?"]),
            ("Nữ Tính Trưởng Thành", "Nữ tính trưởng thành không phải là làm hài lòng; nó là kết nối, trực giác, sức sống, ranh giới và quyền được chọn.", [("Chưa trưởng thành", "Hy sinh để được yêu"), ("Trưởng thành", "Kết nối nhưng không mất mình"), ("Bị bóp méo", "Dùng yếu mềm như thao túng hoặc tự xóa mình")], ["Tôi có nói nhu cầu thật không?", "Tôi có quyền chọn không?", "Tôi đang chăm sóc hay tự hy sinh?"]),
            ("Áp Lực Vai Trò Giới", "Nhiều đau khổ đến từ việc con người phải diễn đúng vai hơn là sống thật.", [("Nam", "Phải thành công, mạnh, không khóc"), ("Nữ", "Phải đẹp, dịu, chăm sóc, không quá tham vọng"), ("Lãnh đạo", "Nam bị phạt khi mềm, nữ bị phạt khi cứng")], ["Vai trò nào đang ép tôi?", "Tôi đang đánh giá người khác theo chuẩn công bằng không?", "Tổ chức có phạt người lệch vai giới không?"]),
            ("Hấp Dẫn Và Chọn Bạn Đời", "Hấp dẫn chịu ảnh hưởng bởi sinh học, địa vị, an toàn, thân mật, giá trị và văn hóa.", [("Địa vị", "Tín hiệu năng lực/tài nguyên"), ("An toàn", "Tín hiệu tin cậy"), ("Sức sống", "Tín hiệu năng lượng"), ("Giá trị chung", "Tín hiệu bền vững")], ["Tôi bị hấp dẫn bởi điều gì?", "Điều đó phục vụ thân mật dài hạn không?", "Tôi đang chọn bằng vết thương hay giá trị?"]),
            ("Giới Trong Lãnh Đạo", "Lãnh đạo tốt cần cả năng lượng định hướng và năng lượng kết nối, không nên gắn cứng với giới.", [("Quyết đoán", "Cần nhưng có thể thành áp đặt"), ("Đồng cảm", "Cần nhưng có thể thành né chuẩn"), ("Tích hợp", "Rõ ràng + kết nối + trách nhiệm")], ["Tổ chức có định kiến về lãnh đạo nam/nữ không?", "Tôi đang thiếu năng lượng nào: rõ ràng hay kết nối?", "Ai bị đánh giá khắt khe hơn vì giới?"]),
            ("Nuôi Dạy Con Về Giới", "Con cần được hướng dẫn để hiểu cơ thể, ranh giới, tôn trọng và tự do khỏi vai diễn cứng nhắc.", [("Con trai", "Được học cảm xúc và trách nhiệm"), ("Con gái", "Được học ranh giới và quyền chọn"), ("Cả hai", "Tôn trọng cơ thể, consent, phẩm giá")], ["Tôi đang truyền định kiến nào?", "Con có được phép là chính mình không?", "Tôi dạy con về tôn trọng và ranh giới thế nào?"]),
        ],
        "tools": [("Audit vai trò giới", ["Vai trò tôi đang diễn:", "Tôi được gì:", "Tôi mất gì:", "Niềm tin văn hóa phía sau:", "Lựa chọn trưởng thành hơn:"]), ("Kiểm tra định kiến lãnh đạo", ["Tôi khen/phê bình nam và nữ theo cùng tiêu chuẩn không?", "Ai bị gọi là quá cứng/quá mềm?", "Hành vi nào thật sự tạo kết quả?"])],
        "weeks": ["Quan sát một định kiến giới trong mình.", "Nói chuyện với người khác giới về áp lực họ chịu.", "Review một quyết định nhân sự qua lăng kính giới.", "Chọn một hành vi sống thật hơn thay vì diễn vai."],
        "summary": [("Giới", "Sinh học + văn hóa + vai trò", "Tầng nào đang chi phối?"), ("Nam tính", "Sức mạnh có trách nhiệm", "Tôi bảo vệ hay kiểm soát?"), ("Nữ tính", "Kết nối có ranh giới", "Tôi chăm sóc hay tự xóa mình?"), ("Vai trò", "Chuẩn xã hội", "Vai nào đang làm mất tự do?")],
        "final": "Trưởng thành về giới là không bị vai diễn nam/nữ điều khiển, mà biết tích hợp sức mạnh, kết nối, ranh giới và trách nhiệm.",
    },
    {
        "n": 36,
        "file": "Tap-36-Tam-ly-khung-hoang-va-lanh-dao-duoi-ap-luc.md",
        "title": "Tâm Lý Khủng Hoảng Và Lãnh Đạo Dưới Áp Lực",
        "subtitle": "Hiểu panic, tê liệt, đổ lỗi, che giấu thông tin và cách giữ bình tĩnh tập thể khi áp lực cực cao",
        "why": ["Khủng hoảng làm con người trở về phản ứng sinh tồn.", "Tổ chức trong khủng hoảng cần rõ ràng, nhịp giao tiếp và người chịu trách nhiệm.", "Lãnh đạo cần quản trị trạng thái thần kinh tập thể trước khi đòi hỏi tư duy tốt.", "Quyết định tệ nhất thường được đưa ra khi sợ hãi giả dạng khẩn cấp."],
        "remember": "Trong khủng hoảng, nhiệm vụ đầu tiên của lãnh đạo là làm sự thật rõ hơn và hệ thần kinh tập thể bớt hỗn loạn hơn.",
        "sections": [
            ("First Principles: Khủng Hoảng Là Gì?", "Khủng hoảng là tình huống có rủi ro cao, dữ kiện thiếu, thời gian ngắn và cảm xúc tập thể tăng mạnh.", [("Rủi ro", "Có thiệt hại thật"), ("Mơ hồ", "Chưa biết đủ"), ("Tốc độ", "Cần hành động"), ("Cảm xúc", "Sợ hãi lan nhanh")], ["Điều gì chắc chắn đúng?", "Điều gì chưa biết?", "Quyết định nào không thể chờ?"]),
            ("Phản Ứng Sinh Tồn Trong Khủng Hoảng", "Con người có thể chiến đấu, bỏ chạy, đóng băng hoặc làm hài lòng quyền lực.", [("Fight", "Đổ lỗi, công kích"), ("Flight", "Né trách nhiệm"), ("Freeze", "Không quyết được"), ("Fawn", "Nói điều lãnh đạo muốn nghe")], ["Tôi và team đang ở phản ứng nào?", "Ai đang im vì sợ?", "Cần tạo an toàn hay tạo quyết đoán?"]),
            ("Panic Và Tin Đồn", "Khi thiếu thông tin chính thức, tổ chức tự tạo câu chuyện để giảm mơ hồ.", [("Khoảng trống thông tin", "Tin đồn lấp vào"), ("Cảm xúc mạnh", "Tin xấu lan nhanh"), ("Thiếu niềm tin", "Thông điệp chính thức bị nghi ngờ")], ["Chúng ta đang để khoảng trống nào?", "Ai cần cập nhật ngay?", "Nhịp thông tin tiếp theo là khi nào?"]),
            ("Ra Quyết Định Dưới Áp Lực", "Không phải quyết định nào trong khủng hoảng cũng cần quyết ngay; cần phân loại theo thời gian và khả năng đảo ngược.", [("24 giờ", "An toàn, tiền mặt, pháp lý, truyền thông"), ("7 ngày", "Nguồn lực, người, khách hàng"), ("30 ngày", "Cấu trúc, chiến lược, học lại")], ["Quyết định này có đảo ngược không?", "Nếu sai, thiệt hại là gì?", "Dữ kiện tối thiểu cần có là gì?"]),
            ("Giao Tiếp Khủng Hoảng", "Thông điệp phải ngắn, thật, có nhịp và nói rõ điều biết/chưa biết.", [("Sự thật", "Không tô hồng"), ("Ưu tiên", "3 việc quan trọng nhất"), ("Vai trò", "Ai làm gì"), ("Nhịp", "Khi nào cập nhật tiếp")], ["Thông điệp có giảm mơ hồ không?", "Có nói rõ điều chưa biết không?", "Có hành động cụ thể không?"]),
            ("Đổ Lỗi Và Che Giấu", "Dưới sợ hãi, con người bảo vệ mình trước khi bảo vệ sự thật.", [("Đổ lỗi", "Giảm xấu hổ"), ("Che giấu", "Tránh bị phạt"), ("Narrative đẹp", "Giữ hình ảnh")], ["Chúng ta đang xử lý vấn đề hay xử lý người báo tin?", "Sai lầm nào cần học, sai lầm nào cần accountability?", "Tin xấu có an toàn không?"]),
            ("Phục Hồi Sau Khủng Hoảng", "Sau khủng hoảng, tổ chức cần xử lý dữ kiện, cảm xúc, niềm tin và hệ thống.", [("Review", "Điều gì đúng/sai"), ("Cảm xúc", "Ai bị tổn thương/kiệt sức"), ("Hệ thống", "Điểm yếu nào lộ ra"), ("Niềm tin", "Cần sửa chữa ở đâu")], ["Chúng ta học gì?", "Ai cần được phục hồi?", "Hệ thống nào phải đổi?"]),
        ],
        "tools": [("Bảng điều hành 72 giờ", ["Điều chắc chắn:", "Điều chưa biết:", "Rủi ro lớn nhất:", "Quyết định cần ngay:", "Owner:", "Thông điệp tiếp theo:"]), ("Checklist giao tiếp khủng hoảng", ["Thật không?", "Ngắn không?", "Có ưu tiên không?", "Có nhịp cập nhật không?", "Có giảm tin đồn không?"])],
        "weeks": ["Review một khủng hoảng cũ bằng bản đồ 72 giờ.", "Thiết kế mẫu thông điệp khủng hoảng.", "Lập danh sách quyết định không thể chờ trong ngành của bạn.", "Tập post-mortem không đổ lỗi."],
        "summary": [("Khủng hoảng", "Rủi ro + mơ hồ + tốc độ + cảm xúc", "Điều gì chắc chắn đúng?"), ("Panic", "Cảm xúc lan trong thiếu rõ ràng", "Khoảng trống nào cần lấp?"), ("Quyết định", "Phân loại theo thời gian/rủi ro", "Cần quyết gì bây giờ?"), ("Phục hồi", "Học + sửa hệ thống + sửa niềm tin", "Sau khủng hoảng cần chữa gì?")],
        "final": "Lãnh đạo khủng hoảng không phải là không sợ; đó là khả năng tạo rõ ràng và hành động có kỷ luật khi mọi người đang bị sợ hãi kéo đi.",
    },
    {
        "n": 37,
        "file": "Tap-37-Tam-ly-sang-tao-truc-giac-va-doi-moi.md",
        "title": "Tâm Lý Sáng Tạo, Trực Giác Và Đổi Mới",
        "subtitle": "Hiểu insight, flow, chịu mơ hồ, sợ sai và cách tổ chức nuôi hoặc giết sáng tạo",
        "why": ["Sáng tạo là năng lực sống còn trong môi trường biến động.", "Người lãnh đạo cần biết khi nào dùng phân tích, khi nào tạo không gian cho insight.", "Tổ chức thường nói muốn đổi mới nhưng thưởng cho an toàn.", "Hiểu sáng tạo giúp thiết kế sản phẩm, chiến lược và văn hóa học hỏi tốt hơn."],
        "remember": "Sáng tạo là khả năng tạo kết nối mới có giá trị trong điều kiện chưa rõ ràng.",
        "sections": [
            ("First Principles: Sáng Tạo Là Gì?", "Sáng tạo không phải chỉ là ý tưởng lạ; nó là ý tưởng mới đủ hữu ích trong một bối cảnh cụ thể.", [("Mới", "Không lặp lại cách cũ"), ("Hữu ích", "Giải quyết vấn đề thật"), ("Bối cảnh", "Phù hợp thời điểm và nguồn lực")], ["Ý tưởng này mới ở đâu?", "Nó giải quyết vấn đề nào?", "Ai được lợi nếu nó đúng?"]),
            ("Não Sáng Tạo", "Sáng tạo cần cả thả lỏng để kết nối và tập trung để chọn lọc.", [("Divergent", "Mở nhiều khả năng"), ("Convergent", "Chọn và tinh chỉnh"), ("Incubation", "Để não xử lý nền"), ("Execution", "Biến ý tưởng thành thực tế")], ["Tôi đang cần mở rộng hay thu hẹp?", "Tôi có cho não thời gian ủ không?", "Ý tưởng có được thử trong thực tế không?"]),
            ("Trực Giác", "Trực giác là kinh nghiệm được nén lại, đáng tin khi có domain experience và phản hồi thật.", [("Đáng tin", "Môi trường quen, feedback nhanh"), ("Nguy hiểm", "Môi trường mới, cảm xúc mạnh"), ("Ứng dụng", "Dùng trực giác tạo giả thuyết, không thay kiểm chứng")], ["Trực giác này đến từ kinh nghiệm hay sợ hãi?", "Có dữ kiện nào kiểm tra được không?", "Nếu sai, cái giá là gì?"]),
            ("Flow", "Flow xuất hiện khi thử thách vừa đủ cao, kỹ năng vừa đủ tốt và phản hồi rõ.", [("Quá dễ", "Chán"), ("Quá khó", "Lo"), ("Vừa tầm", "Tập trung sâu")], ["Việc nào đưa tôi vào flow?", "Tôi có block thời gian đủ sâu không?", "Phản hồi có đủ nhanh không?"]),
            ("Sợ Sai Và Sáng Tạo", "Không có an toàn để sai nhỏ thì tổ chức sẽ tạo sai lớn hoặc không đổi mới.", [("Sai học được", "Thử nghiệm nhỏ"), ("Sai cẩu thả", "Thiếu chuẩn"), ("Sai bị phạt", "Không ai thử")], ["Sai lầm nào được phép?", "Thử nghiệm có giới hạn rủi ro không?", "Ta phạt học hỏi hay phạt cẩu thả?"]),
            ("Tổ Chức Giết Sáng Tạo Như Thế Nào?", "Sáng tạo chết khi mọi thứ bị đo ngắn hạn, phê bình sớm và quyền lực quyết định trước dữ kiện.", [("KPI ngắn", "Không ai thử dài hạn"), ("Họp phán xét", "Ý tưởng non bị giết"), ("Sếp thích đúng", "Người khác ngừng nghĩ")], ["Chúng ta thưởng học hỏi hay chỉ thưởng kết quả ngắn?", "Ai được quyền có ý tưởng?", "Ý tưởng được bảo vệ khi còn non không?"]),
            ("Thiết Kế Đổi Mới", "Đổi mới cần pipeline: quan sát, giả thuyết, prototype, thử nhỏ, học, scale.", [("Quan sát", "Vấn đề thật"), ("Prototype", "Phiên bản đủ học"), ("Pilot", "Rủi ro nhỏ"), ("Scale", "Khi có bằng chứng")], ["Giả thuyết là gì?", "Thử nhỏ nhất là gì?", "Dữ kiện nào cho phép scale?"]),
        ],
        "tools": [("Canvas ý tưởng", ["Vấn đề thật:", "Người bị đau:", "Insight:", "Ý tưởng:", "Giả thuyết:", "Thử nghiệm nhỏ:", "Dữ kiện thành công:"]), ("Audit môi trường sáng tạo", ["Có thời gian deep work không?", "Có phạt sai nhỏ không?", "Có phản biện quá sớm không?", "Có cơ chế pilot không?"])],
        "weeks": ["Ghi 10 vấn đề thật trước khi nghĩ giải pháp.", "Tạo 3 ý tưởng xấu để mở não.", "Chạy một prototype nhỏ.", "Review một cơ chế tổ chức đang giết sáng tạo."],
        "summary": [("Sáng tạo", "Kết nối mới có giá trị", "Nó giải quyết vấn đề nào?"), ("Trực giác", "Kinh nghiệm nén lại", "Có đáng tin trong bối cảnh này không?"), ("Flow", "Thử thách vừa tầm + phản hồi", "Việc nào tạo flow?"), ("Đổi mới", "Thử nhỏ rồi học", "Pilot tối thiểu là gì?")],
        "final": "Đổi mới không bắt đầu bằng khẩu hiệu sáng tạo; nó bắt đầu bằng quyền được nhìn vấn đề thật, thử nhỏ và học nhanh mà không bị cái tôi giết sớm.",
    },
    {
        "n": 38,
        "file": "Tap-38-Tam-ly-danh-tinh-ban-nga-va-tai-thiet-con-nguoi.md",
        "title": "Tâm Lý Danh Tính, Bản Ngã Và Tái Thiết Con Người",
        "subtitle": "Hiểu câu hỏi 'tôi là ai', vai trò xã hội, bản sắc nghề nghiệp, khủng hoảng bản ngã và cách tái thiết sau thành công",
        "why": ["Sau tuổi 40, vấn đề thường không chỉ là mục tiêu mà là bản sắc.", "Người thành công dễ bị vai trò nghề nghiệp nuốt mất con người thật.", "Tái thiết bản sắc giúp đổi hành vi bền hơn đổi mục tiêu.", "Hiểu danh tính giúp lãnh đạo qua thay đổi, chuyển giao và khủng hoảng."],
        "remember": "Danh tính là câu chuyện mình tin về mình; khi câu chuyện đổi, hành vi và giới hạn cũng đổi.",
        "sections": [
            ("First Principles: Danh Tính Là Gì?", "Danh tính là tập hợp câu trả lời sống động cho câu hỏi: tôi là ai, thuộc về đâu, có giá trị vì điều gì.", [("Vai trò", "CEO, cha/mẹ, vợ/chồng"), ("Giá trị", "Điều tôi chọn khi khó"), ("Câu chuyện", "Tôi từng là ai, đang là ai"), ("Tương lai", "Tôi đang trở thành ai")], ["Tôi đang sống theo vai nào?", "Vai này có còn đúng không?", "Tôi muốn trở thành ai?"]),
            ("Bản Sắc Nghề Nghiệp", "Công việc cho ý nghĩa và vị trí, nhưng nguy hiểm khi nó trở thành toàn bộ cái tôi.", [("Lành mạnh", "Tôi làm vai trò này"), ("Nguy hiểm", "Tôi là vai trò này"), ("Khủng hoảng", "Mất vai trò là mất bản thân")], ["Nếu rời chức danh, tôi còn là ai?", "Tôi có đời sống ngoài vai trò không?", "Tôi có đang hy sinh con người cho hình ảnh nghề nghiệp?"]),
            ("Vai Cũ Và Bản Sắc Sinh Tồn", "Nhiều bản sắc được tạo để sống sót: người giỏi, người gánh vác, người kiểm soát, người làm hài lòng.", [("Người giỏi", "Sợ không đủ giá trị"), ("Người gánh", "Sợ mọi thứ sụp"), ("Người kiểm soát", "Sợ bất an"), ("Người làm hài lòng", "Sợ bị bỏ")], ["Vai này từng bảo vệ tôi thế nào?", "Nó đang làm tôi mất gì?", "Vai mới trưởng thành hơn là gì?"]),
            ("Khủng Hoảng Bản Sắc", "Khủng hoảng xảy ra khi câu chuyện cũ không còn chứa được đời sống mới.", [("Sau thành công", "Không biết tiếp theo là gì"), ("Sau thất bại", "Không biết mình còn giá trị không"), ("Sau mất mát", "Không biết sống như ai")], ["Câu chuyện cũ nào đã hết hạn?", "Tôi đang cố cứu vai cũ hay sinh ra vai mới?", "Điều gì vẫn là giá trị lõi?"]),
            ("Tái Thiết Bản Sắc", "Không tái thiết bằng suy nghĩ lớn, mà bằng hành vi nhỏ lặp lại chứng minh câu chuyện mới.", [("Tên gọi mới", "Tôi là người..."), ("Hành vi chứng minh", "Làm mỗi ngày"), ("Môi trường mới", "Người và nhịp sống hỗ trợ"), ("Ritual", "Đánh dấu chuyển giai đoạn")], ["Bản sắc mới là gì?", "Hành vi nhỏ nào chứng minh?", "Môi trường nào làm bản sắc mới dễ sống?"]),
            ("Danh Tính Trong Lãnh Đạo", "Tổ chức cũng có danh tính: chúng ta là ai, không là ai, chơi cuộc chơi nào.", [("Danh tính rõ", "Quyết định nhanh hơn"), ("Danh tính mơ hồ", "Cơ hội nào cũng hấp dẫn"), ("Danh tính giả", "Slogan khác hành vi")], ["Công ty chúng ta thật sự là ai?", "Điều gì không làm dù có lợi?", "Hành vi nào chứng minh danh tính đó?"]),
        ],
        "tools": [("Bản đồ danh tính", ["Tôi từng là:", "Tôi đang là:", "Tôi không còn muốn là:", "Tôi muốn trở thành:", "Hành vi chứng minh:"]), ("Audit vai trò", ["Vai trò:", "Điều vai này cho tôi:", "Điều vai này lấy đi:", "Giá trị lõi còn lại:", "Cách sống vai này trưởng thành hơn:"])],
        "weeks": ["Viết 5 câu 'Tôi là người...'.", "Chọn một bản sắc cũ đã hết hạn.", "Thiết kế 1 hành vi nhỏ cho bản sắc mới.", "Tạo một nghi thức đánh dấu chuyển đổi."],
        "summary": [("Danh tính", "Câu chuyện tôi là ai", "Câu chuyện này còn đúng không?"), ("Vai trò", "Một phần của tôi, không phải toàn bộ", "Tôi có bị vai trò nuốt không?"), ("Khủng hoảng", "Câu chuyện cũ hết hạn", "Giá trị nào vẫn còn?"), ("Tái thiết", "Hành vi nhỏ chứng minh bản sắc mới", "Tôi làm gì hôm nay?")],
        "final": "Tái thiết con người không phải phủ nhận quá khứ; đó là giữ phần giá trị và thôi sống trong vai đã hết hạn.",
    },
    {
        "n": 39,
        "file": "Tap-39-Tam-ly-trung-nien-lao-hoa-va-nua-sau-cuoc-doi.md",
        "title": "Tâm Lý Trung Niên, Lão Hóa Và Nửa Sau Cuộc Đời",
        "subtitle": "Hiểu khủng hoảng trung niên, sợ già, mất vai trò, chuyển từ chinh phục sang chiều sâu, di sản và bình an",
        "why": ["Sau 40 tuổi, câu hỏi tâm lý đổi từ 'làm sao thắng' sang 'thắng để làm gì'.", "Năng lượng, cơ thể, vai trò gia đình và ý nghĩa đều thay đổi.", "Không chuẩn bị cho nửa sau cuộc đời dễ dẫn đến trống rỗng sau thành công.", "Lão hóa trưởng thành là chuyển từ chứng minh sang truyền thừa và chiều sâu."],
        "remember": "Nửa sau cuộc đời không phải là đoạn giảm tốc; đó là cơ hội chuyển từ mở rộng bên ngoài sang trưởng thành bên trong.",
        "sections": [
            ("First Principles: Trung Niên Là Gì?", "Trung niên là giai đoạn con người đối diện giới hạn: thời gian, cơ thể, vai trò, cái chết và ý nghĩa.", [("Thời gian", "Không còn vô hạn"), ("Cơ thể", "Không thể vay mãi"), ("Vai trò", "Con cái lớn, cha mẹ già, sự nghiệp đổi"), ("Ý nghĩa", "Câu hỏi sâu hơn")], ["Tôi đang né giới hạn nào?", "Điều gì không còn có thể trì hoãn?", "Nửa sau muốn phục vụ giá trị nào?"]),
            ("Khủng Hoảng Trung Niên", "Khủng hoảng xảy ra khi thành công cũ không còn trả lời được câu hỏi hiện tại.", [("Trống rỗng", "Đạt rồi nhưng không đủ"), ("Bốc đồng", "Muốn cảm thấy sống"), ("So sánh", "Sợ tụt lại"), ("Hối tiếc", "Nhìn lại điều đã bỏ lỡ")], ["Tôi đang đau vì thiếu gì?", "Tôi muốn thay đổi thật hay chỉ muốn trốn cảm giác già?", "Điều gì cần được tiếc thương?"]),
            ("Sợ Già Và Sợ Mất Vai Trò", "Sợ già thường là sợ mất hấp dẫn, năng lực, quyền lực, tự do hoặc được cần đến.", [("Mất năng lượng", "Không còn như trước"), ("Mất vị trí", "Người trẻ thay thế"), ("Mất kiểm soát", "Cơ thể và đời sống đổi"), ("Mất ý nghĩa", "Không biết mình còn để làm gì")], ["Tôi sợ mất điều gì nhất?", "Có phần nào cần chấp nhận thay vì chống?", "Tôi có thể chuyển vai ra sao?"]),
            ("Từ Chinh Phục Sang Chiều Sâu", "Nửa đầu thường xây năng lực và vị trí; nửa sau cần tích hợp, truyền thừa và bình an.", [("Chinh phục", "Mở rộng, đạt thêm"), ("Tích hợp", "Hiểu mình, chọn lọc"), ("Truyền thừa", "Trao lại năng lực"), ("Bình an", "Không cần chứng minh liên tục")], ["Tôi còn đang chinh phục vì giá trị hay thói quen?", "Tôi muốn truyền lại điều gì?", "Điều gì làm đời sống sâu hơn?"]),
            ("Cha Mẹ Già Và Con Cái Lớn", "Trung niên là giai đoạn bị kéo giữa hai thế hệ: chăm cha mẹ và thả con ra đời.", [("Cha mẹ già", "Đối diện mất mát"), ("Con lớn", "Học buông kiểm soát"), ("Bản thân", "Cần đời sống riêng")], ["Tôi cần ranh giới chăm sóc nào?", "Tôi đang để con trưởng thành hay giữ con cho mình?", "Tôi cần chuẩn bị cho mất mát nào?"]),
            ("Di Sản", "Di sản không chỉ là tài sản; là con người, giá trị, hệ thống, ký ức và ảnh hưởng còn lại.", [("Tài sản", "Nguồn lực"), ("Con người", "Người mình nâng lên"), ("Giá trị", "Điều được sống tiếp"), ("Hệ thống", "Thứ vận hành sau mình")], ["Nếu 10 năm nữa nhìn lại, tôi muốn tự hào vì điều gì?", "Ai mạnh hơn vì tôi từng ở đây?", "Giá trị nào tôi muốn truyền lại?"]),
        ],
        "tools": [("Audit nửa sau cuộc đời", ["Điều tôi đã đạt:", "Điều tôi đã bỏ lỡ:", "Điều cần tiếc thương:", "Điều cần buông:", "Điều cần xây tiếp:", "Di sản muốn để lại:"]), ("Bản đồ năng lượng tuổi trung niên", ["Nguồn năng lượng:", "Thứ làm cạn:", "Thói quen phải đổi:", "Quan hệ cần ưu tiên:", "Lịch phục hồi:"])],
        "weeks": ["Viết thư cho chính mình 10 năm tới.", "Chọn một điều cần buông khỏi bản sắc cũ.", "Có một cuộc trò chuyện sâu với cha mẹ/con cái/người thân.", "Thiết kế một hành động di sản nhỏ."],
        "summary": [("Trung niên", "Đối diện giới hạn và ý nghĩa", "Tôi đang né giới hạn nào?"), ("Khủng hoảng", "Câu hỏi cũ không còn đủ", "Tôi thiếu gì thật sự?"), ("Lão hóa", "Mất và chuyển hóa", "Tôi sợ mất điều gì?"), ("Di sản", "Ảnh hưởng còn lại", "Ai mạnh hơn vì tôi?")],
        "final": "Nửa sau cuộc đời trưởng thành bắt đầu khi ta thôi chỉ hỏi còn đạt được gì, và bắt đầu hỏi điều gì đáng để mình trở thành.",
    },
    {
        "n": 40,
        "file": "Tap-40-Tam-ly-tam-linh-niem-tin-va-su-buong-bo.md",
        "title": "Tâm Lý Tâm Linh, Niềm Tin Và Sự Buông Bỏ",
        "subtitle": "Hiểu nhu cầu kết nối với điều lớn hơn bản thân: niềm tin, thiền định, lòng biết ơn, khiêm nhường, cái chết và buông bỏ",
        "why": ["Con người không chỉ cần hiệu suất và thành công; con người cần ý nghĩa tối hậu.", "Sau nhiều thành tựu, câu hỏi về cái chết, khổ đau và bình an trở nên thực tế hơn.", "Tâm linh có thể được hiểu như nhu cầu kết nối với điều lớn hơn bản ngã, không nhất thiết phải theo tôn giáo.", "Buông bỏ là năng lực tâm lý quan trọng để không bị kiểm soát bởi sợ hãi và ham muốn."],
        "remember": "Tâm linh trưởng thành không làm con người trốn đời; nó giúp con người sống trong đời với ít bản ngã, nhiều ý nghĩa và nhiều tự do hơn.",
        "sections": [
            ("First Principles: Tâm Linh Là Gì?", "Tâm linh là trải nghiệm kết nối với điều lớn hơn cái tôi cá nhân: sự sống, giá trị, cộng đồng, thiên nhiên, thần linh hoặc ý nghĩa tối hậu.", [("Không tôn giáo", "Kết nối, biết ơn, hiện diện"), ("Có tôn giáo", "Niềm tin, nghi lễ, cộng đồng"), ("Méo mó", "Dùng tâm linh để né trách nhiệm")], ["Điều gì làm tôi thấy mình nhỏ lại nhưng rộng hơn?", "Niềm tin này làm tôi trưởng thành hay trốn tránh?", "Tâm linh của tôi có đi cùng đạo đức không?"]),
            ("Niềm Tin", "Niềm tin giúp con người chịu đựng bất định, đau khổ và giới hạn của kiểm soát.", [("Niềm tin sống", "Tạo can đảm và trách nhiệm"), ("Niềm tin cứng", "Không chịu sự thật"), ("Niềm tin vay mượn", "Theo nhóm nhưng không tự hiểu")], ["Niềm tin này giúp tôi yêu thương hơn không?", "Nó có làm tôi phủ nhận dữ kiện không?", "Tôi có sống điều mình tin không?"]),
            ("Thiền Định Và Hiện Diện", "Thiền là tập quan sát mà không bị cuốn hoàn toàn vào suy nghĩ, cảm xúc và ham muốn.", [("Chú ý", "Quay về hiện tại"), ("Khoảng cách", "Thấy suy nghĩ là suy nghĩ"), ("Tự chủ", "Không phản ứng ngay")], ["Tôi có thể ngồi yên với chính mình không?", "Cảm xúc nào tôi luôn muốn chạy khỏi?", "Tôi có đang sống hay chỉ xử lý việc?"]),
            ("Lòng Biết Ơn Và Khiêm Nhường", "Biết ơn giúp não thấy điều đang có; khiêm nhường giúp cái tôi bớt phóng đại vai trò của mình.", [("Biết ơn", "Giảm thiếu thốn"), ("Khiêm nhường", "Thấy mình là một phần"), ("Kiêu ngạo", "Quên sự hỗ trợ và may mắn")], ["Tôi đang xem điều gì là hiển nhiên?", "Ai đã góp vào đời tôi?", "Tôi có nhớ mình không tự tạo ra tất cả không?"]),
            ("Cái Chết", "Cái chết làm rõ ưu tiên vì nó đặt giới hạn cuối cùng cho thời gian và cái tôi.", [("Né cái chết", "Sống như còn vô hạn"), ("Ám ảnh cái chết", "Sợ hãi tê liệt"), ("Nhìn thẳng", "Chọn điều đáng sống")], ["Nếu thời gian ngắn hơn tôi tưởng, điều gì quan trọng?", "Tôi muốn sửa quan hệ nào?", "Tôi đang trì hoãn đời sống nào?"]),
            ("Buông Bỏ", "Buông bỏ không phải bỏ cuộc; là thôi nắm chặt điều không còn thuộc quyền kiểm soát hoặc không còn phục vụ giá trị.", [("Buông kiểm soát", "Chấp nhận giới hạn"), ("Buông vai cũ", "Cho bản sắc mới sinh ra"), ("Buông oán", "Không để quá khứ cầm lái")], ["Tôi đang nắm điều gì vì sợ?", "Nếu buông, tôi sợ mất gì?", "Tôi có thể hành động hết phần mình rồi thả phần còn lại không?"]),
            ("Tâm Linh Và Lãnh Đạo", "Lãnh đạo có chiều sâu cần khiêm nhường trước sự thật, trách nhiệm với quyền lực và ý thức về di sản.", [("Ít bản ngã", "Nghe sự thật tốt hơn"), ("Nhiều ý nghĩa", "Dẫn người qua khó khăn"), ("Có đạo đức", "Không dùng niềm tin để thao túng")], ["Quyền lực của tôi phục vụ điều gì lớn hơn tôi?", "Tôi có đủ khiêm nhường để học không?", "Di sản tinh thần của tôi là gì?"]),
        ],
        "tools": [("Nhật ký biết ơn sâu", ["Điều tôi biết ơn:", "Ai đã góp phần:", "Tôi thường xem nhẹ điều gì:", "Tôi sẽ đáp lại bằng hành động nào:"]), ("Bài tập buông bỏ", ["Điều tôi đang nắm:", "Tôi sợ mất:", "Phần tôi kiểm soát:", "Phần không kiểm soát:", "Hành động hết phần mình:", "Cách buông phần còn lại:"])],
        "weeks": ["Thực hành 5 phút hiện diện mỗi ngày.", "Viết 10 điều biết ơn không liên quan thành tích.", "Có một cuộc trò chuyện về cái chết/di sản với người tin cậy.", "Chọn một điều cần buông và làm nghi thức nhỏ."],
        "summary": [("Tâm linh", "Kết nối với điều lớn hơn cái tôi", "Niềm tin này làm tôi trưởng thành không?"), ("Hiện diện", "Quan sát mà không bị cuốn", "Tôi đang chạy khỏi cảm xúc nào?"), ("Biết ơn", "Thấy điều đang có", "Tôi xem nhẹ điều gì?"), ("Buông bỏ", "Thôi nắm điều không còn phục vụ", "Tôi đang nắm vì giá trị hay sợ?")],
        "final": "Khi cái tôi bớt cần kiểm soát tất cả, con người có thể sống sâu hơn, yêu rộng hơn và ra đi nhẹ hơn.",
    },
]


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)


def code(lines):
    return "```text\n" + "\n".join(lines) + "\n```"


def render_tap(t):
    rows = [
        ("Hiểu bản chất", "Không chỉ nhớ thuật ngữ"),
        ("Nhận diện trong đời sống", "Thấy được khi nó đang xảy ra"),
        ("Ứng dụng vào lãnh đạo/quan hệ", "Chuyển hiểu biết thành hành động"),
        ("Tự soi chiếu", "Không dùng kiến thức chỉ để phán xét người khác"),
        ("Giữ đạo đức", "Tác động đến người khác mà vẫn tôn trọng phẩm giá"),
    ]
    parts = [
        f"# Tập {t['n']}: {t['title']}",
        "",
        f"**{t['subtitle']}**  ",
        "Giáo trình ngắn gọn cho người trưởng thành, cấp quản lý/C-level",
        "",
        "---",
        "",
        f"## 0. Vì Sao C-level Cần Học {t['title']}?",
        "",
        "### Bản chất",
        "",
        *[f"- {item}" for item in t["why"]],
        "",
        "### Một câu cần nhớ",
        "",
        f"> {t['remember']}",
        "",
        "### Mục tiêu tập này",
        "",
        table(["Năng lực", "Ý nghĩa thực tế"], rows),
        "",
        "---",
    ]
    for idx, (title, essence, rows2, questions) in enumerate(t["sections"], 1):
        parts += [
            "",
            f"## {idx}. {title}",
            "",
            "### Bản chất",
            "",
            essence,
            "",
            "### Bảng đọc nhanh",
            "",
            table(["Khía cạnh", "Ý nghĩa"], rows2),
            "",
            "### Câu hỏi áp dụng",
            "",
            code(questions),
            "",
            "### Nguyên tắc",
            "",
            f"> Đừng dùng chủ đề này để dán nhãn con người; hãy dùng nó để nhìn rõ cơ chế và chọn phản ứng trưởng thành hơn.",
            "",
            "---",
        ]
    parts += ["", f"## {len(t['sections']) + 1}. Công Cụ Thực Hành", ""]
    for name, lines in t["tools"]:
        parts += [f"### {name}", "", code(lines), ""]
    parts += ["---", "", f"## {len(t['sections']) + 2}. Lộ Trình Thực Hành 4 Tuần", ""]
    for i, week in enumerate(t["weeks"], 1):
        parts += [f"### Tuần {i}", "", f"- {week}", "- Ghi lại một quan sát thật trong đời sống/công việc.", ""]
    parts += [
        "---",
        "",
        f"## {len(t['sections']) + 3}. Bảng Tóm Tắt First Principles",
        "",
        table(["Chủ đề", "Bản chất", "Câu hỏi áp dụng"], t["summary"]),
        "",
        "---",
        "",
        f"## {len(t['sections']) + 4}. Một Câu Để Nhớ Toàn Bộ Tập {t['n']}",
        "",
        f"> {t['final']}",
        "",
    ]
    return "\n".join(parts)


def main():
    for tap in TAPS:
        path = ROOT / tap["file"]
        path.write_text(render_tap(tap), encoding="utf-8")
        print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
