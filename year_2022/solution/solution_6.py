
def solve(in_list):
    ansA = None
    ansB = None

    data = normalize_input(in_list)

    ansA = partA(data)
    ansB = partB(data)
    return ansA, ansB

def partA(data):
    ret = 0
    width = 4
    buffer = []

    for glyph in data:

        if len(buffer) == width:
            tmp_set = set(buffer)

            # Check for 4 unique characters.
            if len(tmp_set) == width:
                break
            else:
                buffer = buffer[1:]
                buffer.append(glyph)

        else:
            buffer.append(glyph)

        ret += 1

    return ret

def partB(data):
    ret = 0
    width = 14
    buffer = []

    for glyph in data:

        if len(buffer) == width:
            tmp_set = set(buffer)

            # Check for 4 unique characters.
            if len(tmp_set) == width:
                break
            else:
                buffer = buffer[1:]
                buffer.append(glyph)

        else:
            buffer.append(glyph)

        ret += 1

    return ret


def normalize_input(input):
    ret = input[0]

    return ret

