"""Exercício-4: Fluxo de Dados

Considere como unidade de programa o método get_tile da classe PuzzleGame do projeto EightPuzzle.

Para esta unidade:
1. Faça o GFD (Grafo de Fluxo de Dados).
2. Indique os caminhos selecionados utilizando os seguintes critérios de teste de fluxo de dados:
    (i) All-c-uses/Some-p-uses e
    (ii) All-p-uses.
    Considere os dados line e column.
3. Para cada caminho selecionado faça um teste de unidade.
4. Mostre a execução de cada teste de unidade utilizando o debug para que seja possível mostrar a execução dos comandos do m
---
A execução de cada teste de unidade (um teste para cada caminho) utilizando o debug para que seja possível ver os comandos internos do método get_tile que foram executados.
"""
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'conteudo'))

from puzzle_game import PuzzleGame
from invalid_position_exception import InvalidPositionException

import unittest


class ClasseTestesAllP(unittest.TestCase):
    def setUp(self):
        self.dimension = 3
        self.game = PuzzleGame(self.dimension)

    def test_line_bellow_0(self):
        with self.assertRaises(InvalidPositionException):
            l, c = -1, 1
            self.game.get_tile(l, c)

    def test_non_empty_line(self):
        l, c = 2, 3
        tile = self.game.get_tile(l, c)
        self.assertEqual(tile, 6)

    def test_empty_position(self):
        l, c = 3, 3
        tile = self.game.get_tile(l, c)
        self.assertEqual(tile, " ")


class ClasseTestAllC_SomeP(unittest.TestCase):
    def setUp(self):
        self.dimension = 3
        self.game = PuzzleGame(self.dimension)

    def test_get_valid_tile(self):
        l, c = 1, 1
        tile = self.game.get_tile(l, c)
        self.assertEqual(tile, 1)


if __name__ == '__main__':
    unittest.main()