import copy

def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = solutionA(normalized_input)
    ansB = solutionB(normalized_input)
    return ansA, ansB


def normalize_input(input):
    ret = []

    for line in input:
        new_row = []

        for element in line:
            # Height, been_traversed, start/end marker.
            new_index = [None, False, None]

            if element == 'S' or element == 'E':
                new_index[0] = 1 if element == 'S' else 26
                new_index[2] = element
            else:
                # a -> 0, b -> 1... z->25
                new_index[0] = (ord(element) - 96)
                new_index[2] = '-'
            new_row.append(new_index)
        ret.append(new_row)

    return ret


def solutionA(input):
    ret = 0
    start_i = None
    start_j = None

    for i in range(len(input)):
        for j in range(len(input[i])):
            element = input[i][j]
            if element[2] == 'S':
                start_i = i
                start_j = j
                break

        if start_i != None and start_j != None:
            break

    candidate_solutions = traverse_map(start_i, start_j, input, None)
    ret = min(candidate_solutions)

    return ret


def solutionB(input):
    ret = 0

    return ret


def traverse_map (curr_i, curr_j, map, solutions=None):
    # Lazy init the list of solutions.
    if solutions is None:
        solutions = []

    local_map = copy.deepcopy(map)

    # Check if we're currently sitting on the end node.
    curr_element = local_map[curr_i][curr_j]

    if curr_element[2] == 'E':
        solutions.append(count_map(local_map))
        print(f'Solution found! {solutions[-1]}')
        return solutions
    else:
        # Else, mark that we've traversed this element
        local_map[curr_i][curr_j][1] = True

    curr_height = curr_element[0]

    # Check up and recurse.
    if is_traversable(curr_height, curr_i - 1, curr_j, local_map):
        traverse_map(curr_i - 1, curr_j, local_map, solutions)


    # Check down and recurse.
    if is_traversable(curr_height, curr_i + 1, curr_j, local_map):
        traverse_map(curr_i + 1, curr_j, local_map, solutions)

    # Check left and recurse.
    if is_traversable(curr_height, curr_i, curr_j - 1, local_map):
        traverse_map(curr_i, curr_j - 1, local_map, solutions)

    # Check right and recurse.
    if is_traversable(curr_height, curr_i, curr_j + 1, local_map):
        traverse_map(curr_i, curr_j + 1, local_map, solutions)

    return solutions


def count_map(map):
    ret = 0

    for row in map:
        for element in row:
            if element[1] == True:
                ret += 1

    return ret

def is_traversable(current_height, check_i, check_j, map) -> bool:

    # Check bounds.
    if check_i < 0 or check_j < 0:
        return False

    if check_i >= len(map) or check_j >= len(map[0]):
        return False

    # Check accessibility.
    element = map[check_i][check_j]

    if element[1] == True:
        return False

    if abs(current_height - element[0]) > 1:
        return False

    # If all tests pass, then the given element is accessible.
    return True
