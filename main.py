import sys
import os

# Change these to toggle puzzle inputs and solutions.
YEAR = 2021
PUZZLE_NUM = 13

# Format strings.
PUZZLE_FILE = '{0}/solution'.format(YEAR)
ANS_FMT = 'Answer to {0}\'s puzzle {1} part {2} is {3}'

# Manually adds the submodules for the selected puzzle.
sys.path.append(os.path.abspath('./{0}'.format(PUZZLE_FILE)))

def main():
    util = __import__('util')
    curr_puzzle = __import__(str(PUZZLE_NUM), fromlist=['solve'])

    input_list = util.read_file('{0}/input/{1}'.format(YEAR, str(PUZZLE_NUM)))
    answerA, answerB = curr_puzzle.solve(input_list)

    print(ANS_FMT.format(YEAR, PUZZLE_NUM, 'A', answerA))
    print(ANS_FMT.format(YEAR, PUZZLE_NUM, 'B', answerB))

if __name__ == '__main__':
    main()
