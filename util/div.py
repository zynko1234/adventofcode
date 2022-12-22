import math

MIN_DIGIT_COUNT = 16

def __div_by_2(number: int) -> bool:
    # If the last digit is divisible by 2 then the whole nubmer is.
    str_num = str(number)[-1:]
    return (int(str_num, 10) % 2) == 0

def __div_by_3(number: int) -> bool:
    add_val = 0
    str_number = str(number)

    # If the sum of all digits is divisible by 3 then the whole number is.
    for value in str_number:
        add_val += int(value, 10)

    return (add_val % 3) == 0

def __div_by_4(number: int) -> bool:
    # If the last two digits are divisible by 4, then the whole number is.
    str_num = str(number)[-2:]
    return (int(str_num, 10) % 4) == 0

def __div_by_5(number: int) -> bool:
    # If the last digit is 0 or 5 then the whole number is divisible by 5.
    str_num = str(number)[-1:]
    return str_num == '0' or str_num == '5'

def __div_by_6(number: int) -> bool:
    # If divisible by 2 and 3 then the number is divisble by 6.
    return __div_by_2(number) and __div_by_3(number)

def __div_by_7(number: int) -> bool:
    sum = 0
    ce_index = 0
    coefficients = [1, 3, 2, 6, 4, 5]
    str_number = str(number)[::-1]

    # Take the digits of the number in reverse order, from right to left,
    # multiplying them successively by the digits 1, 3, 2, 6, 4, 5, repeating
    # with this sequence of multipliers as long as necessary. Add the products.
    # This sum has the same remainder mod 7 as the original number
    for glyph in str_number:
        sum += int(glyph, 10) * coefficients[ce_index]

        if ce_index != 5:
            ce_index += 1
        else:
            ce_index = 0

    return (sum % 7) == 0

def __div_by_8(number: int) -> bool:
    # If the last three digits are divisible by 8, then the whole number is.
    str_num = str(number)[-3:]
    return (int(str_num, 10) % 4) == 0

def __div_by_9(number: int) -> bool:
    add_val = 0
    str_number = str(number)

    # If the sum of all digits is divisible by 9 then the whole number is.
    for value in str_number:
        add_val += int(value, 10)

    return (add_val % 9) == 0

def __div_by_10(number: int) -> bool:
    # If the last digit is 0 then the whole number is divisible by 10.
    str_num = str(number)[-1]
    return str_num == '0'

def __div_by_11(number: int) -> bool:

    # Copy the given number before we manipulate it.
    candidate_num = number
    str_num = str(candidate_num)

    while len(str_num) > MIN_DIGIT_COUNT:
        # Take the alternating sum of the digits in the number, read from left to
        # right. If that is divisible by 11, so is the original number. Apply
        # this rule over and over again until we reach a more manageable number.
        sum = None
        add_flag = False

        for digit in str_num:
            if sum is not None:
                sum += int(digit, 10) if add_flag else (-1 * int(digit, 10))

                # Alternate between adding and subtracting.
                add_flag = not add_flag
            else:
                sum = int(digit)

        # Take the absolute value in case we have to operate on the result and its
        # length.
        str_num = str(abs(sum))

    candidate_num = sum

    return (candidate_num % 11) == 0

def __div_by_13(number: int) -> bool:
    str_num = str(number)

    # Multiply the last digit by 4. Add the resultant value to the remaining
    # numbers. This number will also be divisible by 13. Apply this rule over
    # and over again until we reach a more manageable number.
    while len(str_num) > MIN_DIGIT_COUNT:
        mod_digit = int(str_num[-1:], 10) * 4
        reduction_sum = int(str_num[:-1]) + mod_digit

        str_num = str(reduction_sum)

    return (int(str_num, 10) % 13) == 0

def __div_by_17(number: int) -> bool:
    str_num = str(number)

    # Multiply the last digit by 4. Add the resultant value to the remaining
    # numbers. This number will also be divisible by 17. Apply this rule over
    # and over again until we reach a more manageable number.
    while len(str_num) > MIN_DIGIT_COUNT:
        mod_digit = int(str_num[-1:], 10) * 5
        reduction_sum = int(str_num[:-1]) - mod_digit

        str_num = str(reduction_sum)

    return (int(str_num, 10) % 17) == 0

def __div_by_19(number: int) -> bool:
    str_num = str(number)

    # Multiply the last two digits by 4. Add the resultant value to the
    # remaining numbers. This number will also be divisible by 19. Apply this
    # rule over and over again until we reach a more manageable number.
    while len(str_num) > MIN_DIGIT_COUNT:
        mod_digit = int(str_num[-2:], 10) * 4
        reduction_sum = int(str_num[:-2]) + mod_digit

        str_num = str(reduction_sum)

    return (int(str_num, 10) % 19) == 0

def get_factors(number: int):
    ret = set()

    factor_limit = 1 + int(abs(number) / 2)

    for i in range(1, factor_limit, 1):
        if (number % i ) == 0:
            ret.add(i)

    return ret


def is_divisible(number: int, factor: int) -> bool:

    rules = {
        1: True,
        2: __div_by_2,
        3: __div_by_3,
        3: __div_by_4,
        5: __div_by_5,
        6: __div_by_6,
        7: __div_by_7,
        8: __div_by_8,
        9: __div_by_9,
        10: __div_by_10,
        11: __div_by_11,
        13: __div_by_13,
        17: __div_by_17,
        19: __div_by_19,
    }

    # Check if the number is big enough to be worth the time.
    div_by_rule = len(str(number)) > MIN_DIGIT_COUNT and factor in rules.keys()

    if div_by_rule:
        result = rules[factor](number)
    else:
        result = (number % factor) == 0

    return result
