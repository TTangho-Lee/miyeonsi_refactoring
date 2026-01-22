label event_4:
    while True:
        "{cps=[text_speed]}탈퇴하시겠습니까?{/cps}"
        menu:
            "네":
                "{cps=[text_speed]}정말로 탈퇴하시겠습니까? 탈퇴를 하고 난 후의 패널티가 적용됩니다.{/cps}"
                menu:
                    "네":
                        $ send_notification("%s님의 호감도가 -25 하락했습니다." % hobanwoo_blind)
                        $ apply_affinity_change("hobanwoo", -25)

                        if hobanwoo_affinity <= 0:
                            jump hobanwoo_angry
                        jump event_4

                    "아니오":
                        "{cps=[text_speed]}...취소되었습니다.{/cps}"
                        return
            "아니오":
                "{cps=[text_speed]}...취소되었습니다.{/cps}"
                return