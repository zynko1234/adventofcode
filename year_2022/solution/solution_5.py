from re import L

def solve(in_list):
    ansA = None
    ansB = None

    normalized_input = normalize_input(in_list)

    # ansA = (normalized_input)
    # ansB = (normalized_input)
    return ansA, ansB

def normalize_input(input):
    stacks = []
    space_counter = 0
    switch_domain = False
    stack_domain = []
    instruction_domain = []
    
    # Split up the sections of input to be normalized by two different processes.
    for line in input:
        # Split on the empty string.
        if line == '':
            switch_domain = True
            continue
        
        if switch_domain is False:
            stack_domain.append(line)
        else:
            instruction_domain.append(line)    
        
    # Normalize the input stacks.
    for line in stack_domain:
        for glyph in line:
            if glyph == ' ':
                space_counter += 1
            
            # If it's a letter, add it to the appropriate stack dictated by the number of spaces.
            elif glyph.isalpha():
                
                if len(stacks) < (space_counter + 1):
                    diff = (space_counter + 1) - len(stacks)
                    
                    for i in range(diff):
                        temp = []
                        stacks.append(temp.copy())
                        
                stacks[space_counter].append(glyph)

    # Normalize the input instructions.
                
                
        
            