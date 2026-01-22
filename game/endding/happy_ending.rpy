label happy_ending:
    scene bg lab
    
    if max_slot_id == "main_role":
        show main_role shy
        $ typing(main_role, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show main_role smile
        $ typing(main_role, "...좋아")
        scene bg sunset_dawon with dissolve # 메인 캐릭터 전용 배경 (또는 슬롯 배경)
        $ typing(main_role, "너랑 이런 사이가 되어서.. 정말 좋아해")
        $ persistent.ending_image = dawon_happy_ending_image

    elif max_slot_id == "sub_role1":
        show sub_role1 shy
        $ typing(sub_role1, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show sub_role1 smile
        $ typing(sub_role1, "...좋아")
        scene bg sunset_jiwoo with dissolve
        $ typing(sub_role1, "너랑 이런 사이가 되어서.. 정말 좋아해")
        $ persistent.ending_image = jiwoo_happy_ending_image

    elif max_slot_id == "sub_role2":
        show sub_role2 shy
        $ typing(sub_role2, "정말? 그럼...우리")
        $ typing(user, "사귀자")
        show sub_role2 smile
        $ typing(sub_role2, "...좋아")
        scene bg sunset_suah with dissolve
        $ typing(sub_role2, "너랑 이런 사이가 되어서.. 정말 좋아해")
        $ persistent.ending_image = suah_happy_ending_image

    $ renpy.save_persistent()
    return