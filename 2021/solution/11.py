import constants
import util
import copy


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = solutionA(normalized_input, 100)
    ansB = solutionB(normalized_input)
    return ansA, ansB


def normalize_input(input):
    output = []

    for line in input:
        tmp_list = []

        for value in line:
            tmp_list.append(int(value))

        output.append(tmp_list)

    return output


def solutionA(input, iterations):
    output = 0
    octopi = copy.deepcopy(input)

    for i in range(iterations):
        flash_cords = []
        increment_octopi(octopi)

        # After the increment, check for 
        flash_cords = check_flash(octopi)

        while(len(flash_cords) > 0):
            for cord in flash_cords:
                flash_single_octopus(octopi, cord[0], cord[1])
            
            # Check again if more flashes occur.
            flash_cords = check_flash(octopi)
        output += count_flashes(octopi)

    return output

def solutionB(input):
    output = 0
    flash_count = 0
    octopi = copy.deepcopy(input)
    set_size = len(octopi) * len(octopi[0]) 

    # Spin until all of the octopi flash on the same step.
    while(flash_count != set_size):
        flash_cords = []
        increment_octopi(octopi)

        # After the increment, check for 
        flash_cords = check_flash(octopi)

        while(len(flash_cords) > 0):
            for cord in flash_cords:
                flash_single_octopus(octopi, cord[0], cord[1])
            
            # Check again if more flashes occur.
            flash_cords = check_flash(octopi)
        flash_count = count_flashes(octopi)

        # Track the steps. The last step number we run will be our output.
        output += 1

    return output

def increment_octopi(octopi):
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            octopi[i][j] += 1

    return

def check_flash(octopi):
    cordinates = []

    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if octopi[i][j] > 9:
                cordinates.append([i, j])

    return cordinates

def count_flashes(octopi):
    count = 0

    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if octopi[i][j] == 0:
                count += 1

    return count


def flash_single_octopus(octopi, i, j):
    north = False
    south = False 
    east = False
    west = False

    octopi[i][j] = 0

    # Increment N if available.
    if i > 0:
        north = True
        
        if octopi[i-1][j] != 0:
            octopi[i-1][j] += 1

    # Increment S if available.
    if i < (len(octopi) - 1) :
        south = True

        if octopi[i+1][j] != 0:
            octopi[i+1][j] += 1

   # Increment W if available.
    if j > 0:
        west = True

        if octopi[i][j-1] != 0:
            octopi[i][j-1] += 1

    # Incrment E if available.
    if j < (len(octopi[i]) - 1):
        east = True

        if octopi[i][j+1] != 0:
            octopi[i][j+1] += 1


    # Increment N and W
    if north and west:
        if octopi[i-1][j-1] != 0:
            octopi[i-1][j-1] += 1

    # Increment N and E
    if north and east:
        if octopi[i-1][j+1] != 0:
            octopi[i-1][j+1] += 1

    # Increment S and W
    if south and west:
        if octopi[i+1][j-1] != 0:
            octopi[i+1][j-1] += 1

    # Increment S and E
    if south and east:
        if octopi[i+1][j+1] != 0:
            octopi[i+1][j+1] += 1
    




    
