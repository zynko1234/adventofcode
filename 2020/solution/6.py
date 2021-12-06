import constants

def solve(in_list):
    dig_list = digest_input(in_list)

    union_list = union_answers(dig_list)
    filt_list = []
    for entry in union_list: filt_list.append(remove_dup(entry)) 
    ansA = count_answers(filt_list)

    intersect_list = intersect_answers(dig_list)
    ansB = count_answers(intersect_list)

    return ansA, ansB

def count_answers(in_list):
    count = 0
    
    for entity in in_list:
        count += len(entity)

    return count

def digest_input(in_list):
    out_list = []
    tmp_list = []

    for i in range(len(in_list)):
        if in_list[i] != constants.EMPTY_STRING:
            tmp_list.append(in_list[i])
        if in_list[i] == constants.EMPTY_STRING or (i + 1) == len(in_list):
            out_list.append(tmp_list)
            tmp_list = []
            
    return out_list

def remove_dup(in_str: str):
    out_string = str()

    for char in in_str:
        if char not in out_string:
            out_string += char

    return out_string

def union_answers(in_list):
    out_list = []
    tmp_string = constants.EMPTY_STRING

    for entry in in_list:
        for curr_string in entry:
            tmp_string += curr_string

        out_list.append(tmp_string)
        tmp_string = constants.EMPTY_STRING
    
    return out_list

def intersect_answers(in_list):
    out_list = []
    pidgeon_list = []
    tmp_string = constants.EMPTY_STRING

    for entity in in_list:
        pidgeon_list = [int()] * 128

        for i in range(len(entity)):
            for j in range(len(entity[i])):
                pidgeon_list[ord(entity[i][j])] += 1

        for i in range(len(pidgeon_list)):
            if pidgeon_list[i] == len(entity):
                tmp_string += chr(i)

        out_list.append(tmp_string)
        tmp_string = constants.EMPTY_STRING

    return out_list

def intersect_string(in_strA, in_strB):
    out_string = constants.EMPTY_STRING

    for char in in_strA:
        if char in in_strB and not char in out_string:
            out_string += char

    for char in in_strB:
        if char in in_strA and not char in out_string:
            out_string += char
    
    return out_string