def solve(in_list):
    ansA = 0
    ansB = None

    normalized_input = normalize_input(in_list)

    ansA = simulate_population(normalized_input, 80)
    ansB = simulate_population(normalized_input, 256)
    return ansA, ansB

def normalize_input(in_input):
    output = []

    split_input = in_input[0].split(',')

    for entry in split_input:
        output.append(int(entry))

    return output        

def simulate_population(in_list, days):
    count = 0
    fish_list = list(in_list).copy()
    pidgeon_list = 9*[0]
    
    for entry in fish_list:
        pidgeon_list[entry] += 1

    temp = 0

    for i in range(days):
        temp =  pidgeon_list[0]
        pidgeon_list.remove(pidgeon_list[0])
        pidgeon_list.append(temp)
        pidgeon_list[6] += temp

    # Count up the new total population
    for entry in pidgeon_list:
        count += entry

    return count




