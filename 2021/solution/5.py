import constants
import util

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
      tmp = entry.replace(' -> ', ',')
      tmp = tmp.split(',')
      output.append(Cord(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])))

   return output


def solutionA(input):
   output = 0

   board = gen_board(input)

   for entry in input:
      if(entry.x1 == entry.x2):
         start = util.get_min(entry.y1, entry.y2)
         distance = abs(entry.y1 - entry.y2)

         for i in range (start, start + distance + 1):
            board[i][entry.x1] +=1

      elif(entry.y1 == entry.y2):
         start = util.get_min(entry.x1, entry.x2)
         distance = abs(entry.x1 - entry.x2)

         for j in range (start, distance + 1):
            board[entry.y1][j] +=1


   for row in board:
      for index in row:
         if index > 1:
            output += 1

   return output

def solutionB(input):
   output = 0

   return output

def gen_board(input):
   max_y = 0
   max_x = 0

   for entry in input:
      if entry.x1 > max_x:
         max_x = entry.x1
      
      if entry.x2 > max_x:
         max_x = entry.x2

      if entry.y1 > max_y:
         max_y = entry.y1
          
      if entry.y2 > max_y:
         max_y = entry.y2

   board = util.gen_2d_array_list(max_y + 1, max_x + 1)

   return board


class Cord(object):
   def __init__(self, x1, y1, x2, y2):
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2
