label event_12:
    scene bg lab
    menu:
        "1. [main_char_name]와 놀자":
            show main_role smile
            $ typing(main_role, "놀자고? 그래 ✨")
            $ apply_affinity_change("main_role", 20)
            $ send_notification(f"{main_char_name} 호감도 +20")
            $ talk_loop_center("main_role", f"너의 역할은 {main_char_name}야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ Current Affinity가 80 이상이거나, 플레이어가 대화를 마무리하려는 말을 할 때 'goal_achievement: true'를 출력하여 대화를 종료하여라.", last_char_line="놀자고? 그래 ✨")
            jump ending_choice

        "2. [side1_char_name]와 놀자":
            show sub_role1 smile
            $ typing(sub_role1, "같이 놀자구? ㅋㅋㅋ 좋아")
            $ apply_affinity_change("sub_role1", 20)
            $ send_notification(f"{side1_char_name} 호감도 +20")
            $ talk_loop_center("sub_role1", f"너의 역할은 {side1_char_name}야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ Current Affinity가 80 이상이거나, 플레이어가 대화를 마무리하려는 말을 할 때 'goal_achievement: true'를 출력하여 대화를 종료하여라.", last_char_line="같이 놀자구? ㅋㅋㅋ 좋아")
            jump ending_choice

        "3. [side2_char_name]와 놀자":
            show sub_role2 smile
            $ typing(sub_role2, "우와! 선배님이랑 노는 거 완전 좋아요!")
            $ apply_affinity_change("sub_role2", 20)
            $ send_notification(f"{side2_char_name} 호감도 +20")
            $ talk_loop_center("sub_role2", f"너의 역할은 {side2_char_name}야. 플레이어와 친밀한 분위기에서 자유롭게 대화를 진행해./ Current Affinity가 80 이상이거나, 플레이어가 대화를 마무리하려는 말을 할 때 'goal_achievement: true'를 출력하여 대화를 종료하여라.", last_char_line="우와! 선배님이랑 노는 거 완전 좋아요!")
            jump ending_choice