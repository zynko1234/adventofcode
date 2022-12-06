

def solve(in_list):
    ansA = None
    ansB = None

    strats = normalize_input(in_list)

    ansA = partA(strats)
    ansB = partB(strats)
    return ansA, ansB

def partA(strats):
    ret = 0

    code = {
        # Maps to the score value of my move based on the opponents move.
        'A': {
            'X': 3,
            'Y': 6,
            'Z': 0,
        },
        'B': {
            'X': 0,
            'Y': 3,
            'Z': 6,
        },
        'C': {
            'X': 6,
            'Y': 0,
            'Z': 3,
        },
        # Maps to the raw point value of my move.
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    for strat in strats:
        ret += code[strat[0]][strat[1]]
        ret += code[strat[1]]

    return ret

def partB(strats):
    ret = 0

    code = {
        # Maps oponents moves to the raw point value of my move dictated by the
        # forced outcome.
        'A': {
            'X': 3,
            'Y': 1,
            'Z': 2,
        },
        'B': {
            'X': 1,
            'Y': 2,
            'Z': 3,
        },
        'C': {
            'X': 2,
            'Y': 3,
            'Z': 1,
        },
        # Maps to the value of winning or losing.
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    for strat in strats:
        ret += code[strat[0]][strat[1]]
        ret += code[strat[1]]

    return ret


def normalize_input(input):
    ret = []

    for line in input:
        ret.append([line[0], line[2]])

    return ret
