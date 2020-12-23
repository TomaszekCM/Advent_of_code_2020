# https://adventofcode.com/2020/day/11

class Board:
  """
  Represents a board with seats. Fields:
  .board: a list of lists (row by row) encoding the board. 
  .width   the width of the board (number of rows)
  .height  the height of the board (number of rows)
  """
  def __init__(self, board):
    """
    Creates a board from a list of lists representing a board.
    """
    self.board = board
    self.height = len(self.board)
    self.width = len(self.board[0])

  @staticmethod
  def CreateFromString(board_str):
    """
    Creates a board from a string representing a board (input to the problem)
    """
    board = [list(line) for line in board_str.split("\n")]        
    return Board(board)

  # Converts the board to string (can be used with print(board))
  def __str__(self):
    lines_str = []
    for line in self.board:
        lines_str.append("".join(line))
    return "\n".join(lines_str)

  # Returns the number of occupied neighbours of the given field.
  def NumOccupiedNeighbours(self, x, y):
    # print("\n\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\\n\nZaczynam uruchamiac dla parametrow: x=%i y=%i plansza:\n%s\n" % (x,y,self))
    seats_occupied = 0
    list_of_x = range(-1, 2)
    list_of_y = range(-1, 2)
    for row in list_of_y:
      for col in list_of_x:
        if col == 0 and row == 0:
          continue

        if x+col < 0 or x+col >= self.width:
          continue
        if y+ row < 0 or y+row >= self.height:
          continue
        x_copy = x
        y_copy = y
        while (y_copy+row) >= 0 and (y_copy+row) < self.height and (x_copy+col) >= 0 and (x_copy+col) < self.width and self.board[y_copy+row][x_copy+col] == ".":
          x_copy += col
          y_copy += row
        if (y_copy+row) >= 0 and (y_copy+row) < self.height and (x_copy+col) >= 0 and (x_copy+col) < self.width:
          if self.board[y_copy+row][x_copy+col] == "#":
            # print(y, x)
            seats_occupied += 1

    # print("Zwracam wynik: %i" % (seats_occupied, ))
    # print("----------------------------------------------")
    return seats_occupied
        

  # Returns a board after one round of resitting.
  def GetNextBoard(self):
    new_seatting_list = []
    for row in range(self.height):
      new_row = []
      for col in range(self.width):
        current_seat = self.board[row][col]
        if current_seat == "L":
          if self.NumOccupiedNeighbours(col, row) == 0:
            new_row.append("#")
          else:
            new_row.append(current_seat)
        elif current_seat == "#":
          if self.NumOccupiedNeighbours(col, row) >= 5:
            new_row.append("L")
          else:
            new_row.append(current_seat)
        else:
          new_row.append(current_seat)
      new_seatting_list.append(new_row)
    return Board(new_seatting_list)
    # raise Exception("Napisz tresc tej funkcji panie Tomek!")

  # Returns True if the other board is equal to the specified board
  # and False if the board is different.
  def Equals(self, other_board):
    if self.height != other_board.height or self.width != other_board.width:
      return False
    for row in range(self.height):
      for col in range(self.width):
        if self.board[row][col] != other_board.board[row][col]:
          return False
    return True

    # raise Exception("Napisz tresc tej funkcji panie Tomek!")

  # Returns the number of occupied fields.
  def GetNumOccupied(self):
    numb_of_occupied_seats = 0
    for row in range(self.height):
      for col in range(self.width):
        # print(self.board[row][col])
        if self.board[row][col] == "#":
          numb_of_occupied_seats += 1
    
    return numb_of_occupied_seats

    # raise Exception("Napisz tresc tej funkcji panie Tomek!")
  
def FindStableBoard(initial_board):
  board = initial_board
  while True:
    new_board = board.GetNextBoard()
    if new_board.Equals(board):
        return new_board
    board = new_board  

def ReadInputFromFile():
  with open("day11_input.txt") as f:
    return f.read()

# Ten warunek bedzie spelniony jesli wywolasz z linii polecen python day11.py
# Nie wywola sie jesli zrobisz import day11
if __name__ == "__main__":
  board = Board.CreateFromString(ReadInputFromFile())
  print("The size of the loaded board: width=%i height=%i" % (board.width, board.height))
  stable_board = FindStableBoard(board)
  print("The number of occupied seats in the final board: %i" % stable_board.GetNumOccupied(), )


