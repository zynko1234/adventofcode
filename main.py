import sys
import os

# Change these to toggle puzzle inputs and solutions.
ADVENT_YEAR = 2022
PUZZLE_NUM = 9

# Format strings.
PUZZLE_FILE = '{0}/solution'.format(ADVENT_YEAR)
ANS_FMT = 'Answer to Puzzle #{0} part {1} is {2}'

# Manually adds the submodules for the selected puzzle.
sys.path.append(os.path.abspath('./{0}'.format(PUZZLE_FILE)))

def main():
    util = __import__('util')

    # Dynamically load the solution file.
    solution_module = f'year_{ADVENT_YEAR}.solution.solution_{PUZZLE_NUM}'
    current_solution = __import__(solution_module, fromlist=solution_module)
    input_list = util.read_file('{0}/input/{1}'.format('year_' + str(ADVENT_YEAR), str(PUZZLE_NUM)) + '.txt')
    
    print(f'Running Solution Set {PUZZLE_NUM} from Advent {ADVENT_YEAR}')
    answerA, answerB = current_solution.solve(input_list)
    print(ANS_FMT.format(PUZZLE_NUM, 'A', answerA))
    print(ANS_FMT.format(PUZZLE_NUM, 'B', answerB))

if __name__ == '__main__':
    main()
