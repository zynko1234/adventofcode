import copy


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = calculate_power(normalized_input)
    ansB = calculate_life_support(normalized_input)
    return ansA, ansB

def normalize_input(in_input):
    output = []

    for entry in in_input:
        output.append(int(entry, 2))

    return output

def calculate_gamma_epsilon(input):

    zero_count = 12 * [0]
    one_count = 12 * [0]
    mask = 0b000000000001
    compound_byte = ""

    for entry in input:

        mask = 0b00001  

        for i in range(len(one_count)):
            if (mask & entry) > 0:
                one_count[i] += 1
            else:
                zero_count[i] += 1
            
            mask = mask << 1

    for i in range(len(zero_count)):
        if one_count[i] > zero_count[i]:
            compound_byte += '1'
        else:
            compound_byte += '0'

    gamma = binstr_to_unsigned_int(compound_byte) 
    epsilon = binstr_to_neg_unsigned_int(compound_byte) 
    return gamma, epsilon


def remove_data_from_list(input, position, value):
    output = []
    
    mask = 0b100000000000 >> position

    for entry in input:
        if (mask & entry) == value:
            output.append(entry)

    return output


def binstr_to_unsigned_int(str):
    output = 0

    for i in range(len(str)):
        if str[i] == '1':
            output += (2**i)

    return  output

def binstr_to_neg_unsigned_int(str):
    output = 0

    for i in range(len(str)):
        if str[i] == '0':
            output += (2**i)

    return  output

def calculate_power(input):
    gamma, epsilon = calculate_gamma_epsilon(input)
    return gamma * epsilon

def calculate_life_support(input):
    gamma, epsilon = calculate_gamma_epsilon(input)
    oxygen = 0
    c02 = 0
    mask = 0b100000000000
    #bin()

    temp_list = copy.deepcopy(input)

    for i in range(12):
        value = gamma >> (12-i)
        temp_list = remove_data_from_list(temp_list, i, value)

    oxygen = temp_list[0]

    return oxygen * c02


