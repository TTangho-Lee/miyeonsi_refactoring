label happy_ending:
    scene bg lab
    
    if max_slot_id == "character_1":
        show character_1 shy
        $ typing(character_1, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show character_1 smile
        $ typing(character_1, "...좋아")
        scene bg sunset_dawon with dissolve # 메인 캐릭터 전용 배경 (또는 슬롯 배경)
        $ typing(character_1, "너랑 이런 사이가 되어서.. 정말 좋아해")
        $ persistent.ending_image = dawon_happy_ending_image

    elif max_slot_id == "character_2":
        show character_2 shy
        $ typing(character_2, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show character_2 smile
        $ typing(character_2, "...좋아")
        scene bg sunset_jiwoo with dissolve
        $ typing(character_2, "너랑 이런 사이가 되어서.. 정말 좋아해")
        $ persistent.ending_image = jiwoo_happy_ending_image

    elif max_slot_id == "character_3":
        show character_3 shy
        $ typing(character_3, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show character_3 smile
        $ typing(character_3, "...좋아")
        scene bg sunset_suah with dissolve
        $ typing(character_3, "너랑 이런 사이가 되어서.. 정말 좋아해")
        $ persistent.ending_image = suah_happy_ending_image

    $ renpy.save_persistent()
    return