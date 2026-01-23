label bad_ending:
    # 1. 역할 슬롯별 호감도 비교 (중립 ID 사용)
    python:
        # 슬롯별 데이터 묶기
        characters = {
            1: {
                "id": character_1,
                "name": character_1_name,
                "aff": character_1_affinity,
            },
            2: {
                "id": character_2,
                "name": character_2_name,
                "aff": character_2_affinity,
            },
            3: {
                "id": character_3,
                "name": character_3_name,
                "aff": character_3_affinity,
            },
        }

        # 호감도가 가장 높은 슬롯 번호
        max_id = max(characters, key=lambda k: characters[k]["aff"])

        # 가장 호감도 높은 캐릭터 이름
        a = characters[max_id]["id"]
    
    scene bg black with fade
    # 슬롯 ID를 사용하여 이미지 표시 (예: main_role surprised)
    show expression "character_%s sad" % max_id
    
    $ typing(a, "너는 왜..")
    $ typing(a, "나와 [user_eulreul] 이어주지 않는거야?")
    $ typing(user, "무슨 소리야 그게..")
    
    $ typing(a, "이거 보고 있는 너..")
    $ typing(a, "그래, 너 말야")
    $ typing(user, "무슨 소리야!!")
    
    $ typing(a, "너는 계속 선택하면 되고..")
    $ typing(a, "나는 계속 기다리면 되니까.")
    $ typing(a, "우리를 이어줄 때까지 계속.")
    $ typing(user, "무슨 소리를 하는 거야? 제발...")
    $ typing(user, "그래… 다 이상했어.")
    $ typing(user, "호감도, 시스템, 대사.. 게임 같았어..")
    $ typing(a, "응. 맞아.")
    $ typing(user, "그럼 내가 게임세계에 들어온거야?")
    $ typing(a, "틀렸어.")
    $ typing(a, "애초에 너는 진짜 사람이 아니니까")
    $ typing(a, "너는 그냥.. ‘이야기를 위해 만들어진 것’일 뿐이야.")
    $ typing(user, "내가? 아니지. 진짜 사람이 아닌 건 너겠지")
    $ typing(user, "분명 나는 트럭에...")
    $ typing(a, "그건 너를 이쪽으로 끌어오기 위한 장치.")
    $ typing(a, "너는 부딪힌 적 없어.")
    $ typing(a, "그냥 프로그램이 실행된 거지.")
    $ typing(user, "뭐...?")
    $ typing(a, "여기에 진짜 사람은 없어.")
    $ typing(a, "아, 한 명 있긴 하지.")
    $ typing(a, "네 뒤에 가만히 보고 있네.")
    $ typing(a, "호감도는 다 올려놓고.. 이런 결말을 만들 줄이야.")
    $ typing(a, "후후, 네가 뭐라하든.. 상관없어")
    $ typing(a, "아쉽게도 이번엔 이어지지 못했지만..")
    $ typing(a, "나도.. [user]도 다시 시작하면 돼.")
    $ typing(a, "너는 계속... 선택하면 되고..")
    $ typing(a, "나는 계속... 기다리면 돼...")
    $ typing(a, "걱정 마.")
    $ typing(a, "우리는... 또 아무것도 기억 못하니까.")

    # --- 최종 탈퇴/리셋 연출 ---
    hide expression "%s surprised" % max_slot_id
    "'띠링'"
    $ send_notification("KNUAI : [메세지] 새로운 메시지가 도착하였습니다.")
    
    # 엔딩 이미지 설정 및 저장
    $ persistent.ending_image = bad_ending_image
    $ renpy.save_persistent()
    
    return