from copy import deepcopy
import os
import constants
import util


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    #ansA = solutionA(normalized_input)
    #ansB = solutionB(normalize_input)
    return ansA, ansB


def normalize_input(input):
    output = CodePaper()
    cords = []
    instructions = []
    mode = 0

    for line in input:
        if line is not constants.EMPTY_STRING:
            if mode == 0:
                x, y = line.split(constants.COMMA)
                cords.append([int(x),int(y)])
            else:
                temp = line.split(constants.SPACE)
                fold, degree = temp[2].split(constants.EQUALS)
                instructions.append([fold, int(degree)])
        else:
            mode = 1

    xlist, ylist = zip(*cords)
    max_x = util.get_max_of_list(xlist)
    max_y = util.get_max_of_list(ylist)
    hole_map = util.gen_2d_array_list(max_y + 1, max_x + 1)

    for cord in cords:
        hole_map[cord[1]][cord[0]] = 1

    output.holes = hole_map
    output.instructs = instructions
    return output


def solutionA(input:'CodePaper'):
    first_fold_count = 0
    message = "Check file under [./2021/solution/output_files/13.sol]"

    # This is the first part solution: Execute first fold instruction.
    input.transform_next_instruction()
    first_fold_count = input.count_marks()

    # This is the second part solution: Execute the rest of the instructions.
    while input.has_next_instruction() == True:
        input.transform_next_instruction()

    input.print_solution_to_file()

    return first_fold_count, message


def solutionB(input):
    output = 0

    return output

class CodePaper(object):
    def __init__(self) -> None:
        super().__init__()
        self.holes = []
        self.instructs = []

    def transform_next_instruction(self):
        fold_type, split = self.instructs[0]
        map_a = []
        map_b = []

        # Fold along a vertical line on the X axis.
        if fold_type == 'x':
            for i in range(len(self.holes)):
                map_a.append([])
                map_b.append([])

                for j in range(len(self.holes[i])):
                    # The fold line dissapears.
                    if j == split:
                        continue

                    if j < split:
                        map_a[i].append(self.holes[i][j])

                    else:
                        map_b[i].append(self.holes[i][j])

            pad_diff = abs(len(map_a[0]) - len(map_b[0]))

            if pad_diff > 0:
                # Pad whatever map is smaller.
                if len(map_a[0]) > len(map_b[0]):
                    for i in range(len(map_b)):
                        map_b[i] = util.pad_zero(map_b[i], pad_diff, False)
                else:
                    for i in range(len(map_a)):
                        map_a[i] = util.pad_zero(map_a[i], pad_diff, True)
            
            util.reverse_2d_list(map_b)

        # Fold along a horizontal line on the Y axis.
        else:
            for i in range(len(self.holes)):
                if i == split:
                    continue
                if i < split:
                    map_a.append(self.holes[i])
                else:
                    map_b.append(self.holes[i])

            pad_diff = abs(len(map_a) - len(map_b))

            if pad_diff > 0:
                # Pad whatever map is smaller.
                if len(map_a) > len(map_b):
                    map_b = util.pad_lines(map_b, pad_diff, False, 0)
                else:
                    map_a = util.pad_lines(map_a, pad_diff, True, 0)

            # A reverse() is all that's needed to invert of the horizontal Y line.
            map_b.reverse()

        self.holes = CodePaper.map_or(map_a, map_b)
        self.instructs.remove(self.instructs[0])
        return
                
    def map_or(map_a, map_b):
        output = []

        for i in range(len(map_a)):
            output.append([])

            for j in range(len(map_a[i])):
                tmp_or = map_a[i][j] | map_b[i][j]
                output[i].append((tmp_or))
        
        return output

    def has_next_instruction(self):
        return len(self.instructs) > 0

    def count_marks(self):
        output = 0

        for line in self.holes:
            for value in line:
                if value == 1:
                    output += 1

        return output

    def print_solution_to_file(self):
        dpath = '2021/solution/output_files/'
        fpath = dpath + '13.sol'
        
        if os.path.exists(dpath) is False:
            os.mkdir(dpath)

        string_map = self.gen_string_map()

        with open(fpath, 'w') as fw:
            fw.write(string_map)

    def gen_string_map(self):
        output = ""

        for i in range(len(self.holes)):
            for j in range(len(self.holes[i])):
                if self.holes[i][j] == 0:
                    output += '_'
                else:
                    output += '#'
            
            output += '\n'

        return output
