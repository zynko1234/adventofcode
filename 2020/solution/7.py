import re
import constants

CRIT_CONTAINER = re.compile(r'^[a-z]*\s[a-z]*\sbags\scontain')
CRIT_CONTENTS = re.compile(r'([0-9]{1})(\s[a-z]*\s[a-z]*\sbags?)')
CRIT_EMPTY = re.compile(r'no other bags')

TEST_CASE_A = 'shiny gold'


def solve(in_list):
    dig_list = digest_input(in_list)

    ansA = count_containers(dig_list, TEST_CASE_A)
    ansB = count_inner_bags(dig_list, TEST_CASE_A)

    return ansA, ansB

def digest_input(in_list):
    dig_output = []

    for entity in in_list:
        # Normalize the containing bag.
        matches = re.search(CRIT_CONTAINER, entity)
        tmp_container = matches.group(0)
        tmp_container = tmp_container.replace(' bags contain', constants.EMPTY_STRING)

        # Normalize contents (if they exist), empty bag otherwise.
        tmp_contents_list = []
        tmp_find_list = re.findall(CRIT_CONTENTS, entity)
        
        if len(tmp_find_list) > 0:
            for inner_bag in tmp_find_list:
                tmp_str = inner_bag[1].replace(' bags', constants.EMPTY_STRING)
                tmp_str = tmp_str.replace(' bag', constants.EMPTY_STRING)
                tmp_str = tmp_str[1:]
                tmp_contents_list.append((inner_bag[0], tmp_str))
        else:
            tmp_find_list = None

        dig_output.append((tmp_container, tmp_contents_list))

    return dig_output

def count_containers(in_list: list, child_bag: str):
    count = 0

    for entity in in_list:
        if contains_child(in_list, entity[0], child_bag):
            count += 1

    return count

def contains_child(in_list: list, parent_bag: str, child_bag: str):
    validity = False
    parent_index = int()

    for i in range(len(in_list)):
        if in_list[i][0] == parent_bag:
            parent_index = i
            break

    # If there is no inner bag list then this is skipped.
    for entity in in_list[parent_index][1]:
        if entity[1] == child_bag:
            validity = True
        else:
            validity = validity | contains_child(in_list, entity[1], child_bag)

    return validity

def count_inner_bags(in_list: list, parent_bag: str):
    out_bag_count = 0
    parent_index = 0

    for i in range(len(in_list)):
        if in_list[i][0] == parent_bag:
            parent_index = i
            break
    
    for entity in in_list[parent_index][1]:
        tmp_bag_count = int(entity[0])
        out_bag_count += tmp_bag_count + (tmp_bag_count * count_inner_bags(in_list, entity[1]))
    
    return out_bag_count
