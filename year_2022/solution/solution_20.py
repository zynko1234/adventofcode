import copy
import resource
import sys

from util.lists import CircularList
from util.util import print_progress_bar

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(2**18)

def solve(in_list):
    ansA = None
    ansB = None

    data = normalize_input(in_list)

    ansA = partA(data)
    ansB = partB(data)
    return ansA, ansB

def partA(input):
    INDEX_A = 1000
    INDEX_B = 2000
    INDEX_C = 3000

    ret = 0
    count = 0
    code = copy.deepcopy(input)

    while count < code.length:
        print_progress_bar(count, code.length)

        for i in range(count, code.length):
            current_element = code.get_element_at(i)

            if current_element[1] == False:
                current_element[1] = True
                code.shift_element(i, current_element[0])
                count += 1
                break

    # Get the index with the value zero and set it to the 0th index.
    index_of_zero = code.get_index_of_first_occurance([0, True])
    code.zero_index(index_of_zero)

    ret += code.get_element_at(INDEX_A % code.length)[1]
    ret += code.get_element_at(INDEX_B % code.length)[1]
    ret += code.get_element_at(INDEX_C % code.length)[1]

    return ret

def partB(input):
    ret = 0

    return ret

def normalize_input(input):
    ret = CircularList()

    for number in input:
        tmp = []
        tmp.append(int(number))
        tmp.append(False)

        ret.append(tmp)

    return ret
