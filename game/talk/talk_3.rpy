label talk_3:
    scene bg my_computer with fade
    hide suah
    
    # --- 1. 대기 상황 ---
    $ typing(dawon, "....")
    $ typing(user, "....")
    "연구실에 남아있는 [user]와 [main_char_name]. 각자의 일을 하다가 갑자기 문이 열린다."
    
    # --- 2. 서브 캐릭터 1 등장 (슬롯: jiwoo) ---
    scene bg lab with dissolve
    show jiwoo normal at center with moveinright
    # 서브 캐릭터 1이 메인 캐릭터의 이름을 부름 [cite: 24]
    $ typing(jiwoo_blind, main_char_name + "! 언니가 마실 것 좀 사왔어.")
    $ typing(dawon, "언니!")
    
    $ typing(jiwoo_blind, "근데 이 친구는 누구? 처음 보는데? 연구실 이번에 들어온 거야?")
    $ typing(dawon, "응 [user]라고, 들어온 지 얼마 안 됐어. 나랑 동갑.")
    
    $ typing(jiwoo_blind, "[user] 안녕?")
    $ typing(user, "안녕하세요.")
    # 서브 캐릭터 1의 실제 이름으로 정체 고정 [cite: 24]
    $ jiwoo_name_ui = side1_char_name  # 휴대폰 UI 이름 동기화
    $ typing(jiwoo, "나는 " + side1_char_name + "라고 해.")
    $ apply_affinity_change("jiwoo", 30)
    
    $ typing(jiwoo, "[user] 있는지 모르고 내 것랑 얘 것만 사 왔네. 다음에 사줄게!")
    $ typing(user, "아니에요, 괜찮습니다.")

    jump talk_4