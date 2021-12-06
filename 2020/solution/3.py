TREE_GLYPH = '#'

def solve(in_list):
    ansA = 0
    ansB = 0

    ansA = calculateWithSlope(in_list, 3, 1)

    ansB = calculateWithSlope(in_list, 1, 1)
    ansB *= calculateWithSlope(in_list, 3, 1)
    ansB *= calculateWithSlope(in_list, 5, 1)
    ansB *= calculateWithSlope(in_list, 7, 1)
    ansB *= calculateWithSlope(in_list, 1, 2)

    return ansA, ansB

def calculateWithSlope(in_list, in_x_mov, in_y_mov):
    y_iter = 0
    x_iter = 0
    tree_count = 0
    x_width = len(in_list[0])


    while y_iter < len(in_list):
        if in_list[y_iter][x_iter] is TREE_GLYPH:
            tree_count += 1

        # Mod against the width of the slope to simulate an infinitely
        # duplicating width of paths and trees.
        x_iter = (x_iter + in_x_mov) % x_width
        y_iter = y_iter + in_y_mov

    return tree_count
