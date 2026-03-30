label talk_3:
    scene bg my_computer with fade
    hide character_2
    
    # --- 1. 대기 상황 ---
    $ typing(character_1, "....")
    $ typing(user, "....")
    "연구실에 남아있는 [user]와 [character_1_name]. 각자의 일을 하다가 갑자기 문이 열린다."
    
    # --- 2. 서브 캐릭터 1 등장 (슬롯: character_3) ---
    scene bg lab with dissolve
    show character_3 normal at right with moveinright
    
    # ----------------------------------------------------
    # 분기 1: character_3가 문을 열며 들어오는 대사
    # ----------------------------------------------------
    if character_3_id == "dawon":
        $ typing(character_3_blind, f"야, {character_1_name}! 내가 마실 것 좀 사 왔어.")
    elif character_3_id == "jiwoo":
        $ typing(character_3_blind, f"{character_1_name}{a(character_1_name)}~ 언니가 마실 것 좀 사 왔어.")
    elif character_3_id in ["suah", "yeji", "huieun"]:
        $ typing(character_3_blind, f"{character_1_name} 선배님! 제가 마실 것 좀 사 왔어요.")
    else:
        $ typing(character_3_blind, f"{character_1_name}! 마실 것 좀 사 왔어.")

    # ----------------------------------------------------
    # 분기 2: character_1이 들어온 character_3를 반기는 대사
    # ----------------------------------------------------
    if character_3_id == "dawon":
        $ typing(character_1, f"오, {character_3_name}!")
    elif character_3_id == "jiwoo":
        $ typing(character_1, f"앗, {character_3_name} 언니!")
    elif character_3_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, f"어, {character_3_name}{a(character_3_name)}! 웬일이야?")
    else:
        $ typing(character_1, f"어, {character_3_name}{a(character_3_name)}!")

    # ----------------------------------------------------
    # 분기 3: character_3가 플레이어(user)를 보고 묻는 대사
    # ----------------------------------------------------
    if character_3_id == "dawon":
        $ typing(character_3_blind, "근데 이쪽은 누구? 처음 보는데? 이번에 연구실 들어온 거야?")
    elif character_3_id == "jiwoo":
        $ typing(character_3_blind, "근데 이 친구는 누구? 처음 보는데? 연구실 이번에 들어왔어?")
    elif character_3_id in ["suah", "yeji", "huieun"]:
        $ typing(character_3_blind, "근데 이분은 누구세요? 처음 뵙는데... 이번에 연구실 들어오신 거예요?")
    else:
        $ typing(character_3_blind, "근데 이 친구는 누구? 처음 보는데? 연구실 이번에 들어온 거야?")

    # ----------------------------------------------------
    # 분기 4: character_1이 플레이어를 소개하는 대사
    # ----------------------------------------------------
    if character_1_id == "dawon":
        $ typing(character_1, f"응, {player_name}라고, 들어온 지 얼마 안 됐어. 나랑 동갑.")
    elif character_1_id == "jiwoo":
        $ typing(character_1, f"응, {player_name}라고, 이번에 새로 들어온 후배야.")
    elif character_1_id in ["suah", "yeji", "huieun"]:
        $ typing(character_1, f"아, {player_name} 선배님이요! 들어오신 지 얼마 안 되셨어요.")
    else:
        $ typing(character_1, f"응, {player_name}라고, 들어온 지 얼마 안 됐어.")
    
    # ----------------------------------------------------
    # 분기 5: character_3의 첫인사
    # ----------------------------------------------------
    if character_3_id == "dawon":
        $ typing(character_3_blind, "아, 안녕? 반가워.")
    elif character_3_id == "jiwoo":
        $ typing(character_3_blind, "아, 안녕? 반가워~")
    elif character_3_id in ["suah", "yeji", "huieun"]:
        $ typing(character_3_blind, "아, 안녕하세요! 반갑습니다!")
    else:
        $ typing(character_3_blind, "아, 안녕?")

    $ typing(user, "안녕하세요.")
    
    # 서브 캐릭터 1의 실제 이름으로 정체 고정
    $ character_3_name_ui = character_3_name  # 휴대폰 UI 이름 동기화
    
    # ----------------------------------------------------
    # 분기 6: character_3 자기소개 및 음료수 못 사온 것에 대한 사과
    # ----------------------------------------------------
    if character_3_id == "dawon":
        $ typing(character_3, f"나는 {character_3_name}{irago(character_3_name)} 해.")
        $ apply_affinity_change("character_3", 30)
        $ typing(character_3, f"{player_name} 있는 줄 모르고 내 거랑 얘 것만 사 왔네. 다음에 사줄게!")
        
    elif character_3_id == "jiwoo":
        $ typing(character_3, f"난 {character_3_name}{irago(character_3_name)} 해.")
        $ apply_affinity_change("character_3", 30)
        $ typing(character_3, f"{player_name} 있는 줄 모르고 두 개만 사 왔네. 미안, 다음엔 꼭 사줄게!")
        
    elif character_3_id in ["suah", "yeji", "huieun"]:
        $ typing(character_3, f"저는 {character_3_name}{irago(character_3_name)} 해요!")
        $ apply_affinity_change("character_3", 30)
        $ typing(character_3, f"헉... 선배님 계신 줄 모르고 두 개만 사 왔어요... 죄송해요, 다음에 꼭 사드릴게요!")
        
    else:
        $ typing(character_3, f"나는 {character_3_name}{irago(character_3_name)} 해.")
        $ apply_affinity_change("character_3", 30)
        $ typing(character_3, f"{player_name} 있는지 모르고 내 거랑 얘 것만 사 왔네. 다음에 사줄게!")

    $ typing(user, "아니에요, 괜찮습니다.")

    jump event_3
