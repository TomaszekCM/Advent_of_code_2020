import unittest
import day11

class TestDay11(unittest.TestCase):
  def test_get_num_occupied_works1(self):
    board_str="LLL\nLLL\nLLL"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(0,0), 0)
    self.assertEqual(board.NumOccupiedNeighbours(1,1), 0)
    self.assertEqual(board.NumOccupiedNeighbours(2,2), 0)


  def test_get_num_occupied_works2(self):
    board_str="LLL\nL#L\nLLL"
    board = day11.Board.CreateFromString(board_str)
    self.assertEqual(board.NumOccupiedNeighbours(0,0), 1)
    self.assertEqual(board.NumOccupiedNeighbours(1,1), 0)
    self.assertEqual(board.NumOccupiedNeighbours(2,2), 1)


  def test_get_next_board_works_small1(self):
    input_str = "LLL\nL.L\nLLL"
    expected_next_board_str = "###\n#.#\n###"

    board = day11.Board.CreateFromString(input_str)
    expected_next_board = day11.Board.CreateFromString(expected_next_board_str)

    next_board = board.GetNextBoard()
    self.assertTrue(next_board.Equals(expected_next_board))

  def test_equals_works(self):
    board1 = day11.Board.CreateFromString( "LLL\nL.L\nLLL")
    board2 = day11.Board.CreateFromString("###\n#.#\n###")
    board3 = day11.Board.CreateFromString("###\n#.#\n###\n###")
    board4 = day11.Board.CreateFromString( "LLL\nL.L\nLLL")

    self.assertFalse(board1.Equals(board2))
    self.assertTrue(board1.Equals(board1))
    self.assertTrue(board1.Equals(board4))
    self.assertTrue(board2.Equals(board2))
    self.assertFalse(board2.Equals(board3))


  def test_get_next_board_works_from_website(self):
    input_str = """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""
    board = day11.Board.CreateFromString(input_str)
    next_board = board.GetNextBoard()

    expected_next_board_str = """#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"""
    expected_next_board = day11.Board.CreateFromString(expected_next_board_str)
    self.assertTrue(next_board.Equals(expected_next_board))

  def test_from_website(self):
    input_str = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    board = day11.Board.CreateFromString(input_str)
    stable_board = day11.FindStableBoard(board)

    expected_final_board_str = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""
    expected_board = day11.Board.CreateFromString(expected_final_board_str)
    self.assertTrue(stable_board.Equals(expected_board))

if __name__ == '__main__':
    unittest.main()
