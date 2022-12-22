import copy

from util.util import print_progress_bar

LEFT_RIGHT = 0
RIGHT_LEFT = 1
TOP_BOTTOM = 2
BOTTOM_TOP = 3

def solve(in_list):
    ansA = None
    ansB = None

    data = normalize_input(in_list)

    ansA = partA(data)
    ansB = partB(data)
    return ansA, ansB

def partA(tree_img):
    ret = 0

    for i in range(len(tree_img)):
        print_progress_bar(i, len(tree_img))

        for j in range(len(tree_img[i])):
            if edge_of_image(tree_img, i, j):
                ret += 1
            elif check_view(tree_img, LEFT_RIGHT, i, j):
                ret += 1
            elif check_view(tree_img, RIGHT_LEFT, i, j):
                ret += 1
            elif check_view(tree_img, TOP_BOTTOM, i, j):
                ret += 1
            elif check_view(tree_img, BOTTOM_TOP, i, j):
                ret += 1

    return ret


def partB(tree_img):
    ret = 0
    current_score = int()

    for i in range(len(tree_img)):
        util.print_progress_bar(i, len(tree_img))

        for j in range(len(tree_img[i])):

            if edge_of_image(tree_img, i, j):
                continue
            else:
                current_score = score_view(tree_img, LEFT_RIGHT, i, j)
                current_score *= score_view(tree_img, RIGHT_LEFT, i, j)
                current_score *= score_view(tree_img, TOP_BOTTOM, i, j)
                current_score *= score_view(tree_img, BOTTOM_TOP, i, j)

            ret = max(ret, current_score)

    return ret

def normalize_input(input):
    ret = []

    for i in range(len(input)):
        # Make a new list-array row.
        ret.append([])

        for j in range(len(input[i])):
            # Add all the numbers to the current row.
            ret[i].append(int(input[i][j]))

    return ret

def edge_of_image(image: list, i: int, j: int):

    # Top or bottom row.
    if i == 0 or i == (len(image)- 1):
        return True

    # Far left or far right column.
    if j ==0 or j == (len(image)- 1):
        return True

    return False

def check_view(tree_img: list, direction: int, i: int, j: int) -> bool:
    tree_visible = True
    check_row = None
    max_i = len(tree_img)
    max_j = len(tree_img[0])

    # Figure out what direction we're looking from, and transform that
    # direction into a simple 1D row.

    # Transform L -> R
    if direction == 0:
        check_row = copy.deepcopy(tree_img[i])
        check_row = check_row[j:max_j]

    # Transform R -> L
    elif direction == 1:
        check_row = copy.deepcopy(tree_img[i])
        check_row = check_row[0:j+1]
        check_row.reverse()

    # Transform T -> B
    elif direction == 2:
        check_row = cut_column(tree_img, j)
        check_row = check_row[i:max_i]

    # Transform B -> T
    elif direction == 3:
        check_row = cut_column(tree_img, j)
        check_row = check_row[0:i+1]
        check_row.reverse()

    # Need to compare the 0the element to everything that is not itself.
    check_range = range(1, len(check_row), 1)

    for i in check_range:
        if check_row[0] <= check_row[i]:
            # Break on any trees blocking the view.
            tree_visible = False
            break

    return tree_visible

def score_view(tree_img: list, direction: int, i: int, j: int) -> int:
    score = int()
    check_row = None
    max_i = len(tree_img)
    max_j = len(tree_img[0])

    # Figure out what direction we're looking from, and transform that
    # direction into a simple 1D row.

    # Transform L -> R
    if direction == 0:
        check_row = copy.deepcopy(tree_img[i])
        check_row = check_row[j:max_j]

    # Transform R -> L
    elif direction == 1:
        check_row = copy.deepcopy(tree_img[i])
        check_row = check_row[0:j+1]
        check_row.reverse()

    # Transform T -> B
    elif direction == 2:
        check_row = cut_column(tree_img, j)
        check_row = check_row[i:max_i]

    # Transform B -> T
    elif direction == 3:
        check_row = cut_column(tree_img, j)
        check_row = check_row[0:i+1]
        check_row.reverse()

    # Need to compare the 0the element to everything that is not itself.
    check_range = range(1, len(check_row), 1)

    for i in check_range:
        if check_row[0] > check_row[i]:
            score += 1
        else:
            score += 1
            break

    return score

def cut_column(two_dim_list: list, col_index: int) -> list:
    transformed_col = []
    tmp_image = copy.deepcopy(two_dim_list)

    for row in tmp_image:
        transformed_col.append(row[col_index])

    return transformed_col



