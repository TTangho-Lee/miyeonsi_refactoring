label talk_6:
    $ typing(professor, "... 수고하지")
    hide professor
    
    show sub_role1 normal at center
    show sub_role2 normal at right
    $ typing(sub_role1, "이쯤하고~ 오늘은 좀 놀까?")
    $ typing(sub_role2, "그니까요! 제가 간식 가져왔어요!") 
    $ typing(user, "그럴까.. 우선 마무리만 좀 할게요")
    
    $ typing(user, "[main_char_name]아, 이거 워드 파일로 제출하면 끝이야?") # 동적 이름 사용
    $ typing(main_role, "너 진짜 핵심을 찔렀어! 프린트해서 직접 드려야 인정돼! ✨")
    
    jump event_6