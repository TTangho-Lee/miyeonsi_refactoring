label ending_choice:
    # 1. 역할 슬롯별 호감도 비교
    python:
        # 각 슬롯의 현재 호감도를 가져옴
        char_affinities = {
            "main_role": main_role_affinity,
            "sub_role1": sub_role1_affinity,
            "sub_role2": sub_role2_affinity,
        }
        
        # 최고 호감도 슬롯 결정
        max_slot_id = max(char_affinities, key=char_affinities.get)
        max_affinity = char_affinities[max_slot_id]

    # 2. 결과에 따른 고백 대사 (슬롯 기반)
    if max_slot_id == "main_role":
        $ typing(main_role, "…야, [player_name].")
        $ typing(main_role, "나… 너 좋아한다. 괜히 빙빙 돌고 싶지도 않고.")
        $ typing(main_role, "됐어, 이 정도면 알아들었겠지.")

    elif max_slot_id == "sub_role1":
        $ typing(sub_role1, "[player_name], 사실… 계속 말하고 싶었어.")
        $ typing(sub_role1, "나, 너 좋아해. 편해서가 아니라… 마음이 가서.")
        $ typing(sub_role1, "이제는 숨기기 싫다.")

    elif max_slot_id == "sub_role2":
        $ typing(sub_role2, "선배님! 저 사실... 처음 봤을 때부터 선배님이 좋았어요.")
        $ typing(sub_role2, "앞으로도 계속 선배님 옆에 있고 싶어요!")

    # 3. 고백 수락 여부 선택
    menu:
        "1. 고백을 받아들인다":
            jump happy_ending
        "2. 거절한다":
            if max_affinity>=80:
                jump bad_ending
            elif max_affinity>=60:
                jump lab_ending
            else:
                jump normal_ending