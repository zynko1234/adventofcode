import copy
import time

from util import print_progress_bar
from div import is_divisible

class Monkey(object):
    def __init__(self) -> None:
        self.items = []
        self.operation  = ()
        self.test = 0
        self.true_path = 0
        self.false_path = 0
        self.inspect_count = 0

def solve(in_list):
    ansA = None
    ansB = None

    monkeys = normalize_input(in_list)

    #ansA = partA(monkeys)
    ansB = partB(monkeys)
    return ansA, ansB

def partA(monkeys: Monkey):
    CYCLES_A = 20

    ret = 0
    mod_monkeys = copy.deepcopy(monkeys)

    for i in range(CYCLES_A):
        for monkey in mod_monkeys:
            for item in monkey.items:
                mod_item = int(item)

                if monkey.operation[1] == 'old':
                    value = int(mod_item)
                else:
                    value = int(monkey.operation[1])

                if monkey.operation[0] == '*':
                    mod_item *= value
                elif monkey.operation[0] == '+':
                    mod_item += value

                mod_item = int(mod_item / 3)

                if (mod_item % monkey.test) == 0:
                    mod_monkeys[monkey.true_path].items.append(mod_item)
                else:
                    mod_monkeys[monkey.false_path].items.append(mod_item)

                monkey.inspect_count += 1

            # Flush the list of items held by this monkey after processing.
            monkey.items = []

    top_monkeys = []

    for i in range(2):
        curr_max = Monkey()

        for monkey in mod_monkeys:
            if curr_max.inspect_count < monkey.inspect_count:
                curr_max = monkey

        # When the top inspecting monkey is found, remove them from the list.
        top_monkeys.append(curr_max)
        mod_monkeys.remove(curr_max)

    ret = 1

    for monkey in top_monkeys:
        ret *= monkey.inspect_count

    return ret

def partB(monkeys):
    CYCLES_B = 1000

    ret = 0
    mod_monkeys = copy.deepcopy(monkeys)

    for i in range(CYCLES_B):
        print(f'Current cycle: {i}')
        for monkey in mod_monkeys:
            for item in monkey.items:
                mod_item = int(item)

                if monkey.operation[1] == 'old':
                    value = int(mod_item)
                else:
                    value = int(monkey.operation[1])

                if monkey.operation[0] == '*':
                    mod_item *= value
                elif monkey.operation[0] == '+':
                    mod_item += value

                # if is_divisible(mod_item, 10):
                #     mod_item = mod_item // 10
                time_start = time.time()
                if is_divisible(mod_item, monkey.test):
                    mod_monkeys[monkey.true_path].items.append(mod_item)
                else:
                    mod_monkeys[monkey.false_path].items.append(mod_item)
                elapsed = time.time()
                digit_count = len(str(mod_item))
                time_per_digit = elapsed / digit_count
                print(f'Divided {monkey.test} with time/digit of {time_per_digit} at {digit_count} digits')

                monkey.inspect_count += 1

            # Flush the list of items held by this monkey after processing.
            monkey.items = []

    top_monkeys = []

    for i in range(2):
        curr_max = Monkey()

        for monkey in mod_monkeys:
            if curr_max.inspect_count < monkey.inspect_count:
                curr_max = monkey

        # When the top inspecting monkey is found, remove them from the list.
        top_monkeys.append(curr_max)
        mod_monkeys.remove(curr_max)

    ret = 1

    for monkey in top_monkeys:
        ret *= monkey.inspect_count
    return ret

def normalize_input(input):
    ret = []

    for line in input:
        if 'Monkey' in line:
            ret.insert(0, Monkey())

        if 'Starting' in line:
            items = line.split()[2:]
            ret[0].items = [int(item.replace(',', '')) for item in items]

        elif 'Operation' in line:
            operation = line.split()[4:]
            operation[1] = operation[1]
            ret[0].operation = (operation[0], operation[1])

        elif 'Test' in line:
            test = line.split()[3:][0]
            test = int(test)
            ret[0].test = test

        elif 'true' in line:
            ret[0].true_path = int(line.split()[5])

        elif 'false' in line:
            ret[0].false_path = int(line.split()[5])

    ret.reverse()

    return ret
