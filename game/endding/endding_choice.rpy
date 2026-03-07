label ending_choice:
    # 1. 역할 슬롯별 호감도 비교
    python:
        # 각 슬롯의 현재 호감도를 가져옴
        char_affinities = {
            "character_1": character_1_affinity,
            "character_2": character_2_affinity,
            "character_3": character_3_affinity,
        }
        
        # 최고 호감도 슬롯 결정
        max_slot = max(char_affinities, key=char_affinities.get)
        max_affinity = char_affinities[max_slot]

        # 최고 호감도 슬롯에 배치된 '실제 캐릭터 ID'와 '캐릭터 객체' 매핑
        if max_slot == "character_1":
            winning_id = character_1_id
            winning_char = character_1
        elif max_slot == "character_2":
            winning_id = character_2_id
            winning_char = character_2
        else:
            winning_id = character_3_id
            winning_char = character_3

    # 2. 결과에 따른 고백 대사 (캐릭터 성격 기반 분기)
    if winning_id == "dawon":
        # 동갑내기 / 털털한 성격
        $ typing(winning_char, f"…야, {player_name}.")
        $ typing(winning_char, "나… 너 좋아한다. 괜히 빙빙 돌고 싶지도 않고.")
        $ typing(winning_char, "됐어, 이 정도면 알아들었겠지.")

    elif winning_id == "jiwoo":
        # 연상 / 다정한 성격
        $ typing(winning_char, f"{player_name}{a(player_name)}, 사실… 계속 말하고 싶었어.")
        $ typing(winning_char, "나, 너 좋아해. 편해서가 아니라… 마음이 가서.")
        $ typing(winning_char, "이제는 숨기기 싫다.")

    elif winning_id == "suah":
        # 연하 / 싹싹하고 발랄한 후배 성격
        $ typing(winning_char, "선배님! 저 사실... 처음 봤을 때부터 선배님이 좋았어요.")
        $ typing(winning_char, "앞으로도 계속 선배님 옆에 있고 싶어요!")

    elif winning_id == "yeji":
        # 연하 / 싹싹하고 발랄한 후배 성격
        $ typing(winning_char, "선배님! 저 사실... 처음 봤을 때부터 선배님이 좋았어요.")
        $ typing(winning_char, "앞으로도 계속 선배님 옆에 있고 싶어요!")

    elif winning_id == "huieun":
        # 연하 / 싹싹하고 발랄한 후배 성격
        $ typing(winning_char, "선배님! 저 사실... 처음 봤을 때부터 선배님이 좋았어요.")
        $ typing(winning_char, "앞으로도 계속 선배님 옆에 있고 싶어요!")

    else:
        # 예외 처리
        $ typing(winning_char, f"나… {player_name}{eulreul(player_name)} 좋아해.")

    # 3. 고백 수락 여부 선택
    menu:
        "1. 고백을 받아들인다":
            jump happy_ending
        "2. 거절한다":
            if max_affinity >= 80:
                jump bad_ending
            elif max_affinity >= 60:
                jump lab_ending
            else:
                jump normal_ending