def solve(in_list):
    ansA = 0
    ansB = None

    normalized_input = normalize_input(in_list)

    ansA = count_ascent(normalized_input)
    ansB = count_window(normalized_input)
    return ansA, ansB

def normalize_input(in_input):
    output = []

    for entry in in_input:
        output.append(int(entry))

    return output

def count_ascent(in_list):
    count = 0

    for i in range(len(in_list)):
        if i > 0:
            if in_list[i] > in_list[i-1]:
                count += 1

    return count

def count_window(in_list):
    count = 0

    for i in range(len(in_list)):
        if i > 0 and ((i + 2) < len(in_list)):

            windowA = in_list[i] + in_list[i+1] + in_list[i + 2]
            windowB = in_list[i-1] + in_list[i] + in_list[i + 1]
            
            if windowA > windowB:
                count += 1

    return count