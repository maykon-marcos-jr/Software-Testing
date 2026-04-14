import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'conteudo'))

from conteudo.puzzle_game import PuzzleGame

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

    def test_assert_number_of_tiles_starts_with_1(self):
        tiles_1 = self.game.board.grid
        tiles  = []
        for i in tiles_1:
            tiles.extend(i)
        self.assertEqual(tiles[0], 1)

    def test_assert_number_of_tiles_has_2(self):
        tiles_1 = self.game.board.grid
        tiles  = []
        for i in tiles_1:
            tiles.extend(i)
        self.assertEqual(tiles[1], 2)

    def test_assert_number_of_tiles_has_3(self):
        tiles_1 = self.game.board.grid
        tiles  = []
        for i in tiles_1:
            tiles.extend(i)
        self.assertEqual(tiles[2], 3)

    def test_assert_number_of_tiles_has_4(self):
        tiles_1 = self.game.board.grid
        tiles  = []
        for i in tiles_1:
            tiles.extend(i)
        self.assertEqual(tiles[3], 4)

    def test_assert_number_of_tiles_has_5(self):
        tiles_1 = self.game.board.grid
        tiles  = []
        for i in tiles_1:
            tiles.extend(i)
        self.assertEqual(tiles[4], 5)

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
