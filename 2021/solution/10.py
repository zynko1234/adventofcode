import copy
import constants
import util
import math 

BRACE = r'<>'
BRACKET = r'{}'
PARENS = r'()'
SQUARE = r'[]'


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = solutionA(normalized_input)
    ansB = solutionB(normalized_input)
    return ansA, ansB


def normalize_input(input):
    output = copy.deepcopy(input)

    return output


def solutionA(input):
    output = 0

    push_list = []

    for string in input:
        for char in string:

            if len(push_list) == 0:
                push_list.append(char)

            elif is_left(char):
                push_list.append(char)

            else:
                pop_char = push_list.pop()

                if(not is_match(pop_char, char)):
                    # Error found. Calculate the points, and clear the checking list.
                    output += get_points(char, False)
                    push_list = []
                    break
                    
    return output

def solutionB(input):
    output = 0
    score = 0
    push_list = []
    score_tracker = []

    for string in input:
        for char in string:

            if len(push_list) == 0:
                push_list.append(char)

            elif is_left(char):
                push_list.append(char)

            else:
                pop_char = push_list.pop()

                if(not is_match(pop_char, char)):
                    push_list = []
                    break

        # Push list will only be populated if the inner loop was successful.
        if(len(push_list) > 0):
            for i in range(len(push_list)):
                # Calculate the scores backwards.
                tmp = push_list[(len(push_list) - 1) - i]
                score = (score * 5) + get_points(tmp, True)
            
            score_tracker.append(score)
            score = 0
            push_list = []

    # Sort all the collected scores, and return the median score.
    score_tracker.sort()
    index = int(math.ceil(len(score_tracker)/2)) - 1
    output = score_tracker[index]
    
    return output

def is_left(char):
    return ((char == BRACE[0]) or (char == BRACKET[0]) or (char == SQUARE[0]) or (char == PARENS[0]))


def is_match(charA, charB):
    match = False
    match_tup = [charA, charB]

    match |= (set(match_tup) == set(BRACE))
    match |= (set(match_tup) == set(BRACKET))
    match |= (set(match_tup) == set(SQUARE))
    match |= (set(match_tup) == set(PARENS))

    return match


def get_points(char, autocorrect):
    points = 0

    if autocorrect:
        if char == BRACE[0]:
            points += 4

        if char == BRACKET[0]:
            points += 3

        if char == SQUARE[0]:
            points += 2

        if char == PARENS[0]:
            points += 1
    else:
        if char == BRACE[1]:
            points += 25137

        if char == BRACKET[1]:
            points += 1197

        if char == SQUARE[1]:
            points += 57

        if char == PARENS[1]:
            points += 3

    return points




