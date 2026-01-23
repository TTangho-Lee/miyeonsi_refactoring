label event_3:
    menu:
        "쌍화차를 마신다.":
            "{cps=[text_speed]}쌍화차를 받아 마신다. 따뜻한 기운이 퍼진다.{/cps}"
            $ apply_affinity_change("character_3", 2)
            $ send_notification(f"{character_3_name} 호감도 +2 (현재: {character_3_affinity})")
            $ typing(character_3, "다행이다. 안 마시면 좀 애매해질 뻔했거든.")
            jump talk_4
        "마시지 않는다.":
            $ typing(character_3, "아… 그렇구나. 뭐, 안 마서도 되긴 해.")
            "{cps=[text_speed]}[character_3_name][iga(character_3_name)] 쌍화차를 잠시 바라보며 고개를 끄덕였다.{/cps}"
            jump talk_4