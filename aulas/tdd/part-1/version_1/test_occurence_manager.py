"""
Uma empresa W possui vários funcionários e desenvolve vários projetos.
Cada funcionário pode trabalhar em vários projetos simultaneamente
e cada projeto pode ter vários funcionários

# História iniciais
Criação da empresa W
Inclusão de funcionário na empresa
Inclusão de projeto na empresa
Inclusão de funcionário da empresa em um projeto

Lista Inicial de Testes
Enumerar testes de criação da Empresa
Enumerar testes de criação de Funcionário e inclusão na empresa
Enumerar testes de criação de Projeto e inclusão na empresa
"""

# PYTHONPATH=.:. coverage run --branch -m unittest test_occurence_manager.TestOccurenceManager
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
# to allow the code called to run modules on the same dir
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'conteudo'))


import unittest

from company import Company

class TestOccurenceManager(unittest.TestCase):

    def test_create_company(self):
        name = "W"
        company = Company(name)
        self.assertEqual(name, company.get_name())


if __name__ == '__main__':
    unittest.main()