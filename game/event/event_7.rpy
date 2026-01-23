label event_7:
    menu:
        "[character_1_name]의 손을 잡는다":
            $ apply_affinity_change("character_1", 5)
            scene bg hand with dissolve
            $ typing(character_1, "......")
            jump talk_8

        "[character_2_name]의 손을 잡는다":
            $ apply_affinity_change("character_2", 5)
            scene bg hand with dissolve
            $ typing(character_2, ".......")
            jump talk_8

        "[character_3_name]의 손을 잡는다":
            $ apply_affinity_change("character_3", 5)
            scene bg hand with dissolve
            $ typing(character_3, "......")
            jump talk_8

        "아무것도 잡지 않는다":
            $ apply_affinity_change("hobanwoo", -10)
            jump talk_8