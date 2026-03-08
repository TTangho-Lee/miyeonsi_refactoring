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

    # --- 4. 메인 캐릭터 등장 (슬롯: character_1) ---
    show character_1 normal at left with moveinright
    
    # [분기 1] 깨우는 대사
    if character_1_id == "dawon":
        $ typing(character_1_blind, f"어이, {player_name}. 언제까지 잘 거야?")
        $ typing(user, "어.. 누구였지?")
    elif character_1_id == "jiwoo":
        $ typing(character_1_blind, f"{player_name}{a(player_name)}, 언제까지 잘 거야? 얼른 일어나~")
        $ typing(user, "헉 누구세요..?")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1_blind, "선배님! 언제까지 주무실 거예요?")
        $ typing(user, "미안 사실은 내가 사람을 잘 기억못해..")
    else:
        $ typing(character_1_blind, f"어이, {player_name}. 언제까지 잘 거야?")
        $ typing(user, "미안 사실은 내가 사람을 잘 기억못해..")


    # [분기 2] 회식 자리 언급 대사
    if character_1_id == "dawon":
        $ typing(character_1_blind, "우리 어제 연구실 회식 때 옆자리였잖아, 내 이름도 물어보고선.")
    elif character_1_id == "jiwoo":
        $ typing(character_1_blind, "우리 어제 연구실 회식 때 옆자리였잖아~ 내 이름도 물어봤으면서.")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1_blind, "저희 어제 연구실 회식 때 옆자리였잖아요! 제 이름도 물어보셨으면서.")
    else:
        $ typing(character_1_blind, "우리 어제 연구실 회식 때 옆자리였잖아, 내 이름도 물어보고선.")
    
    if character_1_id == "jiwoo":
        $ typing(user, "아 맞다. 이름이?")
    else:
        $ typing(user, "내가 좀 취했었나봐, 이름 좀 ...")

    # 선택된 메인 캐릭터의 실제 이름을 출력
    $ character_1_name_ui = character_1_name  # 휴대폰 UI 이름 동기화

    # [분기 3] 자기소개 대사 (조사 함수 완벽 적용)
    if character_1_id == "dawon":
        $ typing(character_1, f"{character_1_name}이다.")
    elif character_1_id == "jiwoo":
        $ typing(character_1, f"난 {character_1_name}{iya(character_1_name)}.")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, f"제 이름은 {character_1_name}{ieyo(character_1_name)}!")
    else:
        $ typing(character_1, f"내 이름은 {character_1_name}{iya(character_1_name)}.")

    $ apply_affinity_change("character_1", 30)

    # --- 5. KNUAI 알림 & 호감도 UI 연동 ---
    "'띠링'"
    play sound "audio/notification.ogg"
    "휴대폰의 알람이 다시 울렸다. 아까 들어온 알림을 클릭하자 새로운 창이 떴다."
    
    # 선택된 캐릭터의 이름이 알림창에 동적으로 표시됨 
    $ send_notification(f"**'{character_1_name}'**의 호감도를 확인하시겠습니까?")
    
    $ typing(user, "tlqkf 이게 뭐야")

    # [분기 4] 욕설에 대한 반응
    if character_1_id == "dawon":
        $ typing(character_1, "갑자기 왜 욕해?")
    elif character_1_id == "jiwoo":
        $ typing(character_1, "깜짝이야, 왜 그래?")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, "헉, 저 뭐 잘못했나요?")
    else:
        $ typing(character_1, "갑자기 왜 욕해?")

    $ typing(user, "아 미안, 약간 감탄사야.")
    
    "일단 누르고 보는 [user], 버튼을 클릭하자 핸드폰 화면이 나타났다."
    show screen phone_overlay
    pause long_pause
    hide screen phone_overlay
    
    # --- 6. 시나리오 대사 계속 ---
    # [분기 5] 논문 진척도 묻기
    if character_1_id == "dawon":
        $ typing(character_1, "너 교수님이 써오라 하신 논문, 어떻게 돼 가는데? 저번 주부터 막막해하더니.")
    elif character_1_id == "jiwoo":
        $ typing(character_1, "그나저나 교수님이 써오라 하신 논문은 어떻게 돼 가? 저번 주부터 막막해하더니.")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, "아, 선배님. 교수님이 써오라 하신 논문은 어떻게 돼 가세요? 저번 주부터 막막해하시더니.")
    else:
        $ typing(character_1, "너 교수님이 써오라 하신 논문, 어떻게 돼 가는데? 저번 주부터 막막해하더니.")

    $ typing(user, "나 논문 써야 해?")

    # [분기 6] 논문 안 쓰냐고 되묻기
    if character_1_id == "dawon":
        $ typing(character_1, "그럼 안 써?")
    elif character_1_id == "jiwoo":
        $ typing(character_1, "엥? 그럼 안 쓰게?")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, "네?! 그럼 안 쓰시게요?!")
    else:
        $ typing(character_1, "그럼 안 써?")

    $ typing(user, "어.. (아니 애초에 지금 이 상황이 이해도 안 되는데)")
    
    jump event_1