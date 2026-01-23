label talk_7:
    "갑자기 정전된다." 
    scene bg black with fade
    hide character_1
    hide character_2
    hide character_3

    $ typing(character_3, "꺄악.~!~!~!~!~~!")
    $ typing(character_2, "갑자기 뭐야!?")
    $ typing(character_1, "뭐야...왜 이래...")
    
    jump event_7