init python:
    import random
    import requests
    import json

    def talk_loop_all_charactor(finish_condition, max_turn=5, last_char_line=""):
        global player_name
        
        # 1. 캐릭터 ID(폴더명)와 슬롯 이름(dawon, jiwoo, suah) 매핑 [cite: 5, 20, 21]
        # AI가 'yuki'라고 대답하면 이를 'dawon'(메인 슬롯)으로 연결하기 위함입니다.
        id_to_slot = {
            store.role_main: "dawon",
            store.role_side1: "jiwoo",
            store.role_side2: "suah"
        }
        active_ids = list(id_to_slot.keys())
        
        summary = []
        if last_char_line:
            summary.append(last_char_line)

        turn_count = 0
        last_speaker_id = store.role_main # 시작 화자 (ID 기준)
        last_reply = ""

        # 초기 등장 연출 (슬롯 기반 태그 사용) [cite: 31, 32]
        # DynamicImage 설정 덕분에 슬롯 이름만 호출해도 실제 이미지가 나옵니다.
        renpy.show("dawon normal", at_list=[store.left])
        renpy.show("jiwoo normal", at_list=[store.center])
        renpy.show("suah normal", at_list=[store.right])

        while True:
            if turn_count >= max_turn + 2:
                return

            # 현재 화자의 슬롯을 찾아 데이터 가져오기 
            current_slot = id_to_slot[last_speaker_id]
            current_sys_prompt = getattr(store, f"system_prompt_{current_slot}")
            current_aff = getattr(store, f"{current_slot}_affinity")

            # 유저 선택지 생성 [cite: 45]
            choices = gemini_generate_choices(current_sys_prompt, summary, last_reply, current_aff, player_name, finish_condition)
            
            choice = renpy.display_menu([
                (choices[0], choices[0]),
                (choices[1], choices[1]),
                ("직접 입력", "direct_input")
            ])

            user_msg = renpy.input(f"{player_name}:").strip() if choice == "direct_input" else choice
            if not user_msg: continue

            turn_count += 1
            summary.append(f"user: {user_msg}")

            # 2. 다음 화자 결정 (AI가 참여자 ID 중 하나를 선택)
            next_char_id = ask_llm_for_next_character(active_ids, id_to_slot, summary, user_msg)
            
            # 3. 선택된 캐릭터의 슬롯 정보를 찾아 응답 생성 [cite: 5, 8]
            next_slot = id_to_slot[next_char_id]
            next_sys_prompt = getattr(store, f"system_prompt_{next_slot}")
            next_aff = getattr(store, f"{next_slot}_affinity")
            
            reply, emotion, summary_text, delta, is_sus, goal_achieved = gemini_generate_response(
                next_sys_prompt, summary, user_msg, next_aff, player_name, finish_condition
            )

            # 비주얼 업데이트: 해당 슬롯의 표정 변경 
            renpy.show(f"{next_slot} {emotion}")
            
            # 데이터 반영 [cite: 5, 12]
            apply_affinity_change(next_slot, delta)
            summary.append(f"{next_char_id}: {reply}")
            last_reply = reply
            last_speaker_id = next_char_id

            # 대사 출력 (슬롯 이름으로 Character 객체 호출) 
            target_char_obj = getattr(store, next_slot)
            safe_reply = reply.replace("{", "{{").replace("}", "}}")
            renpy.say(target_char_obj, "{cps=[text_speed]}%s{/cps}" % safe_reply)

            if goal_achieved:
                return

    def ask_llm_for_next_character(available_ids, id_to_slot, summary, user_msg):
        """Gemini에게 다음 대사를 할 캐릭터 ID를 물어보는 함수입니다."""
        global GEMINI_URL, GEMINI_API_KEY 

        summary_text = "\n".join(summary[-5:])
        
        # 참여자들의 실제 이름을 포함하여 AI가 상황을 더 잘 이해하게 합니다.
        char_info = ""
        for cid in available_ids:
            slot = id_to_slot[cid]
            name = getattr(store, f"{slot}_char_name") # 예: '임다원' [cite: 20]
            char_info += f"- {cid} (이름: {name})\n"

        prompt = f"""
        당신은 대화 제어 시스템입니다. 현재 대화 참여자 목록:
        {char_info}
        
        대화 흐름: {summary_text}
        유저의 마지막 말: {user_msg}
        
        위 캐릭터 ID 중 다음 대사를 하기에 가장 자연스러운 ID 하나만 골라 답변하세요.
        출력 형식: character: ID
        """

        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.3, "maxOutputTokens": 20}
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload), timeout=5)
            result = response.json()
            text = result["candidates"][0]["content"]["parts"][0]["text"].lower()
            
            if "character:" in text:
                res_id = text.split("character:")[1].strip()
                if res_id in available_ids:
                    return res_id
            return random.choice(available_ids)
        except:
            return random.choice(available_ids)