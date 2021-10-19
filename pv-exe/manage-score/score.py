import os
import touch
path_to_score_file = os.getenv("SCORE_FILE")


def file_is_empty(file):
    import re
    content = file.read()
    file.seek(0)
    if re.search(r'^\s*$', content):
        return True
    return False


def add_score(value):
    init()
    with open(path_to_score_file, 'r+') as file:
        data = get_current_score(file)
        new_score = str(data + value)
        file.write(new_score)
        print(f"current score is {new_score}")


def get_current_score(file):
    if file_is_empty(file):
        print(f"file {path_to_score_file} is empty")
        data = 0
    else:
        score_from_file = file.read()
        print(f"score from file: {score_from_file}")
        if len(score_from_file) == 0:
            data = 0
        else:
            data = int(score_from_file)
    file.seek(0)
    return data


def init():
    if not os.path.exists(path_to_score_file):
        touch.touch(path_to_score_file)


add_score(5)
