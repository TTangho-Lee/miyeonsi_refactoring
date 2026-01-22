label talk_7:
    "갑자기 정전된다." 
    scene bg black with fade
    hide main_role
    hide sub_role1
    hide sub_role2

    $ typing(sub_role2, "꺄악.~!~!~!~!~~!")
    $ typing(sub_role1, "갑자기 뭐야!?")
    $ typing(main_role, "뭐야...왜 이래...")
    
    jump event_7