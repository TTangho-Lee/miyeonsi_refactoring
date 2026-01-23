label event_12:
    scene bg lab
    menu:
        "1. [character_1_name]와 놀자":
            show character_1 smile
            $ typing(character_1, "놀자고? 그래 ✨")
            $ apply_affinity_change("character_1", 20)
            $ send_notification(f"{character_1_name} 호감도 +20")
            $ talk_loop_center(character_1_id, f"너의 역할은 {character_1_name}야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ Current Affinity가 80 이상이거나, 플레이어가 대화를 마무리하려는 말을 할 때 'goal_achievement: true'를 출력하여 대화를 종료하여라.", last_char_line="놀자고? 그래 ✨")
            jump ending_choice

        "2. [character_2_name]와 놀자":
            show character_2 smile
            $ typing(character_2, "같이 놀자구? ㅋㅋㅋ 좋아")
            $ apply_affinity_change("character_2", 20)
            $ send_notification(f"{character_2_name} 호감도 +20")
            $ talk_loop_center(character_2_id, f"너의 역할은 {character_2_name}야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ Current Affinity가 80 이상이거나, 플레이어가 대화를 마무리하려는 말을 할 때 'goal_achievement: true'를 출력하여 대화를 종료하여라.", last_char_line="같이 놀자구? ㅋㅋㅋ 좋아")
            jump ending_choice

        "3. [character_3_name]와 놀자":
            show character_3 smile
            $ typing(character_3, "우와! 선배님이랑 노는 거 완전 좋아요!")
            $ apply_affinity_change("character_3", 20)
            $ send_notification(f"{character_3_name} 호감도 +20")
            $ talk_loop_center(character_3_id, f"너의 역할은 {character_3_name}야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ Current Affinity가 80 이상이거나, 플레이어가 대화를 마무리하려는 말을 할 때 'goal_achievement: true'를 출력하여 대화를 종료하여라.", last_char_line="우와! 선배님이랑 노는 거 완전 좋아요!")
            jump ending_choice