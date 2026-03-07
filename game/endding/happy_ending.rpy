label happy_ending:
    scene bg lab
    
    # 1. 1등한 슬롯과 실제 캐릭터 ID 매핑
    python:
        if max_slot_id == "character_1":
            winning_id = character_1_id
            winning_char = character_1
        elif max_slot_id == "character_2":
            winning_id = character_2_id
            winning_char = character_2
        else:
            winning_id = character_3_id
            winning_char = character_3

    # 2. 부끄러워하는 표정 출력 (슬롯 기반 동적 호출)
    $ renpy.show(f"{max_slot_id} shy")

    # 3. 캐릭터 성격별 고백 수락 대사 및 엔딩 배경 분기
    if winning_id == "dawon":
        $ typing(winning_char, "정말? 그럼... 우리")
        $ typing(user, "사귀자.")
        $ renpy.show(f"{max_slot_id} smile")
        $ typing(winning_char, "...좋아.")
        
        scene bg sunset_dawon with dissolve
        $ typing(winning_char, "너랑 이런 사이가 되어서.. 정말 좋아해.")
        $ persistent.ending_image = dawon_happy_ending_image

    elif winning_id == "jiwoo":
        $ typing(winning_char, "정말? 그럼... 우리 이제")
        $ typing(user, "저랑 사귀어요.")
        $ renpy.show(f"{max_slot_id} smile")
        $ typing(winning_char, "...응, 좋아.")
        
        scene bg sunset_jiwoo with dissolve
        $ typing(winning_char, "너랑 이런 사이가 되어서.. 정말 기뻐.")
        $ persistent.ending_image = jiwoo_happy_ending_image

    elif winning_id in ["suah", "yeji", "huieun"]:
        $ typing(winning_char, "정말요? 그럼... 저희")
        $ typing(user, "사귀자.")
        $ renpy.show(f"{max_slot_id} smile")
        $ typing(winning_char, "...네, 좋아요!")
        
        # 연하조(수아, 예지, 희은)는 전용 배경을 공유합니다.
        # (만약 나중에 예지, 희은 전용 배경을 추가하신다면 이 부분을 분리하시면 됩니다.)
        scene bg sunset_suah with dissolve
        $ typing(winning_char, "선배님이랑 이런 사이가 되어서.. 정말 행복해요!")
        $ persistent.ending_image = suah_happy_ending_image

    else:
        # 혹시 모를 예외 처리 (기본값)
        $ typing(winning_char, "정말? 그럼... 우리")
        $ typing(user, "사귀자.")
        $ renpy.show(f"{max_slot_id} smile")
        $ typing(winning_char, "...좋아.")
        
        scene bg sunset_dawon with dissolve
        $ typing(winning_char, "너랑 이런 사이가 되어서.. 정말 좋아해.")
        $ persistent.ending_image = dawon_happy_ending_image

    $ renpy.save_persistent()
    return