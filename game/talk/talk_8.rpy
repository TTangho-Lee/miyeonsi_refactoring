label talk_8:
    "정전되었던 불이 다시 켜진다."
    scene bg lab with fade
    show main_role normal at left
    show sub_role1 normal at center
    show sub_role2 normal at right
    
    $ typing(sub_role2, "뭐, 뭐죠?")
    $ typing(main_role, "원래 정전이 이렇게 갑자기 오는 거야?")
    $ typing(sub_role1, "심장 떨어지는 줄 알았네... 오늘은 집으로 돌아가는 게 좋겠어..")
    
    jump event_8