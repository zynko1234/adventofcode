def solve(in_list):
    ansA = 0
    ansB = None

    normalized_input = normalize_input(in_list)

    ansA = simulate_population_a(normalized_input)
    ansB = simulate_population_b(normalized_input)
    return ansA, ansB

def simulate_population_a(in_list):
    
    fish_list = list(in_list).copy()

    for i in range(80):
        new_births = []

        for j in range(len(fish_list)):            
            if fish_list[j] is 0:
                fish_list[j] = 6
                new_births.append(8)
            else:
                fish_list[j] -= 1
            
        fish_list = fish_list + new_births

    return len(fish_list)
        

def simulate_population_b(in_list):
    count = 0
    fish_list = list(in_list).copy()
    pidgeon_list = 9*[0]
    
    for entry in fish_list:
        pidgeon_list[entry] += 1

    temp = 0

    for i in range(256):
        temp =  pidgeon_list[0]
        pidgeon_list.remove(pidgeon_list[0])
        pidgeon_list.append(temp)
        pidgeon_list[6] += temp

    # Count up the new total population
    for entry in pidgeon_list:
        count += entry

    return count

def pidgeon_add(pidgeon_list, item_list):

    for entry in item_list:
        pidgeon_list[entry] += 1

    return pidgeon_list


def normalize_input(in_input):
    output = []

    split_input = in_input[0].split(',')

    for entry in split_input:
        output.append(int(entry))

    return output
