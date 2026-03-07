label event_1:
    # [main_role] 슬롯과 [main_char_name] 변수를 사용하여 동적 처리
    $ talk_loop(character_1_id, "너의 역할은 [character_1_name]이야. 플레이어가 논문의 파일이 어디있는지 찾는걸 도와달라고 묻는 상황에서 [character_1_name]이 \"도와줄까?\"라고 물어본 상황이다. 파일은 플레이어의 USB에 있지만, 플레이어는 USB에 파일이 있는지 모르는 상황이다. 어디있는지는 절대로 말을 하지 않고 플레이어가 말한 내용에 맞춰서 대꾸만 해야한다./ 플레이어가 도와달라는 뉘앙스로 말을 하면 '그래'라는 말을 한 직후 종료된다.", last_char_line="도와줄까?")
    show character_1 normal at left
    if character_1_id == "dawon":
        # 동갑내기 친구 / 털털한 성격
        $ typing(character_1, "너 USB 완전 신 모시듯 가지고 있었잖아. 거기 있는 거 아니야?")
        
    elif character_1_id == "jiwoo":
        # 연상 / 누나, 언니 같은 다정한 성격
        $ typing(character_1, f"{player_name}{iya(player_name)}, 너 USB 엄청 끔찍하게 아끼잖아. 거기에 둔 거 아니야?")
        
    elif character_1_id == "suah":
        # 연하 / 싹싹하고 발랄한 후배 성격
        $ typing(character_1, "선배님 USB 완전 소중하게 챙기시잖아요! 혹시 거기에 있는 거 아닐까요?")
    
    elif character_1_id == "yeji":
        # 연하 / 싹싹하고 발랄한 후배 성격
        $ typing(character_1, "선배님 USB 완전 소중하게 챙기시잖아요! 혹시 거기에 있는 거 아닐까요?")
    
    elif character_1_id == "huieun":
        # 연하 / 싹싹하고 발랄한 후배 성격
        $ typing(character_1, "선배님 USB 완전 소중하게 챙기시잖아요! 혹시 거기에 있는 거 아닐까요?")
    
    else:
        # 혹시 모를 예외 상황을 위한 기본 대사
        $ typing(character_1, "너 USB 완전 신 모시듯 가지고 있었잖아. 거기 있는 거 아니야?")
    jump talk_2