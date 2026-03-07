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
    # 서브 캐릭터 1이 메인 캐릭터의 이름을 부름 [cite: 24]
    $ typing(character_3_blind, character_1_name + "! 언니가 마실 것 좀 사왔어.")
    $ typing(character_1, "언니!")

    $ typing(character_3_blind, "근데 이 친구는 누구? 처음 보는데? 연구실 이번에 들어온 거야?")
    $ typing(character_1, "응 [user]라고, 들어온 지 얼마 안 됐어. 나랑 동갑.")
    
    $ typing(character_3_blind, "[user] 안녕?")
    $ typing(user, "안녕하세요.")
    # 서브 캐릭터 1의 실제 이름으로 정체 고정 [cite: 24]
    $ character_3_name_ui = character_3_name  # 휴대폰 UI 이름 동기화
    $ typing(character_3, f"나는 {character_3_name}{irago(character_3_name)} 해.")
    $ apply_affinity_change("character_3", 30)

    $ typing(character_3, "[user] 있는지 모르고 내 것랑 얘 것만 사 왔네. 다음에 사줄게!")
    $ typing(user, "아니에요, 괜찮습니다.")

    jump event_3