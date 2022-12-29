import copy

import numpy as np
import matplotlib.pyplot as plt

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

    ret = min(traverse_map(start_i, start_j, input, None))

    return ret


def solutionB(input):
    ret = 0

    return ret


def traverse_map (curr_i, curr_j, map, solution=None):
    # Lazy init the solution to the upper bound.
    if solution is None:
        solution = set()

    local_map = copy.deepcopy(map)

    # Check if we're currently sitting on the end node.
    curr_element = local_map[curr_i][curr_j]

    if curr_element[2] == 'E':
        solution.add(count_map(local_map))
        return solution
    else:
        # Else, mark that we've traversed this element
        local_map[curr_i][curr_j][1] = True

    curr_height = curr_element[0]

    # Check up and recurse.
    if is_traversable(curr_height, curr_i - 1, curr_j, local_map):
        traverse_map(curr_i - 1, curr_j, local_map, solution)

    # Check down and recurse.
    if is_traversable(curr_height, curr_i + 1, curr_j, local_map):
        traverse_map(curr_i + 1, curr_j, local_map, solution)

    # Check left and recurse.
    if is_traversable(curr_height, curr_i, curr_j - 1, local_map):
        traverse_map(curr_i, curr_j - 1, local_map, solution)

    # Check right and recurse.
    if is_traversable(curr_height, curr_i, curr_j + 1, local_map):
        traverse_map(curr_i, curr_j + 1, local_map, solution)

    return solution


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

