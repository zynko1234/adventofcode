# Allows classes to be self-referential in type hints. This must occur at the
# beginning of the file.
from __future__ import annotations

def solve(in_list):
    ansA = None
    ansB = None

    instructions = normalize_input(in_list)

    ansA = partA(instructions)
    ansB = partB(instructions)
    return ansA, ansB

def partA(instructions):
    ret = 0
    map = RopeMap(1)

    map.digest_instructions(instructions)

    ret = map.get_tail_cell_count()

    return ret

def partB(instructions):
    ret = 0
    map = RopeMap(9)

    map.digest_instructions(instructions)

    ret = map.get_tail_cell_count()
    return ret

def normalize_input(input):
    ret = []

    for line in input:
        direction = line.split()[0]
        magnitude = int(line.split()[1])
        ret.append((direction, magnitude))
    return ret


class RopeMap(object):
    def __init__(self, tail_count: int):
        self.map = []
        self.map.append([])

        # Tail starts at the origin so it's marked as such.
        self.map[0].append('#')

        self.head = {'x': 0, 'y': 0}
        self.tails = []

        for i in range(tail_count):
            self.tails.append({'x': 0, 'y': 0})


    def digest_instructions(self, instructions: list):
        for move in instructions:
            self.move_head(move[0], move[1])


    def increase_width(self, difference: int, right: bool):
        for row in self.map:
            for i in range(difference):
                # Are we adding this column to the left or the right.
                if right:
                    row.append('-')
                else:
                    row.insert(0, '-')

    def increase_height(self, difference: int, bottom: bool):
        present_width = len(self.map[0])
        for i in range(difference):
            tmp = []
            for j in range(present_width):
                tmp.append('-')

            # Are we adding this row to the top or bottom.
            if bottom:
                self.map.append(tmp)
            else:
                self.map.insert(0, tmp)


    def move_head(self, direction: str, length: int):
        max_y_index = len(self.map) - 1
        max_x_index = len(self.map[0]) - 1
        diff = 0
        final_tail = False

        if direction == 'R':
            dest = self.head['x'] + length

            if max_x_index < dest:
                diff = dest - max_x_index
                self.increase_width(dest - max_x_index, True)

            for i in range(length):
                self.head['x'] += 1

                # Special case to move the first tale behind the head.
                self.move_tail(self.head, self.tails[0], (len(self.tails) == 1))

                for i in range(len(self.tails) - 1):
                    if i == (len(self.tails) - 2):
                        final_tail = True

                    self.move_tail(self.tails[i], self.tails[i + 1], final_tail)

                final_tail = False

        elif direction == 'L':
            dest = self.head['x'] - length

            if dest < 0:
                diff = abs(dest)
                self.increase_width(diff, False)
                # Update the right-shifted places of the head and tails.
                self.head['x'] += diff

                for tail in self.tails:
                    tail['x'] += diff

            for i in range(length):
                self.head['x'] -= 1

                # Special case to move the first tale behind the head.
                self.move_tail(self.head, self.tails[0], (len(self.tails) == 1))

                for i in range(len(self.tails) - 1):
                    if i == (len(self.tails) - 2):
                        final_tail = True

                    self.move_tail(self.tails[i], self.tails[i + 1], final_tail)

                final_tail = False

        elif direction == 'D':
            dest = self.head['y'] + length

            if max_y_index < dest:
                diff = dest - max_y_index
                self.increase_height(dest - max_y_index, True)

            for i in range(length):
                self.head['y'] += 1

                # Special case to move the first tale behind the head.
                self.move_tail(self.head, self.tails[0], (len(self.tails) == 1))

                for i in range(len(self.tails) - 1):
                    if i == (len(self.tails) - 2):
                        final_tail = True

                    self.move_tail(self.tails[i], self.tails[i + 1], final_tail)

                final_tail = False

        elif direction == 'U':
            dest = self.head['y'] - length

            if dest < 0:
                diff = abs(dest)
                self.increase_height(diff, False)

                # Update the top-shifted places of the head and tails.
                self.head['y'] += diff

                for tail in self.tails:
                    tail['y'] += diff

            for i in range(length):
                self.head['y'] -= 1

                # Special case to move the first tale behind the head.
                self.move_tail(self.head, self.tails[0], (len(self.tails) == 1))

                for i in range(len(self.tails) - 1):
                    if i == (len(self.tails) - 2):
                        final_tail = True

                    self.move_tail(self.tails[i], self.tails[i + 1], final_tail)

                final_tail = False

    def move_tail(self, master, slave, final_tail):
        xdiff = master['x'] - slave['x']
        ydiff = master['y'] - slave['y']

        # Check for a diagonal movement if the head and tail are sharing neither
        # a column or a row.
        if self.must_move_diagonal(master, slave, xdiff, ydiff):
            if final_tail:
                self.map[slave['y']][slave['x']] = '#'
            slave['x'] += int((1 * (xdiff / abs(xdiff))))
            slave['y'] += int((1 * (ydiff / abs(ydiff))))

        elif abs(xdiff) > 1:
            if final_tail:
                self.map[slave['y']][slave['x']] = '#'
            slave['x'] += int((1 * (xdiff / abs(xdiff))))

        elif abs(ydiff) > 1:
            if final_tail:
                self.map[slave['y']][slave['x']] = '#'
            slave['y'] += int((1 * (ydiff / abs(ydiff))))

        # No change to this tail relative to the one in front of it.
        else:
            return

        # Mark the new location of the last tail.
        if final_tail:
            self.map[slave['y']][slave['x']] = 'T'

    def must_move_diagonal(self, master, slave, xdiff, ydiff):
        validity = slave['x'] != master['x']
        validity &= slave['y'] != master['y']
        validity &= abs(xdiff) > 1 or abs(ydiff) > 1

        return validity

    def get_tail_cell_count(self):
        count = 0

        for row in self.map:
            for cell in row:
                if cell == '#' or cell == 'T':
                    count += 1

        return count
