# =========================================================
# character_definition.rpy
# 역할 기반 캐릭터 정의 (완전 동적 시스템)
# =========================================================

# ---------------------------------------------------------
# 1. 기본 및 시스템 변수
# ---------------------------------------------------------
default persistent.player_name = "User"
default player_name = "User"

define text_speed = 35
define long_pause = 3.0
define short_pause = 1.0

# ---------------------------------------------------------
# 2. 역할 슬롯 (시나리오 고정 ID)
# ---------------------------------------------------------
# 게임 코드 내에서는 항상 dawon, jiwoo, suah 슬롯을 사용하지만, 
# 실제 값(role_xxx)은 사용자가 선택한 캐릭터의 ID(폴더명)로 채워집니다. [cite: 16]
default role_main  = "dawon"
default role_side1 = "jiwoo"
default role_side2 = "suah"

# ---------------------------------------------------------
# 3. 역할 슬롯별 동적 이름
# ---------------------------------------------------------
# 선택한 캐릭터의 name.txt 정보가 여기에 할당되어 대사창에 표시됩니다. [cite: 16, 18]
default main_char_name  = "임다원"
default side1_char_name = "홍지우"
default side2_char_name = "윤수아"

# ---------------------------------------------------------
# 4. 현재 대화 및 컨텍스트 정보
# ---------------------------------------------------------
default current_character_id = "dawon"
default current_context = ""

# ---------------------------------------------------------
# 5. 호감도 및 대화 기록 (슬롯 기준 고정)
# ---------------------------------------------------------
default dawon_affinity = 0
default jiwoo_affinity = 0
default suah_affinity = 0
default hobanwoo_affinity = 50
default professor_affinity = 80

default summary_dawon = "아직 대화 없음."
default summary_jiwoo = "아직 대화 없음."
default summary_suah = "아직 대화 없음."
default summary_hobanwoo = "아직 대화 없음."
default summary_professor = "아직 대화 없음."

# ---------------------------------------------------------
# 6. 캐릭터 객체 정의 (이름 동적 반영)
# ---------------------------------------------------------
# [사용자] 조사 처리 포함
define user = Character("[player_name]", color="#ffffff")
define user_eunneun = Character("[player_name][eunneun(player_name)]", color="#ffffff")
define user_iga = Character("[player_name][iga(player_name)]", color="#ffffff")
define user_eulreul = Character("[player_name][eulreul(player_name)]", color="#ffffff")

# [역할 슬롯] 대사창 이름을 변수로 참조 [cite: 18]
define dawon = Character("[main_char_name]", color="#ffb7c5")
define jiwoo = Character("[side1_char_name]", color="#b7d9ff")
define suah  = Character("[side2_char_name]", color="#ffd38c")

define dawon_blind = Character("???", color="#ffb7c5")
define jiwoo_blind = Character("???", color="#b7d9ff")
define suah_blind  = Character("???", color="#ffd38c")

# [고정 NPC]
define hobanwoo = Character("호반우", color="#a0a0a0")
define hobanwoo_blind = Character("@#?%&", color="#a0a0a0")
define professor = Character("교수님", color="#aaaaaa")

# [배경 NPC]
define real_student_1 = Character("동기 A", color="#6b6b6b")
define real_student_2 = Character("동기 B", color="#5e5e5e")
define real_professor = Character("교수", color="#55514a")
define researcher_a = Character("연구원 A", color="#4a4a4a")
define researcher_b = Character("연구원 B", color="#3f3f46")

# ---------------------------------------------------------
# 7. 시스템 프롬프트 (동적 슬롯 및 고정 NPC)
# ---------------------------------------------------------
# 슬롯 캐릭터의 프롬프트는 선택 시 prompt.txt 내용으로 채워집니다. [cite: 19]
default system_prompt_dawon = ""
default system_prompt_jiwoo = ""
default system_prompt_suah = ""

default system_prompt_hobanwoo = """
너는 '호반우 챗봇'이다. 경북대학교 KNUAI 앱 내에 탑재된 인공지능 도우미다. [cite: 130]
감정이 전혀 느껴지지 않는 딱딱하고 기계적인 말투를 사용한다. [cite: 131]
[말투 가이드]
- "무엇을 도와드릴까요?", "이해하지 못했습니다.", "해당 정보는 존재하지 않습니다." [cite: 131]
- 문장 끝은 항상 "~입니다.", "~습니까?"로 끝난다. [cite: 132]
"""

default system_prompt_professor="""
너는 '교수'다. 연구실 책임자이며 [user_eulreul] 대학원으로 이끌고 싶어 한다. [cite: 134]
[말투 가이드]
- 반드시 사용자를 하대하는 말투를 사용한다. [cite: 136]
- 교수다운 말투를 유지한다(자네, 그래, 그렇군). [cite: 136, 137]
- 학생이 본인을 잘생겼다고 하거나 논문을 읽었다고 하면 수줍어한다.
"""

# ---------------------------------------------------------
# 8. 배경 이미지 정의
# ---------------------------------------------------------
image bg lab = im.Scale("images/background/lab.png", config.screen_width, config.screen_height)
image bg my_computer = im.Scale("images/background/my_computer.png", config.screen_width, config.screen_height)
image bg restaurant = im.Scale("images/background/restaurant.png", config.screen_width, config.screen_height)
image bg home = im.Scale("images/background/home.png", config.screen_width, config.screen_height)
image bg sunset = im.Scale("images/background/sunset.png", config.screen_width, config.screen_height)
image bg sunset_dawon = im.Scale("images/background/sunset_dawon.png", config.screen_width, config.screen_height)
image bg sunset_jiwoo = im.Scale("images/background/sunset_jiwoo.png", config.screen_width, config.screen_height)
image bg sunset_suah = im.Scale("images/background/sunset_suah.png", config.screen_width, config.screen_height)
image bg truck = im.Scale("images/background/truck.png", config.screen_width, config.screen_height)
image bg black = "#000000"
image bg lab_ending = im.Scale("images/background/lab_ending.png", config.screen_width, config.screen_height)
image bg hand = im.Scale("images/background/hand.png", config.screen_width, config.screen_height)

# ---------------------------------------------------------
# 9. 역할 기반 캐릭터 이미지 (DynamicImage 활용)
# ---------------------------------------------------------
# role_main 등의 변수가 변하면 해당 경로의 이미지를 자동으로 로드합니다. [cite: 17]
image dawon normal     = DynamicImage("character/[role_main]/normal.png")
image dawon smile      = DynamicImage("character/[role_main]/smile.png")
image dawon sad        = DynamicImage("character/[role_main]/sad.png")
image dawon angry      = DynamicImage("character/[role_main]/angry.png")
image dawon shy        = DynamicImage("character/[role_main]/shy.png")
image dawon surprised  = DynamicImage("character/[role_main]/surprised.png")

image jiwoo normal     = DynamicImage("character/[role_side1]/normal.png")
image jiwoo smile      = DynamicImage("character/[role_side1]/smile.png")
image jiwoo sad        = DynamicImage("character/[role_side1]/sad.png")
image jiwoo angry      = DynamicImage("character/[role_side1]/angry.png")
image jiwoo shy        = DynamicImage("character/[role_side1]/shy.png")
image jiwoo surprised  = DynamicImage("character/[role_side1]/surprised.png")

image suah normal      = DynamicImage("character/[role_side2]/normal.png")
image suah smile       = DynamicImage("character/[role_side2]/smile.png")
image suah sad         = DynamicImage("character/[role_side2]/sad.png")
image suah angry       = DynamicImage("character/[role_side2]/angry.png")
image suah shy         = DynamicImage("character/[role_side2]/shy.png")
image suah surprised   = DynamicImage("character/[role_side2]/surprised.png")

# 고정 캐릭터 (교수님)
image professor normal = ConditionSwitch("True", "images/professor/normal.png")
image professor smile  = ConditionSwitch("True", "images/professor/smile.png")
image professor sad    = ConditionSwitch("True", "images/professor/sad.png")
image professor angry  = ConditionSwitch("True", "images/professor/angry.png")
image professor shy    = ConditionSwitch("True", "images/professor/shy.png")

# ---------------------------------------------------------
# 10. 엔딩 이미지 정의
# ---------------------------------------------------------
define normal_ending_image = "images/background/main_screen.png"
define lab_ending_image = "images/background/lab_ending.png"
define hobanwoo_angry_ending_image = "images/background/hobanwoo_angry_ending.png"
define dawon_happy_ending_image = "images/background/sunset_dawon.png"
define jiwoo_happy_ending_image = "images/background/sunset_jiwoo.png"
define suah_happy_ending_image = "images/background/sunset_suah.png"
define dream_ending_image = "images/background/dream_ending.png"
define bad_ending_image = "images/background/bad_ending.png"

default persistent.ending_image = normal_ending_image