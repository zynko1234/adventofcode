# Allows classes to be self-referential in type hints. This must occur at the
# beginning of the file.
from __future__ import annotations

import copy
import util

# Constants.
SIGNAL_CHECKS = [20, 60, 100, 140, 180, 220]
CRT_HEIGHT = 6
CRT_WIDTH = 40

def solve(in_list):
    ansA = None
    ansB = None

    instructions = normalize_input(in_list)

    ansA = partA(instructions)
    ansB = partB(instructions)
    return ansA, ansB

def partA(instructions):
    ret = 0

    # Reverse the input instructions so they may be treated as a stack.
    instruction_stack = copy.deepcopy(instructions)
    instruction_stack.reverse()
    cycle_counter = 0
    execution_stack = []
    simulated_variable = 1

    # Execute as long as there are still instructions currently processing or waiting to process.
    while len(instruction_stack) > 0 or len(execution_stack) > 0:
        cycle_counter += 1

        finished_instruction = None
        current_instruction = None

        # Pop the previously started instruction if there is one.
        if len(execution_stack) > 0:
            finished_instruction = execution_stack.pop()

        # Pop the next instruction if there is one and one is not currently executing.
        if len(instruction_stack) > 0 and finished_instruction is None:
            current_instruction = instruction_stack.pop()

        # Push the new instruction if it's not a NOOP.
        if current_instruction is not None:
            if current_instruction[0] != 0:
                execution_stack.append(current_instruction)

        # Compute the signal strength.
        if cycle_counter in SIGNAL_CHECKS:
            ret += simulated_variable * cycle_counter

        # Compute the any saved finished instruction at the end of the cycle.
        if finished_instruction is not None:
            simulated_variable += finished_instruction[1]

    return ret

def partB(instructions):
    ret = ''

    # Reverse the input instructions so they may be treated as a stack.
    instruction_stack = copy.deepcopy(instructions)
    instruction_stack.reverse()
    cycle_counter = 0
    execution_stack = []
    simulated_variable = 1

    # Create crt_map
    crt_map = []
    for i in range(CRT_HEIGHT):
        tmp = []

        for i in range(CRT_WIDTH):
            tmp.append(' ')

        crt_map.append(tmp)

    # Execute as long as there are still instructions currently processing or waiting to process.
    while len(instruction_stack) > 0 or len(execution_stack) > 0:
        # Use the non-updated cycle counter as the pixel index.
        sprite_pos = [simulated_variable -1, simulated_variable, simulated_variable + 1]

        if (cycle_counter % CRT_WIDTH) in sprite_pos:
            row = int(cycle_counter / CRT_WIDTH)
            index = cycle_counter % CRT_WIDTH
            crt_map[row][index] = '#'

        cycle_counter += 1

        finished_instruction = None
        current_instruction = None

        # Pop the previously started instruction if there is one.
        if len(execution_stack) > 0:
            finished_instruction = execution_stack.pop()

        # Pop the next instruction if there is one and one is not currently executing.
        if len(instruction_stack) > 0 and finished_instruction is None:
            current_instruction = instruction_stack.pop()

        # Push the new instruction if it's not a NOOP.
        if current_instruction is not None:
            if current_instruction[0] != 0:
                execution_stack.append(current_instruction)

        # Compute the any saved finished instruction at the end of the cycle.
        if finished_instruction is not None:
            simulated_variable += finished_instruction[1]

    # Stringify the map
    ret += '\n'
    for row in crt_map:
        for pixel in row:
            ret += pixel
            ret += ' '
        ret += '\n'

    # Remove the last newline
    ret = ret[:len(ret)]

    return ret

def normalize_input(input):
    ret = []

    for line in input:
        tmp = line.split()

        # Swith the strings with numbered codes and convert the given input terms to integers.
        if tmp[0] == 'noop':
            ret.append((0, None))
        else:
            ret.append((1, int(tmp[1])))

    return ret
