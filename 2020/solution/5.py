import util

# Binary magnitudes of the input.
ROW_MAGNITUDE = 7
COL_MAGNITUDE = 3


def solve(in_list):

    # Convert the string into proper binary.
    dig_list = digest_input(in_list)

    # Generate a list of ticket rows, columns, and IDs.
    data_list = convert_seat(dig_list, ROW_MAGNITUDE, COL_MAGNITUDE)

    # Get a list of just the ID's for answer A.
    id_list = util.split_list(data_list, 2)
    ansA = max(*id_list)

    ansB = find_missing_seat(data_list)
    return ansA, ansB


def digest_input(in_list):
    out_list = []

    for entity in in_list:
        tmp = str(entity)
        tmp = tmp.replace('B', '1').replace('F', '0')
        tmp = tmp.replace('R', '1').replace('L', '0')
        out_list.append(int(tmp, 2))

    return out_list


def convert_seat(in_list, row_deg, col_deg):
    out_ticket_data = []
    row_mask = int('0b0000000111', 2)
    row_val = 0
    col_val = 0

    for entity in in_list:
        row_val = int(entity >> col_deg)
        col_val = int(entity & row_mask)
        id = ((row_val * 8) + col_val)

        # Formula for the seat ID
        out_ticket_data.append((row_val, col_val, id))

    return out_ticket_data


def find_missing_seat(in_list):
    out_id = 0
    # Split out a list representing all the rows.
    row_list = util.split_list(in_list, 0)
    row_max = max(*row_list)
    viable_seats = []

    for entity in in_list:
        # If the row qualifies. Add the ID.
        if entity[0] > 0 and entity[0] < row_max:
            viable_seats.append(entity[2])

    viable_seats.sort()
    num_viable_seats = len(viable_seats)

    for i in range(num_viable_seats):
        if i < (num_viable_seats - 1):
            if viable_seats[i] != (viable_seats[i+1] - 1):
                # Index of interest found. It's one more than this seat's ID.
                out_id = viable_seats[i] + 1
    return out_id
