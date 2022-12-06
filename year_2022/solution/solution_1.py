def solve(in_list):
    ansA = None
    ansB = None

    elfs = normalize_input(in_list)

    ansA = partA(elfs)
    ansB = partB(elfs)
    return ansA, ansB

def partA(elfs):
    ret = None
    calories = []

    for elf in elfs:
        tmp_calories = 0
        for food_item in elf:
            tmp_calories += food_item

        calories.append(tmp_calories)

    ret = max(calories)

    return ret

def partB(elfs):
    ret = None
    calories = []

    for elf in elfs:
        tmp_calories = 0
        for food_item in elf:
            tmp_calories += food_item

        calories.append(tmp_calories)

    calories.sort(reverse=True)
    ret = calories[0] + calories[1] + calories[2]
    return ret


def normalize_input(input):
    elfs = []
    tmp_elf = []

    for line in input:
        if line != '':
            tmp_elf.append(int(line))
        else:
            elfs.append(tmp_elf)
            tmp_elf = []


    return elfs



