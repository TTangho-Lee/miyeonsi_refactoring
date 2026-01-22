label event_8:
    # 서브 히로인 1(sub_role1) 슬롯을 사용하여 대화 진행
    $ talk_loop("sub_role1", f"너의 역할은 {side1_char_name}야. 정전이 되었다가 막 불이 돌아와서 {side1_char_name}가 집에 가야겠다고 언급한 상황이다. 플레이어가 집을 가겠다는 말을 하도록 유도하여라./ 플레이어로부터 집에 가자고 입력을 받으면 종료된다.", last_char_line="그냥... 오늘은 집으로 돌아가는게 좋겠어..")
    jump talk_9