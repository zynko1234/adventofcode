alpha_vals = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
    'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
    't':20, 'u':21, 'v':22,'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28,
    'C':29, 'D':30, 'E':31, 'F':32,'G':33, 'H':34, 'I':35, 'J':36, 'K':37,
    'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46,
    'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52,
}

def solve(in_list):
    ansA = None
    ansB = None

    rucksacks = normalize_input(in_list)

    ansA = partA(rucksacks)
    ansB = partB(in_list)
    return ansA, ansB

def partA(rucksacks):
    ret = 0

    for compartments in rucksacks:
        setA = set()
        setB = set()
        # Create sets from the two split compartments, and find their common
        # items.
        for item in compartments[0]:
            setA.add(item)
        for item in compartments[1]:
            setB.add(item)

        common_set = setA.intersection(setB)
        ret += alpha_vals[common_set.pop()]

    return ret

def partB(in_list):
    ret = 0
    set_list = []
    item = None

    for i in range(len(in_list)):
        tmp_set = set()
        for item in in_list[i]:
            tmp_set.add(item)
        set_list.append(tmp_set)

        if len(set_list) == 3:
            common_set = set_list[0].intersection(set_list[1], set_list[2])
            ret += alpha_vals[common_set.pop()]
            set_list = []

    return ret

def normalize_input(input):
    ret = []

    for line in input:
        split_len = int(len(line) / 2)
        ret.append([line[:split_len], line[split_len:]])

    return ret
