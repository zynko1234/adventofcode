from typing import Mapping


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = calculate_pos(normalized_input)
    ansB = calculate_pos_waim(normalized_input)
    return ansA, ansB

def normalize_input(input):
    output = []
    split_input = []

    for entry in input:
        split_input.append(entry.split(' '))

    for entry in split_input:
        
        output.append({'dir': entry[0], 'mag': int(entry[1])})

    return output

def calculate_pos(input):
    xPos = 0
    yPos = 0

    for entry in input:
        magnitude = entry['mag']
        direction = entry['dir']
        
        if direction == 'forward':
            xPos += magnitude
        elif direction == 'down': 
            yPos += magnitude
        elif direction == 'up':
            yPos -= magnitude

    return (xPos * yPos)

def calculate_pos_waim(input):
    xPos = 0
    yPos = 0
    aim = 0

    for entry in input:
        magnitude = entry['mag']
        direction = entry['dir']
        
        if direction == 'forward':
            xPos += magnitude
            yPos += (magnitude * aim)
        elif direction == 'down': 
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude

    return (xPos * yPos)

