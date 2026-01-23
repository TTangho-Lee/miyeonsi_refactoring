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

    jump select_character_1

# ---------------------------------------------------------
# 캐릭터 선택 화면 및 로직
# ---------------------------------------------------------

label select_character_1:
    $ temp_character_1 = None
    call screen select_character_1_screen
    jump select_character_2

label select_character_2:
    $ temp_character_2 = None
    call screen select_character_2_screen
    jump select_character_3

label select_character_3:
    $ temp_character_3 = None
    call screen select_character_3_screen
    jump apply_character_selection

# ---------------------------------------------------------
# 실제 데이터 매핑 (가장 중요한 부분)
# ---------------------------------------------------------

label apply_character_selection:
    python:
        # [1] 역할 ID 할당 (이미지 경로 결정)
        character_1_id = temp_main
        character_2_id = temp_side1
        character_3_id = temp_side2

        # [2] 실제 이름 할당 (대사창 이름 표시)
        character_1_name  = all_characters[character_1_id]["name"]
        character_2_name = all_characters[character_2_id]["name"]
        character_3_name = all_characters[character_3_id]["name"]

        # [3] AI 시스템 프롬프트 로드 (말투 및 성격 결정)
        system_prompt_character_1 = all_characters[character_1_id]["prompt"]
        system_prompt_character_2 = all_characters[character_2_id]["prompt"]
        system_prompt_character_3  = all_characters[character_3_id]["prompt"]

        # [4] 휴대폰 UI 이름 변수 동기화
        character_1_name_ui = "???"
        character_2_name_ui = "???"
        character_3_name_ui  = "???"

    "캐릭터 설정이 완료되었습니다. 게임을 시작합니다."
    
    jump talk_1

# ---------------------------------------------------------
# 선택용 스크린 정의
# ---------------------------------------------------------

screen select_character_1_screen():
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

screen select_character_2_screen():
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

screen select_character_3_screen():
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