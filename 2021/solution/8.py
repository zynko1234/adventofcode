import constants


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = solutionA(normalized_input)
    ansB = solutionB(normalized_input)
    return ansA, ansB


def normalize_input(input):
    output = []

    for entry in input:
        split = entry.replace(' | ', '|').split('|')
        codes = (split[0].split(constants.SPACE))
        unk_num_codes_unsorted = split[1].split(constants.SPACE)

        unk_nums_codes = []

        # Sort everything to make later matching easier.
        for num in unk_num_codes_unsorted:
            unk_nums_codes.append(''.join(sorted(num)))

        unk_wires = []
        tmp_wiring = None
        tmp_1 = str()
        tmp_4 = str()
        tmp_7 = str()
        tmp_8 = str()

        for code in codes:
            if Wiring.is_one(code):
                tmp_1 = ''.join(sorted(code))
            elif Wiring.is_four(code):
                tmp_4 = ''.join(sorted(code))
            elif Wiring.is_seven(code):
                tmp_7 = ''.join(sorted(code))
            elif Wiring.is_eight(code):
                tmp_8 = ''.join(sorted(code))
            else:
                unk_wires.append(''.join(sorted(code)))

        tmp_wiring = Wiring(tmp_1, tmp_4, tmp_7, tmp_8, unk_wires, unk_nums_codes)
        output.append(tmp_wiring)

    return output


def solutionA(input):
    output = 0

    for curr_wiring in input:
        output += Wiring.count_unique_display_nums(curr_wiring)

    return output


def solutionB(input):
    output = 0

    for curr_wiring in input:
            output += curr_wiring.solution

    return output


class Wiring(object):

    def __init__(self, one_seg, four_seg, seven_seg, eight_seg, unknown_segs, unknown_nums):

        # Segments known by unique count.
        self.one = one_seg
        self.four = four_seg
        self.seven = seven_seg
        self.eight = eight_seg

        # Not implicitly known.
        self.two = None
        self.three = None
        self.five = None
        self.six = None
        self.nine = None
        self.zero = None

        # Collection of initial non-implicitly known segments.
        self.unk_segs = unknown_segs

        # Unknown numbers to solve for.
        self.unk_num_codes = unknown_nums

        self.solution = 0

        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None
        self.g = None

        self.uniques = 0

        # Automatically deduce the letters and corresponding numbers.
        self.solve_for_all()

    def solve_for_all(self):

        ######## Solve for A

        setA = set(self.one)
        setB = set(self.seven)
        diff = list(setA.symmetric_difference(setB))
        self.a = diff[0]

        ######## Solve for G (derive 9)

        # Search for candidates for the 9.
        for segment in self.unk_segs:
            if len(segment) is 6:
                count = 0

                # Keep looping until you find a segment who contains all the segments of 4.
                for char in self.four:
                    if char not in segment:
                        break
                    else:
                        count += 1

                # When you find the that segment, see if it also contains whatever is mapped to 'a'.
                # If so then we've found 9. Break out.
                if (self.a in segment) and (count == 4):
                    self.nine = ''.join(sorted(segment))
                    self.unk_segs.remove(segment)
                    break

        composite_set = set(self.four + self.a)
        set9 = set(self.nine)
        diff = list(composite_set.symmetric_difference(set9))

        # 'g' is the summetric difference of (seg_4 + a) and seg_9
        self.g = diff[0]

        ######## Solve for E

        setA = set(self.nine)
        setB = set(self.eight)
        diff = list(setA.symmetric_difference(setB))

        self.e = diff[0]

        ######## Solve for D (get 0)

        # If the one segment config is a subset, and it's 6, we've found zero.
        for segment in self.unk_segs:
            if len(segment) is 6:
                if set(self.one).issubset(set(segment)):
                    self.zero = ''.join(sorted(segment))
                    self.unk_segs.remove(segment)
                    break

        # Disjuct union of 0 and 8 to find 'd'
        setA = set(self.eight)
        setB = set(self.zero)
        diff = list(setA.symmetric_difference(setB))

        self.d = diff[0]

        ######## Solve for C (derive 6)

        # Find the last 6 length segment set. It is guaranteed to be to be the number '6'.
        for segment in self.unk_segs:
            if len(segment) is 6:
                self.six = ''.join(sorted(segment))
                self.unk_segs.remove(self.six)
                break

        # Disjuct union of 6 and 8 to find 'c'
        setA = set(self.eight)
        setB = set(self.six)
        diff = list(setA.symmetric_difference(setB))

        self.c = diff[0]

        ######## Solve for F

        self.f = self.one.replace(self.c, constants.EMPTY_STRING)

        ######## Solve for B

        composite_set = set(self.one + self.d)
        set4 = set(self.four)
        diff = list(composite_set.symmetric_difference(set4))
        self.b = diff[0]

        ######## Derive 2, 3, and 5

        self.two = self.a + self.c + self.d + self.e + self.g
        self.two = ''.join(sorted(self.two))
        self.three = self.a + self.c + self.d + self.f + self.g
        self.three = ''.join(sorted(self.three))
        self.five = self.a + self.b + self.d + self.f + self.g
        self.five = ''.join(sorted(self.five))
        self.unk_segs = None

        ######## Solve the puzzle

        for num_code in self.unk_num_codes:
            if num_code == self.one:
                self.solution = (self.solution * 10) + 1
            if num_code == self.two:
                self.solution = (self.solution * 10) + 2
            if num_code == self.three:
                self.solution = (self.solution * 10) + 3
            if num_code == self.four:
                self.solution = (self.solution * 10) + 4
            if num_code == self.five:
                self.solution = (self.solution * 10) + 5
            if num_code == self.six:
                self.solution = (self.solution * 10) + 6
            if num_code == self.seven:
                self.solution = (self.solution * 10) + 7
            if num_code == self.eight:
                self.solution = (self.solution * 10) + 8
            if num_code == self.nine:
                self.solution = (self.solution * 10) + 9
            if num_code == self.zero:
                self.solution = (self.solution * 10) + 0

        unk_nums = None

    @staticmethod
    def is_one(code):
        return (len(code) == 2)

    @staticmethod
    def is_four(code):
        return (len(code) == 4)

    @staticmethod
    def is_seven(code):
        return (len(code) == 3)

    @staticmethod
    def is_eight(code):
        return (len(code) == 7)

    @staticmethod
    def is_unique_segment(code):
        return (Wiring.is_one(code) | Wiring.is_four(code) | Wiring.is_seven(code) | Wiring.is_eight(code))

    @staticmethod
    def count_unique_display_nums(in_wiring: 'Wiring'):
        count = 0

        for code in in_wiring.unk_num_codes:
            if Wiring.is_unique_segment(code):
                count += 1

        return count
