import sys
import os

# Change these to toggle puzzle inputs and solutions.
YEAR = 2022
PUZZLE_NUM = 5

# Format strings.
PUZZLE_FILE = '{0}/solution'.format(YEAR)
ANS_FMT = 'Answer to {0}\'s puzzle {1} part {2} is {3}'

# Manually adds the submodules for the selected puzzle.
sys.path.append(os.path.abspath('./{0}'.format(PUZZLE_FILE)))

def main():
    util = __import__('util')

    solution_module = f'year_{YEAR}.solution.solution_{PUZZLE_NUM}'
    current_solution = __import__(solution_module, fromlist=solution_module)

    input_list = util.read_file('{0}/input/{1}'.format('year_' + str(YEAR), str(PUZZLE_NUM)) + '.txt')
    answerA, answerB = current_solution.solve(input_list)

    print(ANS_FMT.format(YEAR, PUZZLE_NUM, 'A', answerA))
    print(ANS_FMT.format(YEAR, PUZZLE_NUM, 'B', answerB))

if __name__ == '__main__':
    main()
