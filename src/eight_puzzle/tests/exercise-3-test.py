import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'src'))

from src.puzzle_game import PuzzleGame

import unittest

class ClasseTestesCommands(unittest.TestCase):
    def setUp(self):
        self.dimension = 3
        self.game = PuzzleGame(self.dimension)

    # Path 1
    def test_invalid_move_tile_non_adjacent_positions(self):
        self.assertFalse(self.game.move_tile(1))

    # Path 1
    def test_valid_move_tile(self):
        self.assertTrue(self.game.move_tile(8))

class ClasseTestesBranches(unittest.TestCase):
    def setUp(self):
        self.dimension = 3
        self.game = PuzzleGame(self.dimension)

    # Path 1
    def test_invalid_move_tile_outside_board(self):
        tile = 9
        self.game.dic_positions_of_tiles[tile] = (self.dimension, self.dimension+1)
        self.assertFalse(self.game.move_tile(tile))

    # Path 2
    def test_invalid_move_tile_non_adjacent_positions(self):
        self.assertFalse(self.game.move_tile(1))

    # Path 3
    def test_valid_move_tile(self):
        self.assertTrue(self.game.move_tile(8))

if __name__ == '__main__':
    unittest.main()
