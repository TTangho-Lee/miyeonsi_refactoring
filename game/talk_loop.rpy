init python:
    def talk_loop(charactor, finish_condition, max_turn=3, last_char_line=""):
        global player_name, character_1_affinity, character_2_affinity, character_3_affinity, professor_affinity
        global character_1_prompt, character_2_prompt, character_3_prompt, system_prompt_professor
        emotion_map = {
            "normal": "normal",
            "smile": "smile",
            "sad": "sad",
            "shy": "shy",
            "angry": "angry",
        }
        all_emotions = ["normal", "smile", "sad", "shy", "angry"]
        summary = []
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트
        last_reply = last_char_line

        # 캐릭터별 초기 설정
        if charactor == character_1_id:
            current_affinity = character_1_affinity
            sys_prompt = character_1_prompt
        elif charactor == character_2_id:
            current_affinity = character_2_affinity
            sys_prompt = character_2_prompt
        elif charactor == character_3_id:
            current_affinity = character_3_affinity
            sys_prompt = character_3_prompt
        elif charactor == "professor":
            current_affinity = professor_affinity
            sys_prompt = system_prompt_professor

        while True:
            # [안전장치 1] 10턴이 넘어가면 강제 종료 (무한 루프 방지)
            if turn_count >= max_turn+2:
                return

            # AI를 통해 선택지 생성
            choices = gemini_generate_choices(sys_prompt, summary, last_reply, current_affinity, player_name, finish_condition)
            
            # 메뉴 표시
            choice = renpy.display_menu(
                [
                    (choices[0], choices[0]),
                    (choices[1], choices[1]),
                    ("직접 입력", "direct_input")
                ]
            )

            if choice == "direct_input":
                user_msg = renpy.input(f"{player_name}:").strip()
            else:
                user_msg = choice

            if user_msg == "":
                # 빈 입력은 턴 수에 포함하지 않거나, 그냥 넘어감
                continue
            
            turn_count += 1 # 유효한 대화 1턴 증가

            # [핵심 수정] 3턴 이상 진행되면 종료 유도 프롬프트 추가
            # finish_condition 문자열 뒤에 시스템 메시지를 덧붙여 LLM에게 종료를 압박합니다.
            current_condition = finish_condition
            if turn_count >= max_turn:
                current_condition = f"현재 대화가 {turn_count}턴 진행되었다. 대화가 마무리되는 대사를 입력하여라./ 반드시 'goal_achievement: true'를 출력하여 대화를 종료하여라."

            summary_text = "\n".join(summary) if summary else ""

            # AI 응답 생성
            # finish_condition 대신 수정된 current_condition을 전달합니다.
            reply, charactor_emotion, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )
            last_reply = reply # 다음 턴의 선택지 생성을 위해 현재 응답을 저장
            reply = reply.replace("{", "{{").replace("}", "}}")
            sentences=[s for s in split_sentences(reply)]
            # 요약 저장
            summary.append(f"user: {user_msg}")
            

            for emo in all_emotions:
                renpy.hide("character_1 " + emo)
                renpy.hide("character_2 " + emo)
                renpy.hide("character_3 " + emo)
                renpy.hide("professor " + emo)

            if charactor_emotion in emotion_map:
                show_expression = emotion_map[charactor_emotion]
                if charactor==character_1_id:
                    renpy.show("character_1 " + show_expression, at_list=[store.left])
                elif charactor==character_2_id:
                    renpy.show("character_2 " + show_expression, at_list=[store.center])
                elif charactor==character_3_id:
                    renpy.show("character_3 " + show_expression, at_list=[store.right])
                elif charactor=="professor":
                    renpy.show("professor " + show_expression, at_list=[store.center])

            if charactor == character_1_id:
                summary.append(f"{character_1_name}: {reply}")
                apply_affinity_change(character_1_id, affinity_delta)
                current_affinity = character_1_affinity
                for s in sentences:
                    # %, [, {, } 기호를 모두 이스케이프 처리하여 오류 방지
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(character_1, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == character_2_id:
                summary.append(f"{character_2_name}: {reply}")
                apply_affinity_change(character_2_id, affinity_delta)
                current_affinity = character_2_affinity
                for s in sentences:
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(character_2, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == character_3_id:
                summary.append(f"{character_3_name}: {reply}")
                apply_affinity_change(character_3_id, affinity_delta)
                current_affinity = character_3_affinity
                for s in sentences:
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(character_3, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "professor":
                summary.append(f"professor: {reply}")
                apply_affinity_change("professor", affinity_delta)
                current_affinity = professor_affinity
                for s in sentences:
                    safe_s = s.replace("%", "%%").replace("[", "[[").replace("{", "{{").replace("}", "}}")
                    renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)
            

            # [안전장치 2] 목표 달성 시 종료
            if goal_achieved:
                return

        return


    def talk_loop_center(charactor, finish_condition, max_turn=5, last_char_line=""):
        global player_name, character_1_affinity, character_2_affinity, character_3_affinity, professor_affinity
        global character_1_prompt, character_2_prompt, character_3_prompt, system_prompt_professor
        emotion_map = {
            "normal": "normal",
            "smile": "smile",
            "sad": "sad",
            "shy": "shy",
            "angry": "angry",
        }
        all_emotions = ["normal", "smile", "sad", "shy", "angry"]
        summary = []
        is_sus = False
        turn_count = 0  # [추가] 대화 턴 수 카운트
        last_reply = last_char_line

        # 캐릭터별 초기 설정
        if charactor == character_1_id:
            current_affinity = character_1_affinity
            sys_prompt = character_1_prompt
        elif charactor == character_2_id:
            current_affinity = character_2_affinity
            sys_prompt = character_2_prompt
        elif charactor == character_3_id:
            current_affinity = character_3_affinity
            sys_prompt = character_3_prompt
        elif charactor == "professor":
            current_affinity = professor_affinity
            sys_prompt = system_prompt_professor

        while True:
            # [안전장치 1] 10턴이 넘어가면 강제 종료 (무한 루프 방지)
            if turn_count >= max_turn+2:
                return

            # AI를 통해 선택지 생성
            choices = gemini_generate_choices(sys_prompt, summary, last_reply, current_affinity, player_name, finish_condition)
            
            # 메뉴 표시
            choice = renpy.display_menu(
                [
                    (choices[0], choices[0]),
                    (choices[1], choices[1]),
                    ("직접 입력", "direct_input")
                ]
            )

            if choice == "direct_input":
                user_msg = renpy.input(f"{player_name}:").strip()
            else:
                user_msg = choice

            if user_msg == "":
                # 빈 입력은 턴 수에 포함하지 않거나, 그냥 넘어감
                continue
            
            turn_count += 1 # 유효한 대화 1턴 증가

            # [핵심 수정] 3턴 이상 진행되면 종료 유도 프롬프트 추가
            # finish_condition 문자열 뒤에 시스템 메시지를 덧붙여 LLM에게 종료를 압박합니다.
            current_condition = finish_condition

            summary_text = "\n".join(summary) if summary else ""

            # AI 응답 생성
            # finish_condition 대신 수정된 current_condition을 전달합니다.
            reply, charactor_emotion, summary_text, affinity_delta, is_sus, goal_achieved = gemini_generate_response(
                sys_prompt, summary, user_msg, current_affinity, player_name, current_condition
            )
            last_reply = reply # 다음 턴의 선택지 생성을 위해 현재 응답을 저장
            reply = reply.replace("{", "{{").replace("}", "}}")
            sentences=[s for s in split_sentences(reply)]
            # 요약 저장
            summary.append(f"user: {user_msg}")
            

            for emo in all_emotions:
                renpy.hide("character_1 " + emo)
                renpy.hide("character_2 " + emo)
                renpy.hide("character_3 " + emo)
                renpy.hide("professor " + emo)

            if charactor_emotion in emotion_map:
                show_expression = emotion_map[charactor_emotion]
                if charactor==character_1_id:
                    renpy.show("character_1 " + show_expression, at_list=[store.center])
                elif charactor==character_2_id:
                    renpy.show("character_2 " + show_expression, at_list=[store.center])
                elif charactor==character_3_id:
                    renpy.show("character_3 " + show_expression, at_list=[store.center])
                elif charactor=="professor":
                    renpy.show("professor " + show_expression, at_list=[store.center])

            if charactor == character_1_id:
                summary.append(f"{character_1_name}: {reply}")
                apply_affinity_change(character_1_id, affinity_delta)
                current_affinity = character_1_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(character_1, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == character_2_id:
                summary.append(f"{character_2_name}: {reply}")
                apply_affinity_change(character_2_id, affinity_delta)
                current_affinity = character_2_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(character_2, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == character_3_id:
                summary.append(f"{character_3_name}: {reply}")
                apply_affinity_change(character_3_id, affinity_delta)
                current_affinity = character_3_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(character_3, "{cps=[text_speed]}%s{/cps}" % safe_s)
            elif charactor == "professor":
                summary.append(f"professor: {reply}")
                apply_affinity_change("professor", affinity_delta)
                current_affinity = professor_affinity
                for s in sentences:
                    safe_s = s.replace("{", "{{").replace("}", "}}")
                    renpy.say(professor, "{cps=[text_speed]}%s{/cps}" % safe_s)
            

            # [안전장치 2] 목표 달성 시 종료
            if goal_achieved:
                return

        return