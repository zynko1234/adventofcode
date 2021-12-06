import constants

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
