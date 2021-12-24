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
    output = []

    for q in range(i):
        tmp = j*[0]
        output.append(tmp)

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

def get_max_of_list(input):
    if len(input) > 0:
        currmax = input[0]

    for i in range(1, len(input)):
        currmax = get_max(currmax, input[i])

    return currmax

def get_min_of_list(input):
    if len(input) > 0:
        currmin = input[0]

    for i in range(1, len(input)):
        currmin = get_min(currmin, input[i])

    return currmin

def pad_zero(input: list, add_length: int, left: bool, pad_value = 0):
    output = copy.deepcopy(input)

    if input is None:
        return None
    
    if add_length < 1:
        return input

    if left:
        for i in range(add_length):
            output.insert(0, pad_value)
    else:
        for i in range(add_length):
            output.append(pad_value)
    
    return output

def reverse_2d_list(input: list()):
    '''
    Calls reverse() on each row in a 2D list. Like the normal call of reverse(), this is done in
    place.
    '''

    if input is not None and len(input) > 0:
        if isinstance(input, list):
            for sub_list in input:
                sub_list.reverse()

def pad_lines(input: list, add_length: int, top: bool, pad_value = 0):
    '''
    Takes a 2D list of ideally consistent width, and pads the top or bottom with single lists of
    the given pad values. The width of the padding will be the same as the 0th element of the given
    list.
    '''
    
    output = copy.deepcopy(input)
    pad_list = None

    if input is None:
        return None
    
    if add_length < 1:
        return input

    if len(input[0]) > 0:
        # In case the caller is trying to pad the list with objects.
        if isinstance(pad_value, object):
            pad_list = len(input[0]) * [copy.deepcopy(pad_value)]
        else: 
            pad_list = len(input[0]) * [pad_value]
    else:
        pad_list = []

    if top:
        for i in range(add_length):
            output.insert(0, pad_list)
    else:
        for i in range(add_length):
            output.append(pad_list)

    return output
