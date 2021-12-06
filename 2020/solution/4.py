import constants
import re

CRITERIA_REGEX_A = [re.compile(r'.*ecl:.*'),
                    re.compile(r'.*pid:.*'),
                    re.compile(r'.*eyr:.*'),
                    re.compile(r'.*hcl:.*'),
                    re.compile(r'.*byr:.*'),
                    re.compile(r'.*iyr:.*'),
                    re.compile(r'.*hgt:.*')]

CRITERIA_REGEX_B = [ re.compile(r'.*byr:(19[2-8][0-9]|199[0-9]|200[0-2])(\s)+.*'),
                     re.compile(r'.*iyr:(201[0-9]|2020)(\s)+.*'),
                     re.compile(r'.*eyr:(202[0-9]|2030)(\s)+.*'),
                     re.compile(r'.*hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))(\s)+.*'),
                     re.compile(r'.*hcl:#([a-f0-9]){6}(\s)+.*'),
                     re.compile(r'.*ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s)+.*'),
                     re.compile(r'.*pid:[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9](\s)+.*')]


def solve(in_list):
    norm_list = normalize_input(in_list)
    ansA = parse_with_regex(norm_list, CRITERIA_REGEX_A)
    ansB = parse_with_regex(norm_list, CRITERIA_REGEX_B)
    return ansA, ansB


def normalize_input(in_input):
    out_list = []
    amalg_str = str()

    # List is tokenized with an empty line.
    # Amalgamate populated lines and add a space, enter into list.
    for entity in in_input:
        if entity is not constants.EMPTY_STRING:
            amalg_str = amalg_str + entity + constants.SPACE
        else:
            out_list.append(amalg_str)
            amalg_str = str()
            continue

    out_list.append(amalg_str)

    return out_list


def parse_with_regex(in_input, in_crit_regex):
    out_valid_input = 0
    valid = bool()

    # Iterate through each input and regex match against each criteria.
    # A single failure skips the input being counted.
    for entity in in_input:
        # Set/reset flag.
        valid = True

        for criteria in in_crit_regex:
            if criteria.match(entity) is None:
                valid = False
                break

        if valid:
            out_valid_input += 1

    return out_valid_input
