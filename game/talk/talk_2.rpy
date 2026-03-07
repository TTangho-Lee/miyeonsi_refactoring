label talk_2: 
    # --- 1. 논문 확인 및 호감도 변화 ---
    "[user_iga] 컴퓨터를 켜서 USB 안의 '논문.docx' 이라고 적힌 파일을 열어본다."
    $ show_center_notice(
        "모바일 디바이스에서 근거리 객체 탐지를 위한",
        "YOLOv8 모델 경량화 연구"
        )
    $ typing(user, "고맙다. 헛고생할 뻔 했네.")
    $ apply_affinity_change("character_1", 1)
    $ typing(character_1, "도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었어 ✨")
    # UI에 표시되는 이름도 동기화 [cite: 24]
    $ send_notification(f"{character_1_name} 호감도 +1 (현재: {character_1_affinity})")
    
    # --- 2. 유튜브 대화 ---
    $ typing(character_1, "뭔데? 뭐 보는데.")
    $ typing(user, "아, 별건 아니고. 유튜브 알림.")
    $ typing(character_1, "뭐? 그게 뭔...")
    
    # --- 3. 서브 캐릭터 2 등장 (슬롯: suah) ---
    "연구실의 문이 열리고 누군가 들어온다."
    show character_1 normal at left with move
    show character_2 normal at right with moveinright
    
    $ typing(character_2_blind, "선배님들 같이 계셨네요?")
    $ typing(user, "아, 안녕?")
    # 서브 캐릭터 2의 실제 이름을 사용하여 정체를 밝힘 [cite: 24]
    $ character_2_name_ui = character_2_name  # 휴대폰 UI 이름 동기화
    $ typing(character_2_blind, f"에이 선배님, {character_2_name}{ieyo(character_2_name)}! 서운하게 왜 그러세요~")
    $ apply_affinity_change("character_2", 30)
    $ typing(character_2, "저녁 드시러 가실 거죠? 제가 맛있는 데 알아놨는데!")

    jump event_2