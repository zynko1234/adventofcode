import constants
import util
import copy


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = solutionA(normalized_input)
    ansB = solutionB(normalized_input)
    return ansA, ansB


def normalize_input(input):
    modified = copy.deepcopy(input)
    draw_nums = []
    tmp_str  = modified[0].split(',')
    modified = modified[2:]

    # To act as a delimiter for the last board to add.
    modified.append(constants.EMPTY_STRING)

    for char in tmp_str:
        draw_nums.append(int(char))

    # Use to amalgamate the board entries.
    tmp_line = []
    tmp_vals = []
    tmp_board = []
    boards = []

    for line in modified:
        if line == constants.EMPTY_STRING:
            boards.append(tmp_board)
            tmp_board = []
            continue

        line = line.replace('  ',  constants.SPACE)

        tmp_line = line.split(constants.SPACE)

        for value in tmp_line:
            if value != constants.EMPTY_STRING:
                tmp_vals.append(int(value))

        tmp_board.append(tmp_vals)
        tmp_vals = []
        tmp_line = []

    return Bingo(draw_nums, boards)


def solutionA(input):
    output = 0
    winner, last_called = input.find_first_winning_board()
    output = Bingo.calculate_score(winner, last_called)
    return output


def solutionB(input):
    output = 0
    winner, last_called = input.find_last_winning_board()
    output = Bingo.calculate_score(winner, last_called)
    return output


class Bingo(object):
    def __init__(self, draw_nums, boards):
        self.draw_nums = draw_nums
        self.boards = boards

    def find_first_winning_board(self):
        clone_nums = copy.deepcopy(self.draw_nums)
        clone_boards = copy.deepcopy(self.boards)

        for num in clone_nums:

            num = int(num)

            for board in clone_boards:
                # Keep calling numbers on the collections of boards. As soon as you find the winner
                # capture it and the current number and return out.
                self.call(board, num)

                if Bingo.check_board(board) is True:
                    return board, num

        return None, None

    def find_last_winning_board(self):
        clone_nums = copy.deepcopy(self.draw_nums)
        clone_boards = copy.deepcopy(self.boards)
        winning_indexes = []

        for num in clone_nums:

            for i in range(len(clone_boards)):

                self.call(clone_boards[i], num)
                
                if Bingo.check_board(clone_boards[i]) is True:
                    # This is pretty dirty, but this keeps the order of winners and removes
                    # duplicates when they're re added. The last index is the index of the winner
                    # board. Capture it and the current bingo number of the moment and return.
                    winning_indexes.append(i)
                    winning_indexes = util.remove_dupe(winning_indexes)

                    if(len(winning_indexes) == len(clone_boards)):
                        # Spin the list of recorded indexes around. The first one will be the last winner.
                        winning_indexes.reverse()
                        return clone_boards[winning_indexes[0]], num

        return None, None

    def call(self, board, num):
        for i in range(len(board)):
            for j in range(len(board[i])):

                # Break when you mark the called number. Should only be one on each bingo board if
                # any.
                if board[i][j] == num:
                    board[i][j] = -1
                    return

    @staticmethod
    def calculate_score(board, last_call):
        output = 0

        for line in board:
            for value in line:

                # Amalgamate all values that aren't -1
                if value != -1:
                    output += value

        output *= last_call

        return  output

    @staticmethod
    def check_board(board):
        found = bool()

        # Check rows.
        for line in board:
            found = True

            # Unmarked value found. Move to the next row.
            for value in line:
                if value != -1:
                    found = False
                    break

            # Made it to the end with the whole row marked, return out.
            if found is True:
                return found

        # If nothing is found in the rows, check the columns.
        for i in range(len(board)):
            found = True

            for j in range(len(board[0])):
                if board[j][i] != -1:
                    found = False
                    break

            if found is True:
                return found

        return found