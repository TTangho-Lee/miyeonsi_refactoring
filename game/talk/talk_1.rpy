label talk_1:
    # --- 1. 트럭 사고 씬 ---
    scene bg black with fade
    "[user_eunneun] 경북대학교 전자과에 재학 중인 3학년."
    "저녁 수업을 마치고 환승연애를 보며 횡단보도를 건너게 된다."
    play sound "audio/truck_horn.ogg"
    with vpunch
    scene bg truck with Dissolve(0.1) 
    
    "하지만 빠르게 달려오는 대형트럭을 보지 못한 채 그대로 치인다."
    scene bg black with fade 

    # --- 2. 깨어남 씬 ---
    scene bg my_computer with dissolve
    "눈을 뜬 [user], 책상에서 엎드린 상태였다."
    $ typing(user, "뭐야, 나 방금 트럭에 치인 거 아니였나?")
    $ typing(user, "꿈이라기엔 너무 생생했는데, 여긴 어디.. 연구실?")

    # --- 3. KNUAI 앱 알림 ---
    "‘띠링’"
    play sound "audio/notification.ogg"
    $ send_notification("[메시지] 새로운 메시지가 도착하였습니다.")
    "휴대폰의 알람이 울렸다. [user_iga] 이 낯선 장소로 오기 전의 본인 것이 아닌, 처음 보는 휴대폰이었다."

    # --- 4. 메인 캐릭터 등장 (슬롯: dawon) ---
    show dawon normal at center with moveinright
    $ typing(dawon_blind, "어이, [user]. 언제까지 잘 거야?") # dawon_blind는 ???로 표시됨
    $ typing(user, "미안 사실은 내가 사람을 잘 기억못해..")
    $ typing(dawon_blind, "우리 어제 연구실 회식 때 옆자리였잖아, 내 이름도 물어보고선.")
    $ typing(user, "내가 좀 취했었나봐, 이름 좀 ...")
    
    # 선택된 메인 캐릭터의 실제 이름을 출력 [cite: 23]
    $ dawon_name_ui = main_char_name  # 휴대폰 UI 이름 동기화
    $ typing(dawon, "내 이름은 " + main_char_name + "이야.") 
    $ apply_affinity_change("dawon", 30)

    # --- 5. KNUAI 알림 & 호감도 UI 연동 ---
    "'띠링'"
    play sound "audio/notification.ogg"
    "휴대폰의 알람이 다시 울렸다. 아까 들어온 알림을 클릭하자 새로운 창이 떴다."
    # 선택된 캐릭터의 이름이 알림창에 동적으로 표시됨 
    $ send_notification(f"**'{main_char_name}'**의 호감도를 확인하시겠습니까?")
    
    $ typing(user, "tlqkf 이게 뭐야")
    $ typing(dawon, "갑자기 왜 욕해?")
    $ typing(user, "아 미안, 약간 감탄사야.")
    
    "일단 누르고 보는 [user], 버튼을 클릭하자 핸드폰 화면이 나타났다."
    show screen phone_overlay
    pause long_pause
    hide screen phone_overlay
    
    # --- 6. 시나리오 대사 계속 ---
    $ typing(dawon, "너 교수님이 써오라 하신 논문, 어떻게 돼 가는데? 저번 주부터 막막해하더니.")
    $ typing(user, "나 논문 써야 해?")
    $ typing(dawon, "그럼 안 써?")
    $ typing(user, "어.. (아니 애초에 지금 이 상황이 이해도 안 되는데)")
    
    jump event_1