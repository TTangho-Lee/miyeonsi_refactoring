label talk_2: 
    # --- 1. 논문 확인 및 호감도 변화 ---
    "[user_iga] 컴퓨터를 켜서 USB 안의 '논문.docx' 이라고 적힌 파일을 열어본다."
    $ show_center_notice(
        "모바일 디바이스에서 근거리 객체 탐지를 위한",
        "YOLOv8 모델 경량화 연구"
        )
        
    # [분기 1] 논문을 확인한 유저의 반응 (연상인 지우에게는 존댓말)
    if character_1_id == "jiwoo":
        $ typing(user, "고마워요. 하마터면 헛고생할 뻔했네요.")
    else:
        $ typing(user, "고맙다. 하마터면 헛고생할 뻔했네.")

    $ apply_affinity_change("character_1", 1)

    # [분기 2] 유저의 감사에 대한 character_1의 반응
    if character_1_id == "dawon":
        $ typing(character_1, "도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었어 ✨")
    elif character_1_id == "jiwoo":
        $ typing(character_1, "도움이 됐다니 다행이네~ 난 진짜 옆에서 조금 거들기만 한걸 뭐.")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, "앗, 다행이에요! 전 진짜 옆에서 조금만 거들었는걸요 ✨")
    else:
        $ typing(character_1, "도움 됐다면 다행이지 뭐~ 난 진짜 조금만 거들었어 ✨")

    # UI에 표시되는 이름도 동기화
    $ send_notification(f"{character_1_name} 호감도 +1 (현재: {character_1_affinity})")
    
    # --- 2. 유튜브 대화 ---
    # [분기 3] 유튜브 알림을 보고 묻는 대화
    if character_1_id == "dawon":
        $ typing(character_1, "뭔데? 뭐 보는데.")
        $ typing(user, "아, 별건 아니고. 유튜브 알림.")
        $ typing(character_1, "뭐? 그게 뭔...")
    elif character_1_id == "jiwoo":
        $ typing(character_1, "응? 뭐 재밌는 거 봐?")
        $ typing(user, "아, 별건 아니고요. 유튜브 알림 뜬 거요.")
        $ typing(character_1, "유튜브? 그게 뭐야...?")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, "어? 선배님 뭐 보세요?")
        $ typing(user, "아, 별건 아니고. 유튜브 알림.")
        $ typing(character_1, "네? 유튜브요? 그게 뭐예요...?")
    else:
        $ typing(character_1, "뭔데? 뭐 보는데.")
        $ typing(user, "아, 별건 아니고. 유튜브 알림.")
        $ typing(character_1, "뭐? 그게 뭔...")
    
    # --- 3. 서브 캐릭터 2 등장 (슬롯: character_2) ---
    "연구실의 문이 열리고 누군가 들어온다."
    show character_1 normal at left with move
    show character_2 normal at right with moveinright
    
    # [분기 4] character_2의 등장 및 인사
    if character_2_id == "dawon":
        $ typing(character_2_blind, "오, 둘이 같이 있었어?")
        $ typing(user, "아, 안녕?")
        
        $ character_2_name_ui = character_2_name  # 휴대폰 UI 이름 동기화
        $ typing(character_2_blind, f"에이, 나 {character_2_name}{iya(character_2_name)}! 벌써 내 얼굴 까먹은 건 아니지?")
        $ apply_affinity_change("character_2", 30)
        $ typing(character_2, "저녁 먹으러 갈 거지? 내가 진짜 맛있는 데 알아놨거든!")
        
    elif character_2_id == "jiwoo":
        $ typing(character_2_blind, "어머, 둘이 같이 있었네?")
        $ typing(user, "아, 안녕하세요?")
        
        $ character_2_name_ui = character_2_name  # 휴대폰 UI 이름 동기화
        $ typing(character_2_blind, f"에이, 나 {character_2_name}{iya(character_2_name)}! 서운하게 왜 그래~")
        $ apply_affinity_change("character_2", 30)
        $ typing(character_2, "저녁 먹으러 갈 거지? 내가 엄청 맛있는 데 알아놨어!")
        
    elif character_2_id in ["suah", "yeji", "huieun"]:
        $ typing(character_2_blind, "선배님들 같이 계셨네요?")
        $ typing(user, "아, 안녕?")
        
        $ character_2_name_ui = character_2_name  # 휴대폰 UI 이름 동기화
        $ typing(character_2_blind, f"에이 선배님, 저 {character_2_name}{ieyo(character_2_name)}! 서운하게 왜 그러세요~")
        $ apply_affinity_change("character_2", 30)
        $ typing(character_2, "저녁 드시러 가실 거죠? 제가 맛있는 데 알아놨는데!")
        
    else:
        $ typing(character_2_blind, "선배님들 같이 계셨네요?")
        $ typing(user, "아, 안녕?")
        
        $ character_2_name_ui = character_2_name
        $ typing(character_2_blind, f"에이 선배님, {character_2_name}{ieyo(character_2_name)}! 서운하게 왜 그러세요~")
        $ apply_affinity_change("character_2", 30)
        $ typing(character_2, "저녁 드시러 가실 거죠? 제가 맛있는 데 알아놨는데!")

    jump event_2