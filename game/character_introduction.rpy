label character_introduction:
    scene bg black
    with fade

    python:
        for cid, c in all_characters.items():

            # 캐릭터 이미지 표시 (축소)
            renpy.show(
                cid,
                what=DynamicImage("character/%s/normal.png" % cid),
                at_list=[ intro_char ]
            )
            renpy.with_statement(dissolve)

            # 이름 출력
            renpy.say(None, "{size=40}{b}%s{/b}{/size}" % c["name"])

            # intro.txt 한 줄씩 출력
            for line in c["intro"].splitlines():
                if line.strip():
                    renpy.say(None, line)

            # 이미지 숨김
            renpy.hide(cid)
            renpy.with_statement(fade)

    jump select_main_character





label select_main_character:
    scene bg black
    with fade

    $ temp_main = None
    call screen select_main_character_screen
    jump select_side1_character

screen select_main_character_screen():

    text "메인 캐릭터를 선택하세요" xpos 0.5 ypos 0.1 xanchor 0.5

    hbox:
        spacing 40
        xpos 0.5
        ypos 0.2
        xanchor 0.5

        for cid, c in all_characters.items():
            vbox:
                spacing 10
                
                imagebutton:
                    idle Transform(
                        "character/%s/normal.png" % cid,
                        crop=(200, 0, 600, 1400)
                    )
                    hover Transform(
                        "character/%s/smile.png" % cid,
                        crop=(200, 0, 600, 1400)
                    )
                    at intro_char
                    action [ SetVariable("temp_main", cid), Return() ]

                text c["name"] xalign 0.5 yoffset -150


label select_side1_character:
    scene bg black
    with fade

    $ temp_side1 = None
    call screen select_side1_character_screen
    jump select_side2_character

screen select_side1_character_screen():

    text "서브 캐릭터 1을 선택하세요" xpos 0.5 ypos 0.1 xanchor 0.5

    hbox:
        spacing 40
        xpos 0.5
        ypos 0.2
        xanchor 0.5

        for cid, c in all_characters.items():
            if cid != temp_main:
                vbox:
                    spacing 10

                    imagebutton:
                        idle Transform(
                        "character/%s/normal.png" % cid,
                        crop=(200, 0, 600, 1400)
                        )
                        hover Transform(
                            "character/%s/smile.png" % cid,
                            crop=(200, 0, 600, 1400)
                        )
                        at intro_char
                        action [ SetVariable("temp_side1", cid), Return() ]

                    text c["name"] xalign 0.5 yoffset -150


label select_side2_character:
    scene bg black
    with fade

    $ temp_side2 = None
    call screen select_side2_character_screen
    jump apply_character_selection

screen select_side2_character_screen():

    text "서브 캐릭터 2를 선택하세요" xpos 0.5 ypos 0.1 xanchor 0.5

    hbox:
        spacing 40
        xpos 0.5
        ypos 0.2
        xanchor 0.5

        for cid, c in all_characters.items():
            if cid != temp_main and cid != temp_side1:
                vbox:
                    spacing 10
                    
                    imagebutton:
                        idle Transform(
                            "character/%s/normal.png" % cid,
                            crop=(200, 0, 600, 1400)
                        )
                        hover Transform(
                            "character/%s/smile.png" % cid,
                            crop=(200, 0, 600, 1400)
                        )
                        at intro_char
                        action [ SetVariable("temp_side2", cid), Return() ]

                    text c["name"] xalign 0.5 yoffset -150

label apply_character_selection:
    python:
        role_main = temp_main
        role_side1 = temp_side1
        role_side2 = temp_side2

        main_char_name  = all_characters[role_main]["name"]
        side1_char_name = all_characters[role_side1]["name"]
        side2_char_name = all_characters[role_side2]["name"]

        system_prompt_dawon = all_characters[role_main]["prompt"]
        system_prompt_jiwoo = all_characters[role_side1]["prompt"]
        system_prompt_suah  = all_characters[role_side2]["prompt"]

    jump talk_1
