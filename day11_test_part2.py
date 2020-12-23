import unittest
import day11

class TestDay11(unittest.TestCase):
  def test_get_num_occupied_works1(self):
    board_str="LLL\nLLL\nLLL"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(0,0), 0, "Test polegl na:\n"+str(board))
    self.assertEqual(board.NumOccupiedNeighbours(1,1), 0, "Test polegl na:\n"+str(board))
    self.assertEqual(board.NumOccupiedNeighbours(2,2), 0, "Test polegl na:\n"+str(board))

  def test_get_num_occupied_works2(self):
    board_str="###\n###\n###"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(1,1), 8, "Test polegl na:\n"+str(board))

  def test_get_num_occupied_works3(self):
    board_str="#L#L#\n.....\n#...#\n.....\n#L#L#"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(2,2), 8, "Test polegl na:\n"+str(board))

  def test_get_num_occupied_works4(self):
    board_str="###\n#.#\n###"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(1,1), 8, "Test polegl na:\n"+str(board))
  def test_get_num_occupied_works5(self):
    board_str="#..#"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(2,0), 2, "Test polegl na:\n"+str(board))
  def test_get_num_occupied_works6(self):
    board_str = "L#.\n...\n..."
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(2, 2), 0, "Test polegl na:\n" + str(board))
  def test_get_num_occupied_works7(self):
    board_str = ".."
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(0, 0), 0, "Test polegl na:\n" + str(board))

if __name__ == '__main__':
    unittest.main()
