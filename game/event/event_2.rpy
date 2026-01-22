label event_2:
    menu:
        "먹는다":
            # --- 1. 식사 수락 및 이동 ---
            $ apply_affinity_change("sub_role2", 4)
            $ send_notification(f"{side2_char_name} 호감도 +4 (현재: {sub_role2_affinity})")
            
            $ typing(main_role, f"{side2_char_name}, 먹고 싶은 거 없어?")
            $ typing(sub_role2, "저, 햄버거요!")
            $ typing(user, "그러자.")
            
            scene bg restaurant with fade
            "식당에 도착했다."
            show sub_role2 normal at right
            $ typing(sub_role2, "뭐 드실래요?")

            # --- 2. 자유 대화 1: 메뉴 주문 ---
            $ talk_loop("sub_role2", "너의 역할은 [side2_char_name]야. 햄버거 가게에 도착해서 메뉴를 고르고 주문하는 상황에서 [side2_char_name]가 뭐 먹을지 물어본 상황이다./ 플레이어가 뭘 먹을지 결정하면 종료된다.", last_char_line="뭐 드실래요?")

            # --- 3. 음식 나옴 및 대화 전환 ---
            "잠시 후, 주문한 음식이 나왔다."
            $ typing(sub_role2, "선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?")

            # --- 4. 자유 대화 2: 방과 후 일정 ---
            $ talk_loop_all_charactor("음식을 먹으며 방과 후 일정에 대해 이야기하는 상황이다. 플레이어의 말에 따라 반응하라./ 일정에 대한 대화를 3~5턴 정도 진행하면 종료된다.", last_char_line=f"{side2_char_name}: 선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?")
            hide sub_role2 normal
            jump talk_3

        "먹지 않는다":
            # --- 거절 루트 ---
            $ typing(sub_role2, "아… 그러면 저는 그냥 혼자 먹고 올게요…")
            $ typing(main_role, "뭐야. 안 먹는다고? 이상하네 진짜.")

            $ apply_affinity_change("sub_role2", -4)
            $ apply_affinity_change("main_role", -4)
            $ send_notification(f"{side2_char_name}, {main_char_name} 호감도 -4")

            "둘은 조금 어색한 분위기 속에서 자리를 떴다."
            jump talk_3