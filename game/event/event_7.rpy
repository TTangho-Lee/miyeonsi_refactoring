label event_7:
    menu:
        "[side2_char_name]의 손을 잡는다":
            $ apply_affinity_change("sub_role2", 5)
            scene bg hand with dissolve
            $ typing(sub_role2, "......")
            jump talk_8

        "[side1_char_name]의 손을 잡는다":
            $ apply_affinity_change("sub_role1", 5)
            scene bg hand with dissolve
            $ typing(sub_role1, ".......")
            jump talk_8

        "[main_char_name]의 손을 잡는다":
            $ apply_affinity_change("main_role", 5)
            scene bg hand with dissolve
            $ typing(main_role, "......")
            jump talk_8

        "아무것도 잡지 않는다":
            $ apply_affinity_change("hobanwoo", -10)
            jump talk_8