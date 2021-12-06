PREAM_OFFSET = 25

def solve (in_list):
    # Solution for answer A
    digested_list = digest_input(in_list)
    validation_list = brute_check(digested_list, PREAM_OFFSET)
    ans_index = PREAM_OFFSET + validation_list.index(False)
    ansA = digested_list[ans_index]

    # Solution for answer B
    addA, addB = min_max_cont_sum(digested_list, ansA)
    ansB = addA + addB

    return ansA, ansB

def digest_input(in_list):
    out_list = []
    for i in range(len(in_list)):
        out_list.append(int(in_list[i]))

    return out_list

def brute_check(in_list, offset):
    check_index = offset
    validity_matrix = [False] * (len(in_list) - offset)

    for i in range(offset, len(in_list)):
        for j in range(check_index - offset, check_index):
            for k in range(check_index - offset, check_index): 
                    # Don't add things to themselves.
                    # Check addition.                 
                    if (j != k) and ((in_list[j] + in_list[k]) == in_list[i]):
                        validity_matrix[i - offset] = True
                        break
            if validity_matrix[i - offset] is True:
                break
        check_index += 1

    return validity_matrix

# Get the min and maximum of the first contiguous sum that adds up to
# sum_to_find from the values in in_list.
def min_max_cont_sum(in_list, sum_to_find):
    sum_found = False
    tmp_list = []

    for i in range(len(in_list)):
        tmp_list = []
        tmp_sum = 0

        for j in range(i, len(in_list)):
            tmp_list.append(in_list[j])
            tmp_sum += in_list[j]

            # Current contiguous sum added past the target sum. Break the inner
            # loop.
            if tmp_sum > sum_to_find:
                break
            elif tmp_sum == sum_to_find:
                sum_found = True
                break
        if sum_found:
            break

    return min(tmp_list), max(tmp_list)

# Add up all of the values in in_ist.
def sum_list(in_list):
    out_sum = 0

    for i in range(len(in_list)):
        out_sum += in_list[i]

    return out_sum
