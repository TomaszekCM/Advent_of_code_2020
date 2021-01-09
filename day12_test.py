import unittest
from day12 import find_destination

class TestDay12(unittest.TestCase):
    def test_one(self):
        instructions = [["R",90],["R", 180],["R",180], ["F", 12], ["L", 270], ["F", 12]]
        self.assertEqual(find_destination(instructions), 24)
    def test_two(self):
        instructions = [["F", 10], ["L", 90], ["L", 90], ["L", 180], ["F", 10], ["L", 270], ["F", 14]]
        self.assertEqual(find_destination((instructions)), 14)

if __name__ == '__main__':
    unittest.main()