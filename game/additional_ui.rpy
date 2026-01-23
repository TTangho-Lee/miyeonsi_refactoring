# additional_ui.rpy

# --- 변수 선언 ---
default phone_visible = False

# [추가됨] 캐릭터 이름 변수 (초기값은 ???)
default dawon_name_ui = "???"
default jiwoo_name_ui = "???"
default suah_name_ui = "???"

# --- 키 설정 (0번 누르면 폰 토글) ---
init python:
    config.keymap['toggle_phone'] = ['K_0']

# --- 키 입력 리스너 ---
screen input_listener():
    key "toggle_phone" action ToggleScreen("phone_overlay")

# --- 핸드폰 UI (KNUAI 앱) ---
screen phone_overlay():
    zorder 100
    
    # 핸드폰 프레임
    frame:
        xalign 0.95
        yalign 0.95
        xsize 450
        ysize 800
        background "#1a1a1a" # 어두운 핸드폰 본체

        # 내부 화면 (스크린)
        frame:
            background "#000000" # 완전 검정 배경
            xfill True
            yfill True
            padding (20, 20)

            vbox:
                spacing 15
                xalign 0.5
                
                # 앱 헤더
                text "KNUAI" size 40 bold True color "#ffffff" xalign 0.5
                null height 10
                
                # 호감도 섹션
                frame:
                    background "#110000"
                    xfill True
                    padding (10, 10)
                    vbox:
                        text "♥ 호감도 표시" size 22 color "#ff0000" bold True xalign 0.0
                        null height 5

                        # 임다원
                        hbox:
                            spacing 10
                            # [수정됨] 변수([character_1_name_ui])를 사용하여 이름 표시
                            text "[character_1_name_ui]" color "#ffffff" size 18 yalign 0.5
                            bar value character_1_affinity range 100 xysize (230, 20) style "blood_bar"

                        # 홍지우
                        hbox:
                            spacing 10
                            # [수정됨] 변수 사용
                            text "[character_2_name_ui]" color "#ffffff" size 18 yalign 0.5
                            bar value character_2_affinity range 100 xysize (230, 20) style "blood_bar"

                        # 윤수아
                        hbox:
                            spacing 10
                            # [수정됨] 변수 사용
                            text "[character_3_name_ui]" color "#ffffff" size 18 yalign 0.5
                            bar value character_3_affinity range 100 xysize (230, 20) style "blood_bar"

                null height 20
                
                # 기능 버튼 섹션
                textbutton "🤖 호반우 챗봇 대화":
                    #action Call("hobanwoo_chat_start") 
                    xalign 0.5
                    text_size 22
                    text_color "#aaaaaa"
                    text_hover_color "#ffffff"
                    
                # 공지사항 (나폴리탄 괴담)
                frame:
                    background "#220000"
                    xfill True
                    padding (10, 10)
                    vbox:
                        text "※ [[필독] 사용 유의사항" size 18 color "#ffaaaa" bold True
                        null height 5
                        text "1. 호감도가 급격히 떨어지지 않게 주의하십시오." size 14 color "#cccccc"
                        text "2. 과제 및 평가의 제출 기한을 엄수하십시오." size 14 color "#cccccc"
                        text "3. 시스템의 정체에 대해 묻지 마십시오." size 14 color "#cccccc"

                null height 40

                # 탈퇴 버튼 (붉게 강조)
                textbutton "탈퇴하기":
                    action Call("event_4")
                    xalign 0.5 
                    text_color "#ff0000" 
                    text_size 28
                    text_bold True

# --- 스타일 정의 (피 묻은 듯한 붉은 바) ---
style blood_bar:
    left_bar Frame(Solid("#ff0000"), 0, 0) # 꽉 찬 부분 (선명한 붉은색)
    right_bar Frame(Solid("#330000"), 0, 0) # 빈 부분 (검붉은색)
    thumb None

# --- 알림 토스트 메시지 (띠링 효과) ---
screen message_toast(msg):
    zorder 200
    frame:
        xalign 0.5
        yalign 0.1
        background "#000000cc"
        padding (30, 20)
        
        hbox:
            spacing 15
            text "🔔" size 30 yalign 0.5
            vbox:
                text "KNUAI 알림" size 16 color "#aaaaaa"
                text "[msg]" size 24 color "#ffffff" bold True

    timer 3.5 action Hide("message_toast")

screen red_notice_popup(messages):

    frame:
        xalign 0.5
        yalign 0.5
        padding (30,30,30,30)
        background "#000c"

        vbox:
            spacing 10

            # ★ 첫 문장(제목) : 빨간색 + 가운데 정렬
            text messages[0] color "#FF0000" xalign 0.5 size 32

            # ★ 나머지 문장들 출력
            for msg in messages[1:]:
                text msg

    timer 5 action Hide("red_notice_popup")

screen normal_notice_popup(messages):

    frame:
        xalign 0.5
        yalign 0.5
        padding (30,30,30,30)
        background "#000c"

        vbox:
            spacing 10

            for msg in messages:
                text msg

    timer 5 action Hide("normal_notice_popup")

screen center_notice_popup(messages):

    frame:
        xalign 0.5
        yalign 0.5
        padding (30,30,30,30)
        background "#000c"

        vbox:
            spacing 10

            for msg in messages:
                text msg xalign 0.5 size 32

    timer 5 action Hide("center_notice_popup")

# 알림 호출 함수
init python:
    def send_notification(msg):
        renpy.play("audio/notification.ogg")
        renpy.show_screen("message_toast", msg=msg)

    def show_red_notice(*msgs):
        renpy.play("audio/notification.ogg")
        renpy.show_screen("red_notice_popup", messages=list(msgs))

    def show_normal_notice(*msgs):
        renpy.show_screen("normal_notice_popup", messages=list(msgs))

    def show_center_notice(*msgs):
        renpy.show_screen("center_notice_popup", messages=list(msgs))