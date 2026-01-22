# =========================================================
# character_introduction.rpy
# 캐릭터 선택 및 역할 슬롯 매칭 시스템
# =========================================================

label character_introduction:
    scene bg black
    with fade

    # 1. 로드된 모든 캐릭터 소개 (캐릭터 폴더 내 intro.txt 기반)
    python:
        for cid, c in all_characters.items():
            # 캐릭터 이미지 표시 (역할 슬롯 변수와 무관하게 직접 ID로 로드)
            renpy.show(
                cid,
                what=DynamicImage("character/%s/normal.png" % cid),
                at_list=[ intro_char ]
            )
            renpy.with_statement(dissolve)

            # 이름 및 소개 문구 출력
            renpy.say(None, "{size=40}{b}%s{/b}{/size}" % c["name"])
            for line in c["intro"].splitlines():
                if line.strip():
                    renpy.say(None, line)

            # 이미지 숨김
            renpy.hide(cid)
            renpy.with_statement(fade)

    jump select_main_character

# ---------------------------------------------------------
# 캐릭터 선택 화면 및 로직
# ---------------------------------------------------------

label select_main_character:
    $ temp_main = None
    call screen select_main_character_screen
    jump select_side1_character

label select_side1_character:
    $ temp_side1 = None
    call screen select_side1_character_screen
    jump select_side2_character

label select_side2_character:
    $ temp_side2 = None
    call screen select_side2_character_screen
    jump apply_character_selection

# ---------------------------------------------------------
# 실제 데이터 매핑 (가장 중요한 부분)
# ---------------------------------------------------------

label apply_character_selection:
    python:
        # [1] 역할 ID 할당 (이미지 경로 결정)
        role_main  = temp_main
        role_side1 = temp_side1
        role_side2 = temp_side2

        # [2] 실제 이름 할당 (대사창 이름 표시)
        main_char_name  = all_characters[role_main]["name"]
        side1_char_name = all_characters[role_side1]["name"]
        side2_char_name = all_characters[role_side2]["name"]

        # [3] AI 시스템 프롬프트 로드 (말투 및 성격 결정)
        system_prompt_dawon = all_characters[role_main]["prompt"]
        system_prompt_jiwoo = all_characters[role_side1]["prompt"]
        system_prompt_suah  = all_characters[role_side2]["prompt"]

        # [4] 휴대폰 UI 이름 변수 동기화
        dawon_name_ui = main_char_name
        jiwoo_name_ui = side1_char_name
        suah_name_ui  = side2_char_name

    "캐릭터 설정이 완료되었습니다. 게임을 시작합니다."
    jump talk_1

# ---------------------------------------------------------
# 선택용 스크린 정의
# ---------------------------------------------------------

screen select_main_character_screen():
    style_prefix "select_char"
    text "메인 캐릭터를 선택하세요" xalign 0.5 ypos 100 size 50

    hbox:
        spacing 50
        xalign 0.5
        yalign 0.5
        for cid, c in all_characters.items():
            vbox:
                imagebutton:
                    idle Transform("character/%s/normal.png" % cid, zoom=0.4)
                    hover Transform("character/%s/smile.png" % cid, zoom=0.4)
                    action [ SetVariable("temp_main", cid), Return() ]
                text c["name"] xalign 0.5 size 30

screen select_side1_character_screen():
    style_prefix "select_char"
    text "서브 캐릭터 1을 선택하세요" xalign 0.5 ypos 100 size 50

    hbox:
        spacing 50
        xalign 0.5
        yalign 0.5
        for cid, c in all_characters.items():
            if cid != temp_main: # 이미 선택된 캐릭터는 제외
                vbox:
                    imagebutton:
                        idle Transform("character/%s/normal.png" % cid, zoom=0.4)
                        hover Transform("character/%s/smile.png" % cid, zoom=0.4)
                        action [ SetVariable("temp_side1", cid), Return() ]
                    text c["name"] xalign 0.5 size 30

screen select_side2_character_screen():
    style_prefix "select_char"
    text "서브 캐릭터 2를 선택하세요" xalign 0.5 ypos 100 size 50

    hbox:
        spacing 50
        xalign 0.5
        yalign 0.5
        for cid, c in all_characters.items():
            if cid != temp_main and cid != temp_side1:
                vbox:
                    imagebutton:
                        idle Transform("character/%s/normal.png" % cid, zoom=0.4)
                        hover Transform("character/%s/smile.png" % cid, zoom=0.4)
                        action [ SetVariable("temp_side2", cid), Return() ]
                    text c["name"] xalign 0.5 size 30