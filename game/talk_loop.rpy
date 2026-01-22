init python:
    def talk_loop(char_id, sys_prompt, finish_condition, max_turn=3, last_char_line=""):
        global player_name
        # 캐릭터 ID와 매칭되는 객체 및 호감도 변수 매핑
        # character_definition.rpy에 정의된 역할 객체들을 사용합니다. [cite: 680]
        char_map = {
            "dawon": (store.dawon, "dawon_affinity"),
            "jiwoo": (store.jiwoo, "jiwoo_affinity"),
            "suah": (store.suah, "suah_affinity"),
            "professor": (store.professor, "professor_affinity"),
            "hobanwoo": (store.hobanwoo, "hobanwoo_affinity")
        }
        
        target_char, aff_var_name = char_map.get(char_id, (store.dawon, "dawon_affinity"))
        current_affinity = getattr(store, aff_var_name)
        
        summary = []
        turn_count = 0
        last_reply = last_char_line

        while True:
            if turn_count >= max_turn + 2: return

            # AI를 통해 선택지 생성 [cite: 735]
            choices = gemini_generate_choices(sys_prompt, summary, last_reply, current_affinity, player_name, finish_condition)
            
            choice = renpy.display_menu([
                (choices[0], choices[0]),
                (choices[1], choices[1]),
                ("직접 입력", "direct_input")
            ])

            user_msg = renpy.input(f"{player_name}:").strip() if choice == "direct_input" else choice
            if not user_msg: continue
            
            turn_count += 1
            current_condition = finish_condition
            if turn_count >= max_turn:
                current_condition = f"{finish_condition} / 대화가 길어졌으니 마무리 대사를 하고 반드시 'goal_achievement: true'를 출력해."

            # AI 응답 생성 [cite: 719]
            reply, emotion, summary_text, delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )
            
            # 비주얼 처리 (DynamicImage가 적용된 태그 사용) [cite: 695]
            renpy.hide(char_id) 
            renpy.show(f"{char_id} {emotion}", at_list=[store.center])

            summary.append(f"user: {user_msg}")
            summary.append(f"{char_id}: {reply}")
            
            # 호감도 반영 및 업데이트 [cite: 782]
            apply_affinity_change(char_id, delta)
            current_affinity = getattr(store, aff_var_name)
            last_reply = reply

            # 대사 출력 (텍스트 이스케이프 처리) [cite: 624]
            sentences = [s for s in split_sentences(reply)]
            for s in sentences:
                safe_s = s.replace("{", "{{").replace("}", "}}")
                renpy.say(target_char, "{cps=[text_speed]}%s{/cps}" % safe_s)

            if goal_achieved: return