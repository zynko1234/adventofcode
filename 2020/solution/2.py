from nltk.tokenize import RegexpTokenizer

MIN_COUNT_OFF = 0
MAX_COUNT_OFF = 1
CHAR_OFF = 2
PWD_OFF = 3
INPUT_REGEX_TOK = r'\s+|-|:'


def solve(in_list: list):
    dig_list = digest_input(in_list)
    return count_criteria_a(dig_list), count_criteria_b(dig_list)


def digest_input(in_list: list):
    out_list = []
    tk = RegexpTokenizer(INPUT_REGEX_TOK, gaps=True)

    for entry in in_list:
        out_list.append(tk.tokenize(entry))

    return out_list


def count_criteria_a(in_list: list) -> int:
    req_char = str()
    pwd = str()
    min = 0
    max = 0
    occur_counter = 0
    valid_counter = 0

    for entry in in_list:
        min = int(entry[MIN_COUNT_OFF])
        max = int(entry[MAX_COUNT_OFF])
        req_char = str(entry[CHAR_OFF])
        pwd = str(entry[PWD_OFF])

        occur_counter = pwd.count(req_char)

        if (occur_counter >= min) and (occur_counter <= max):
            valid_counter += 1

    return valid_counter


def count_criteria_b(in_list: list) -> int:
    req_char = str()
    pwd = str()
    posOne = 0
    posTwo = 0
    valid_counter = 0

    for entry in in_list:
        posOne = (int(entry[MIN_COUNT_OFF]) - 1)
        posTwo = (int(entry[MAX_COUNT_OFF]) - 1)
        req_char = str(entry[CHAR_OFF])
        pwd = str(entry[PWD_OFF])

        if (pwd[posOne] is req_char) ^ (pwd[posTwo] is req_char):
            valid_counter += 1

    return valid_counter
