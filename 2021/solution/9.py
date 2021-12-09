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
   temp_list = []

   for string in input:
      for char in string:
         temp_list.append(int(char))
      
      output.append(temp_list)
      temp_list = []

   return output


def solutionA(input):
   output = 0

   # Get the location of all the low points.
   lowest_points = map_lowpoints(input) 

   # Sum up all of the lowest points.            
   for point in lowest_points:
      output += 1 + input[point[0]][point[1]]   

   return output

def solutionB(input):
   output = 1
   low_points = []
   basin_sizes = []

   low_points = map_lowpoints(input)

   for point in low_points:
      tmp_basin = []
      flood_fill_basin(point, input, tmp_basin)
      tmp_basin = remove_duplicate_tuples(tmp_basin)
      basin_sizes.append(len(tmp_basin))

   top_three = find_max_three(basin_sizes)
   
   for entry in top_three:
      output *= entry

   return output

def remove_duplicate_tuples(input):
   prune_list = []

   for candidate in input:
      unique = True
      for entry  in prune_list:
         
         # Any match will prohibit appending to the output list
         if candidate == entry:
            unique = False
            break

      if unique:
         prune_list.append(candidate)

   return prune_list

def find_max_three(input):
   clone_list = input[:]
   
   if len(clone_list) <= 3:
      return clone_list

   output = []

   for i in range(3):
      curr_max = clone_list[0]

      for value in clone_list:
         if value > curr_max:
            curr_max = value
      
      clone_list.remove(curr_max)
      output.append(curr_max)

   return output

def flood_fill_basin(point, input, output):
   output.append(point)
   i = point[0]
   j = point[1]

   # See if we chan check the top for a higher point. 9's block flow.
   if (i > 0):
      if (input[i][j] < input[i-1][j]) and (input[i-1][j] != 9):
         flood_fill_basin([i-1, j], input, output)
         
   # See if we can check the bottom.
   if i < (len(input) - 1):
      if (input[i][j] < input[i+1][j]) and (input[i+1][j] != 9):
         flood_fill_basin([i+1, j], input, output)

   # See if we can check the left.
   if j > 0:
      if (input[i][j] < input[i][j-1]) and (input[i][j-1] != 9):
         flood_fill_basin([i, j-1], input, output)

   # See if we can check the right.
   if j < (len(input[i]) - 1):
      if (input[i][j] < input[i][j+1]) and (input[i][j+1] != 9):
         flood_fill_basin([i, j+1], input, output)

def map_lowpoints(input):
   lowest_points = []
   
   # Assume true until it isn't
   is_lowest_point = True

   for i in range(len(input)):
      for j in range(len(input[i])):
         # Reset the check
         is_lowest_point = True

         # See if the top can be greater-than checked.
         if i > 0:
            is_lowest_point &= (input[i][j] < input[i-1][j])

         # See if the bottom can be greater-than checked.
         if i < (len(input) - 1):
            is_lowest_point &= (input[i][j] < input[i+1][j])

         # See if the left can be greater-than checked.
         if j > 0:
            is_lowest_point &= (input[i][j] < input[i][j-1])

         # See if the right can be greater-than checked.
         if j < (len(input[i]) - 1):
            is_lowest_point &= (input[i][j] < input[i][j+1])

         if is_lowest_point is True:
            lowest_points.append([i,j])

   return lowest_points