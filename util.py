import constants
import copy

def read_file(in_file: str) -> list:
    out_list = []
    file_handle = open(in_file)
    lines = file_handle.readlines()

    for entry in lines:
        out_list.append(entry.replace('\n', constants.EMPTY_STRING))

    return out_list

def split_list(in_list, tuple_index):
    out_list = list(list(zip(*in_list))[tuple_index])
    return out_list

def sum_list(in_list):
    out_sum = 0
    
    for i in range(len(in_list)):
        out_sum += in_list[i]

    return out_sum

def replace_char(in_str, in_idx, in_subst):
    out_string = in_str[:in_idx] + in_subst + in_str[in_idx+1:]
    return out_string


def remove_dupe(input: list) -> list:
    ''' 
    Returns a list populated by the input lists elements with no two elements te same.
    '''

    return list(dict.fromkeys(input))

def sort_and_remove_dup(input: list) -> list:
    '''
    Returns a sorted version of the input list, with all duplicate elements removed.
    '''

    output = copy.deepcopy(input)
    output = remove_dupe(output)
    return output.sort()

def gen_2d_array_list(i: int, j: int) -> list:
    output = i*[list()]

    for entry in output:
        tmp = j*[0]
        entry.append(tmp)

    return output

def get_min(a: int, b: int) -> int:
    if a > b:
        return b
    else:
        return a

def get_max(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b