label talk_8:
    "정전되었던 불이 다시 켜진다."
    scene bg lab with fade
    show character_1 normal at left
    show character_2 normal at center
    show character_3 normal at right

    $ typing(character_3, "뭐, 뭐죠?")
    $ typing(character_1, "원래 정전이 이렇게 갑자기 오는 거야?")
    $ typing(character_2, "심장 떨어지는 줄 알았네... 오늘은 집으로 돌아가는 게 좋겠어..")

    jump event_8