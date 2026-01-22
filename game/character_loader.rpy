init python:
    CHARACTER_DIR = "character"

    def load_text(path):
        with renpy.open_file(path, encoding="utf-8") as f:
            return f.read().strip()

    def load_characters():
        result = {}

        # 🔥 캐릭터 ID 목록 파일
        index_path = CHARACTER_DIR + "/characters.txt"

        if not renpy.loader.loadable(index_path):
            renpy.error("character/characters.txt 파일이 없습니다.")

        ids = load_text(index_path).splitlines()

        for cid in ids:
            base = CHARACTER_DIR + "/" + cid

            result[cid] = {
                "name": load_text(base + "/name.txt"),
                "prompt": load_text(base + "/prompt.txt"),
                "intro": load_text(base + "/intro.txt"),
            }

        return result

    all_characters = load_characters()
