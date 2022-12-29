import copy
import resource
import sys

from util.lists import CircularList
from util.util import print_progress_bar
from util.util import print_image_progress_bar

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(2**18)

def solve(in_list):
    ansA = None
    ansB = None

    data = normalize_input(in_list)

    # ansA = partA(data)
    ansB = partB(data)
    return ansA, ansB

def partA(input):
    POS_A = 1000
    POS_B = 2000
    POS_C = 3000

    ret = 0
    count = 0
    code = copy.deepcopy(input)

    print(f'Code length before manipulation: {code.length}')

    while count < code.length:
        print_progress_bar(count, code.length)

        for i in range(code.length):
            current_element = code.get_element_at(i)

            if current_element[1] == False:
                current_element[1] = True
                code.shift_element(i, current_element[0])
                count += 1
                break

    # Get the index with the value zero and set it to the 0th index.
    index_of_zero = code.get_index_of_first_occurance([0, True])
    code.zero_index(index_of_zero)

    print(f'Code length after manipulation: {code.length}')

    # Compute the answer.
    index_A = POS_A % code.length
    print(f'Index A: {index_A}')
    valueA = code.get_element_at(index_A)[0]
    print(valueA)
    ret += valueA

    index_B = POS_B % code.length
    print(f'Index B: {index_B}')
    valueB = code.get_element_at(index_B)[0]
    print(valueB)
    ret += valueB

    index_C = POS_C % code.length
    print(f'Index C: {index_C}')
    valueC = code.get_element_at(index_C)[0]
    print(valueC)
    ret += valueC

    return ret

def partB(input):
    POS_A = 1000
    POS_B = 2000
    POS_C = 3000
    ENCRYPTION_KEY = 811589153

    ret = 0
    count = 0
    code = copy.deepcopy(input)
    zero_element = None

    # Set the new values.
    for i in range(code.length):
        current_element = code.get_element_at(i)

        # Need to track the new expanded number for the end calculation.
        new_val = current_element[0] * ENCRYPTION_KEY

        # Reduced number for moving the indexes around.
        mod_val = new_val # (abs(new_val)) & (code.length)

        if current_element[0] > 0:
            current_element[0] = mod_val
            current_element[3] = new_val
        elif current_element[0] < 0:
            # If a number is negative, maintain that after the mod operation.
            current_element[0] = -1 * mod_val
            current_element[3] = new_val
        else:
            # Save off the zero element. No need to modify it.
            zero_element = current_element

    print(f'Code length before manipulation: {code.length}')
    for i in range(10):

        for j in range(code.length):
            print_image_progress_bar(i, j, 10, code.length)

            # Find the next element to move.
            for k in range(code.length):
                current_element = code.get_element_at(k)

                if current_element[2] == i:
                    code.shift_element(k, current_element[0])
                    count += 1
                    break

    # Get the index with the value zero and set it to the 0th index.
    print('Aligning the zero index')
    index_of_zero = code.get_index_of_first_occurance(zero_element)
    code.zero_index(index_of_zero)

    print(f'Code length after manipulation: {code.length}')

    # Compute the answer.
    index_A = POS_A % code.length
    print(f'Index A: {index_A}')
    valueA = code.get_element_at(index_A)[3]
    print(valueA)
    ret += valueA

    index_B = POS_B % code.length
    print(f'Index B: {index_B}')
    valueB = code.get_element_at(index_B)[3]
    print(valueB)
    ret += valueB

    index_C = POS_C % code.length
    print(f'Index C: {index_C}')
    valueC = code.get_element_at(index_C)[3]
    print(valueC)
    ret += valueC

    return ret

def normalize_input(input):
    ret = CircularList()
    data_max = 0
    data_min = 0

    for i in range(len(input)):
        tmp = []
        current = int(input[i])
        data_max = max(current, data_max)
        data_min = min(current, data_min)
        tmp.append(current)
        tmp.append(False)
        tmp.append(i)
        tmp.append(current)

        ret.append(tmp)

    print(f'Max data value: {data_max}')
    print(f'Min data value: {data_min}')
    return ret
