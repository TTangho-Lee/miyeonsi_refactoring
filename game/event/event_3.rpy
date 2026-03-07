label event_3:
    menu:
        "쌍화차를 마신다.":
            "{cps=[text_speed]}쌍화차를 받아 마신다. 따뜻한 기운이 퍼진다.{/cps}"
            $ apply_affinity_change("character_3", 2)
            $ send_notification(f"{character_3_name} 호감도 +2 (현재: {character_3_affinity})")
            
            # ----------------------------------------------------
            # 분기 1: 쌍화차를 마셨을 때 character_3의 반응
            # ----------------------------------------------------
            if character_3_id == "dawon":
                $ typing(character_3, "어때? 맛있어?")
            elif character_3_id == "jiwoo":
                $ typing(character_3, "다행이다~ 입맛에 안 맞으면 어쩌나 은근 걱정했거든.")
            elif character_3_id == "suah":
                $ typing(character_3, "와, 다행이에요! 선배님 안 드시면 어쩌나 조마조마했어요!")
            elif character_3_id == "yeji":
                $ typing(character_3, "헤헤, 다행이다. 선배가 안 드시면 제가 두 잔 다 마셔야 하나 고민했거든요.")
            elif character_3_id == "huieun":
                $ typing(character_3, "휴, 다행이에요! 선배님 입맛에 안 맞을까 봐 엄청 걱정했거든요.")
            else:
                $ typing(character_3, "다행이다. 안 마시면 좀 애매해질 뻔했거든.")
                
            jump talk_4
            
        "마시지 않는다.":
            # ----------------------------------------------------
            # 분기 2: 쌍화차를 거절했을 때 character_3의 반응
            # ----------------------------------------------------
            if character_3_id == "dawon":
                $ typing(character_3, "마시기 싫으면 이리 줘. 이제 안 사준다?")
            elif character_3_id == "jiwoo":
                $ typing(character_3, "아… 쌍화차는 별로 안 좋아하는구나? 알았어, 무리해서 안 마셔도 돼.")
            elif character_3_id == "suah":
                $ typing(character_3, "아… 그렇구나. 넵! 억지로 안 드셔도 괜찮아요!")
            elif character_3_id == "yeji":
                $ typing(character_3, "앗… 입맛에 안 맞으신가 보네요. 괜찮아요, 무리해서 안 드셔도 돼요!")
            elif character_3_id == "huieun":
                $ typing(character_3, "아… 쌍화차 안 좋아하시는구나… 넵, 알겠습니다!")
            else:
                $ typing(character_3, "아… 그렇구나. 뭐, 안 마셔도 되긴 해.")

            "{cps=[text_speed]}[character_3_name][iga(character_3_name)] 쌍화차를 잠시 바라보며 고개를 끄덕였다.{/cps}"
            jump talk_4