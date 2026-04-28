"""Exercício 5: Mock Test

Parte 1:
1. Faça dois testes sem mock para o método get_tile da classe PuzzleGame.
2. Faça os mesmos dois testes com mocks para o método get_tile da classe PuzzleGame.

Para o projeto PuzzleGame:
1. Inclua o arquivo puzzle_game_with_mock.py no projeto.
    Este arquivo tem a classe PuzzleGameWithPlayer que é subclasse de PuzzleGame.
2. Faça dois testes sem mock envolvendo o método end_of_the_game da classe PuzzleGameWithPlayer.
3. Faça os mesmos dois testes envolvendo o método end_of_the_game da classe PuzzleGameWithPlayer
    utilizando mock para o método save_game_to_file.
    Obs: o método com ”mockeado” é o save_game_to_file e não o método end_of_the_game.
"""

import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'conteudo'))
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'views'))

import unittest
from unittest.mock import patch, Mock


from conteudo.puzzle_game import PuzzleGame
from conteudo.puzzle_game_with_mock import PuzzleGameWithPlayer
from views.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786

# mock do get_tile
# @patch('board.Board.get_tile')
class ClasseMockGetTile(unittest.TestCase):
    def setUp(self):
        self.dimension = 3
        self.game = PuzzleGame(self.dimension)

    def test_move_tile_6(self):
        self.game.move_empty_tile("UP")

        self.assertEqual(self.game.get_tile(3, 3), 6)

    def test_move_tile_8(self):
        self.game.move_empty_tile("LEFT")

        self.assertEqual(self.game.get_tile(3, 3), 8)

    @patch('puzzle_game.PuzzleGame.get_tile')
    def test_move_tile_6_with_mock(self, mock_get_tile):
        mock_get_tile.result_value = 6

        self.game.move_empty_tile("UP")

        self.assertEqual(self.game.get_tile(3, 3), 6)

    @patch('puzzle_game.PuzzleGame.get_tile')
    def test_move_tile_8_with_mock(self, mock_get_tile):
        mock_get_tile.result_value = 8

        self.game.move_empty_tile("LEFT")

        self.assertEqual(self.game.get_tile(3, 3), 8)

class ClasseMockEndGame(unittest.TestCase):
    def setUp(self):
        self.dimension = 3
        self.player_name = "Test"
        self.game = PuzzleGameWithPlayer(self.dimension, self.player_name)
        self.shuffler = TestingShufflerPuzzleGame3x3To12345X786()

    def test_verify_game_finished_no_mock(self):
        self.assertEqual(self.game.end_of_the_game(), "Saved")

    def test_verify_game_not_finished_no_mock(self):

        self.game.shuffle(self.shuffler)

        self.assertEqual(self.game.end_of_the_game(), "Game not finished")

    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_verify_game_finished(self, mock_save_game_to_file):
        mock_save_game_to_file.return_value = "Saved"
        self.assertEqual(self.game.end_of_the_game(), "Saved")

    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_verify_game_not_finished(self, mock_save_game_to_file):
        mock_save_game_to_file.return_value = "Saved"

        self.game.shuffle(self.shuffler)

        self.assertEqual(self.game.end_of_the_game(), "Game not finished")


if __name__ == '__main__':
    unittest.main()