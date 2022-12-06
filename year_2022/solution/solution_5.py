import copy
from re import L

def solve(in_list):
    ansA = None
    ansB = None

    stacks, instructions = normalize_input(in_list)

    ansA = partA(stacks, instructions)
    ansB = partB(stacks, instructions)
    return ansA, ansB

def partA(stacks, instructions):
    ret = str()

    man_stacks = copy.deepcopy(stacks)

    for task in instructions:
        count = int(task[0])
        src =  int(task[1])
        dst = int(task[2])

        for i in range(count):
            # Minus one for index translation.
            tmp = man_stacks[src - 1].pop()
            man_stacks[dst - 1].append(tmp)

    # Get the top most crate on each stack.
    for stack in man_stacks:
        ret += stack.pop()

    return ret

def partB(stacks, instructions):
    ret = str()

    man_stacks = copy.deepcopy(stacks)

    for task in instructions:
        count = int(task[0])
        src =  int(task[1])
        dst = int(task[2])
        tmp = []

        # Pop the crates in the reverse order all at once.
        for i in range(count):
            # Minus one for index translation.
            tmp.append(man_stacks[src - 1].pop())

        # Reverse them back before adding them to their destination.
        tmp.reverse()

        for crate in tmp:
            man_stacks[dst - 1].append(crate)

    # Get the top most crate on each stack.
    for stack in man_stacks:
        ret += stack.pop()

    return ret


def normalize_input(input):
    # Return values for the stacked boxes and the instructions to move them.
    stacks = None
    instructions = None

    # Containers to partition the two different domains of input.
    stack_domain = []
    instruction_domain = []

    # Toggles what input is being copied over.
    domain_flag = False

    for line in input:
        # Split on the empty string. Toggle what we're copying.
        if line == '':
            domain_flag = True
            continue

        if domain_flag is False:
            tmp = ''
            modified_line = line[1:]
            # We only care about every 4th element.
            for i in range(len(modified_line)):
                if (i % 4) == 0:
                    tmp += modified_line[i]

            stack_domain.append(tmp)
        else:
            instruction_domain.append(line)

    stack_domain.reverse()
    slots_numbers = stack_domain[0].replace(' ', '')
    max = int(slots_numbers[len(slots_numbers)-1])

    # 2D lists have to be created this way.
    stacks = []
    for i in range(max):
        stacks.append(list())

    stack_domain = stack_domain[1:]

    # Normalize the input stacks.
    for line in stack_domain:
        for i in range(len(line)):
            if line[i] == ' ':
                continue
            else:
                stacks[i].append(line[i])

    instructions = []

    # Normalize the input instructions.
    for line in instruction_domain:
        tmp = ''
        tmp = line.replace('move ', '')
        tmp = tmp.replace(' from ', ',')
        tmp = tmp.replace(' to ', ',')
        instructions.append(tmp.split(','))

    return stacks, instructions



