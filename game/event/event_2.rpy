label event_2:
    menu:
        "먹는다":
            # --- 1. 식사 수락 및 이동 ---
            $ apply_affinity_change("character_2", 4)
            $ send_notification(f"{character_2_name} 호감도 +4 (현재: {character_2_affinity})")

            # character_1이 character_2에게 질문
            $ typing(character_1, f"{character_2_name}{a(character_2_name)}, 먹고 싶은 거 없어?")

            # ----------------------------------------------------
            # 분기 1: character_2가 대답 ("저, 햄버거요!")
            # ----------------------------------------------------
            if character_2_id == "dawon":
                $ typing(character_2, "난 햄버거!")
            elif character_2_id == "jiwoo":
                $ typing(character_2, "음~ 난 햄버거 먹을래!")
            elif character_2_id == "suah":
                $ typing(character_2, "저, 햄버거요!")
            elif character_2_id == "yeji":
                $ typing(character_2, "저는 무조건 햄버거 세트요!")
            elif character_2_id == "huieun":
                $ typing(character_2, "저 햄버거 엄청 땡겨요!")
            else:
                $ typing(character_2, "저, 햄버거요!")

            $ typing(user, "그러자.")
            
            scene bg restaurant with fade
            "식당에 도착했다."
            show character_2 normal at right

            # ----------------------------------------------------
            # 분기 2: character_2가 플레이어에게 되물음 ("뭐 드실래요?")
            # ----------------------------------------------------
            if character_2_id == "dawon":
                $ typing(character_2, f"{player_name}{eunneun(player_name)} 뭐 먹을래?")
            elif character_2_id == "jiwoo":
                $ typing(character_2, f"{player_name}{eunneun(player_name)} 뭐 먹고 싶어?")
            elif character_2_id == "suah":
                $ typing(character_2, "선배님은 뭐 드실래요?")
            elif character_2_id == "yeji":
                $ typing(character_2, "선배님은 뭐 드시고 싶으세요?")
            elif character_2_id == "huieun":
                $ typing(character_2, "선배님 메뉴는 고르셨어요?")
            else:
                $ typing(character_2, "뭐 드실래요?")

            # --- 2. 자유 대화 1: 메뉴 주문 ---
            $ talk_loop(character_2_id, f"너의 역할은 {character_2_name}{iya(character_2_name)}. 햄버거 가게에 도착해서 메뉴를 고르고 주문하는 상황에서 {character_2_name}{iga(character_2_name)} 뭐 먹을지 물어본 상황이다./ 플레이어가 뭘 먹을지 결정하면 종료된다.", last_char_line="뭐 드실래요?")
            
            # --- 3. 음식 나옴 및 대화 전환 ---
            "잠시 후, 주문한 음식이 나왔다."

            # --- 4. 자유 대화 2: 방과 후 일정 ---
            $ talk_loop_all_charactor("음식을 먹으며 방과 후 일정에 대해 이야기하는 상황이다. 플레이어의 말에 따라 반응하라./ 일정에 대한 대화를 3~5턴 정도 진행하면 종료된다.", last_char_line=f"{character_2_name}: 선배님들은 오늘 끝나고 뭐하세요? 일정 따로 있으세요?")
            hide character_2
            jump talk_3

        "먹지 않는다":
            # ----------------------------------------------------
            # 분기 3: character_2의 거절당한 반응 ("아… 그러면 혼자 먹고 올게요")
            # ----------------------------------------------------
            if character_2_id == "dawon":
                $ typing(character_2, "아… 그래? 그럼 나 대충 혼자 먹고 올게…")
            elif character_2_id == "jiwoo":
                $ typing(character_2, "아… 알았어. 그럼 나 혼자 금방 먹고 올게…")
            elif character_2_id == "suah":
                $ typing(character_2, "아… 그러면 저는 그냥 혼자 먹고 올게요…")
            elif character_2_id == "yeji":
                $ typing(character_2, "아… 넵. 그럼 저 혼자 후딱 다녀올게요…")
            elif character_2_id == "huieun":
                $ typing(character_2, "아아… 알겠습니다. 그럼 저 먼저 다녀오겠습니다…")
            else:
                $ typing(character_2, "아… 그러면 저는 그냥 혼자 먹고 올게요…")

            # ----------------------------------------------------
            # 분기 4: character_1의 반응 ("뭐야. 안 먹는다고? 이상하네 진짜.")
            # ----------------------------------------------------
            if character_1_id == "dawon":
                $ typing(character_1, "뭐야. 안 먹는다고? 이상하네 진짜.")
            elif character_1_id == "jiwoo":
                $ typing(character_1, "어머, 안 먹는다고? 웬일이래. 진짜 이상하네.")
            elif character_1_id == "suah":
                $ typing(character_1, "엥? 선배님 밥을 안 드신다고요? 평소랑 다르게 이상하네요 진짜.")
            elif character_1_id == "yeji":
                $ typing(character_1, "헐, 웬일로 밥을 거르세요? 진짜 이상하시네.")
            elif character_1_id == "huieun":
                $ typing(character_1, "앗, 안 드신다고요? 평소랑 다르게 이상하시네요 진짜.")
            else:
                $ typing(character_1, "뭐야. 안 먹는다고? 이상하네 진짜.")

            $ apply_affinity_change("character_2", -4)
            $ apply_affinity_change("character_1", -4)
            $ send_notification(f"{character_2_name}, {character_1_name} 호감도 -4")

            "둘은 조금 어색한 분위기 속에서 자리를 떴다."
            jump talk_3