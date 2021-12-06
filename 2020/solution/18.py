import constants
import util

def solve(in_list):

    dig_list = digest_input(in_list)
    no_prec_answers = no_precedent_solve(dig_list)
    ansA = util.sum_list(no_prec_answers)
    ansB = 0

    return ansA, ansB

def digest_input(in_list: list):
    out_list = []

    for entry in in_list:
        tmp = digest_expr(entry)
        out_list.append(tmp[0])

    return out_list

def digest_expr(in_string: str, in_iter = -1):
    out_list = []
    
    i = (in_iter + 1)

    while i < len(in_string):
        
        if str(in_string[i]).isalnum() or in_string[i] == '+' or in_string[i] == '*':
            out_list.append(in_string[i])
            i += 1
        elif in_string[i] == constants.SPACE:
            i += 1
            continue
        elif in_string[i] == '(':
            # Recurse for the inner parenthesis.
            tmp_list, i = digest_expr(in_string, i)
            out_list.append(tmp_list)
            i += 1
        elif in_string[i] == ')':
            i += 1
            break
        # i++

    return out_list, i

def no_precedent_solve(in_list):
    out_list = []

    for i in range(len(in_list)):
        out_list.append(resolve_espression(in_list[i]))

    return out_list

def resolve_espression(in_list: list):
    answer = None
    tmp_oper = None
    tmp_num = None

    for entity in in_list:
        if type(entity) is list:
            tmp_num = resolve_espression(entity)
        elif str(entity).isdecimal():
            tmp_num = int(entity) 
        else:
            tmp_oper = entity

        if (answer is not None) and (tmp_num is not None) and (tmp_oper is not None):
            if tmp_oper == "*":
                answer *= tmp_num
            if tmp_oper == "+":
                answer += tmp_num
            
            # Reset the operator after arithmatic
            tmp_oper = None
            tmp_num = None

        elif answer is None:
            answer = tmp_num
            tmp_num = None
    
    return answer

