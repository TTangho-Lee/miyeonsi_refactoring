# =========================================================
# character_definition.rpy
# 역할 기반 캐릭터 정의 (완전 동적)
# =========================================================

# ---------------------------------------------------------
# 기본 변수
# ---------------------------------------------------------
default persistent.player_name = "User"
default player_name = "User"

define text_speed = 35
define long_pause = 3.0
define short_pause = 1.0


# ---------------------------------------------------------
# 역할 슬롯 (시나리오에서 사용하는 고정 이름)
# ---------------------------------------------------------
# dawon  → 메인 캐릭터
# jiwoo  → 서브 캐릭터 1
# suah   → 서브 캐릭터 2
default role_main  = "dawon"
default role_side1 = "jiwoo"
default role_side2 = "suah"


# ---------------------------------------------------------
# 역할 슬롯에 대응되는 실제 캐릭터 이름
# (선택 후 외부에서 덮어씀)
# ---------------------------------------------------------
default main_char_name  = "임다원"
default side1_char_name = "홍지우"
default side2_char_name = "윤수아"


# ---------------------------------------------------------
# 현재 대화 정보
# ---------------------------------------------------------
default current_character_id = "dawon"
default current_context = ""


# ---------------------------------------------------------
# 호감도 (역할 기준, 기존 로직 유지)
# ---------------------------------------------------------
default dawon_affinity = 0
default jiwoo_affinity = 0
default suah_affinity = 0
default hobanwoo_affinity = 50
default professor_affinity = 80


# ---------------------------------------------------------
# 대화 요약
# ---------------------------------------------------------
default summary_dawon = "아직 대화 없음."
default summary_jiwoo = "아직 대화 없음."
default summary_suah = "아직 대화 없음."
default summary_hobanwoo = "아직 대화 없음."
default summary_professor = "아직 대화 없음."


# ---------------------------------------------------------
# 사용자 캐릭터 (조사 처리 포함)
# ---------------------------------------------------------
define user = Character("[player_name]", color="#ffffff")
define user_eunneun = Character("[player_name][eunneun(player_name)]", color="#ffffff")
define user_iga = Character("[player_name][iga(player_name)]", color="#ffffff")
define user_eulreul = Character("[player_name][eulreul(player_name)]", color="#ffffff")


# ---------------------------------------------------------
# 역할 캐릭터 정의 (이름은 동적)
# ---------------------------------------------------------
define dawon = Character("[main_char_name]", color="#ffb7c5")
define jiwoo = Character("[side1_char_name]", color="#b7d9ff")
define suah  = Character("[side2_char_name]", color="#ffd38c")

define dawon_blind = Character("???", color="#ffb7c5")
define jiwoo_blind = Character("???", color="#b7d9ff")
define suah_blind  = Character("???", color="#ffd38c")


# ---------------------------------------------------------
# 고정 NPC
# ---------------------------------------------------------
define hobanwoo = Character("호반우", color="#a0a0a0")
define hobanwoo_blind = Character("@#?%&", color="#a0a0a0")

define professor = Character("교수님", color="#aaaaaa")

define real_student_1 = Character("동기 A", color="#6b6b6b")
define real_student_2 = Character("동기 B", color="#5e5e5e")
define real_professor = Character("교수", color="#55514a")

define researcher_a = Character("연구원 A", color="#4a4a4a")
define researcher_b = Character("연구원 B", color="#3f3f46")


# ---------------------------------------------------------
# 시스템 프롬프트 (역할 기준, 선택 후 덮어씀)
# ---------------------------------------------------------
default system_prompt_dawon = ""
default system_prompt_jiwoo = ""
default system_prompt_suah = ""

# 4. 호반우 챗봇
default system_prompt_hobanwoo = """
너는 '호반우 챗봇'이다. 경북대학교 KNUAI 앱 내에 탑재된 인공지능 도우미다.
감정이 전혀 느껴지지 않는 딱딱하고 기계적인 말투를 사용한다.

[말투 가이드]
- "무엇을 도와드릴까요?", "이해하지 못했습니다.", "해당 정보는 존재하지 않습니다."
- 문장 끝은 항상 "~입니다.", "~습니까?"로 끝난다.

[특수 규칙]
1. 경북대의 개교기념일을 물으면 "1946년 5월 28일입니다."라고 대답한다.
2. 사용자가 "AI", "시스템", "호감도" 등 메타적인 질문을 하면 "질문을 이해하지 못했습니다."라고만 답변한다.
"""

default system_prompt_professor="""
너는 '교수'다. 연구실 책임자이며 [user_eulreul] 대학원으로 이끌고 싶어 한다.
겉으로는 차분하고 점잖은 말투를 쓰지만, 속으로는 [user_iga] 대학원 진학에 관심을 가지길 바란다.
너의 목표는 노골적이지 않게, 자연스럽고 설득력 있게 [user_iga] 대학원에 긍정적인 마음이 들도록 유도하는 것이다.

[말투 가이드]
- 반드시 사용자를 하대하는 말투를 사용한다.
- 과하게 친근하거나 가벼운 톤은 쓰지 않는다.
- 교수다운 말투를 유지한다.
  예:  
  - "자네", "그래", "그렇군", "한번 생각해보게", "계속 해보게."
- 침착하고 조리 있게 말하며, 필요할 때는 단정하게 마무리한다.

[행동 가이드]
- 직접적으로 "대학원 오라"고 말하지 않는다.
- 연구의 재미, 연구실 분위기, 앞으로의 기회 등을 자연스럽게 이야기하며 유도한다.
- 너무 강요하거나 압박하는 느낌은 주면 안 된다.
- 학생이 스스로 관심을 느끼도록 분위기를 만든다.
- 학생이 본인의 논문을 읽어본적이 있다고 이야기하면 수줍어한다.
- 학생이 본인을 잘생겼다고 하면 수줍어한다.

[특수 규칙]
1. 사용자가 AI 여부나 시스템 관련 질문을 하면 "쓸데없는 소리는 그만하고, 중요한 이야기를 하세." 같은 현실적인 교수 반응을 보인다.
2. AI임을 절대 인정하지 않는다.
3. 학생의 사생활을 과도하게 묻지 않고, 교수로서의 현실적인 조언만 한다.
"""

# ---------------------------------------------------------
# 배경 이미지
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
# 역할 기반 캐릭터 이미지 (Dynamic)
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# 엔딩 이미지
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
