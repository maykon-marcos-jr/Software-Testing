"""Exercício 2 24/03/2026
@Author: Maykon Marcos Junior

Teste de Unidade com Diferentes Estratégias de Setup

---
Criar testes de unidade para um sistema bancário
▪ utilizando o inline setup, implicit setup e delegated setup.
Um teste pode combinar diferentes estratégias.

Obs:
▪ Indique, para cada teste, quais estratégias estão sendo usadas
    ▪ (inline, implicit e/ou delegated).
▪ Indique também as fases de cada teste
    ▪ (Fixture Setup, Exercise SUT, Result Verification e Fixture Teardown).

Faça 20 ou mais testes de unidade para as seguintes classes:
▪ Dinheiro
▪ Valor Monetario
▪ Banco
▪ Agencia
▪ Conta
▪ SistemaBancario

Obs: as operações para depositar, sacar e transferir dinheiro
devem ser realizadas a partir do sistema bancário.
"""

import unittest

from sistema_bancario import SistemaBancario
from agencia import Agencia
from banco import Banco
from conta import Conta
from dinheiro import Dinheiro, Moeda
from transacao import ValorMonetario
from operacao import EstadosDeOperacao, Operacao

class AuxTestSistemaBancario:
    def criar_banco(self) -> Banco:
        return Banco("Banco Teste", Moeda.BRL)

    def criar_agencia(self) -> Agencia:
        banco = self.criar_banco()
        return Agencia("Agencia Teste", 1, banco)

    def criar_conta(self) -> Conta:
        agencia = self.criar_agencia()
        return Conta("Conta Teste", 1, agencia)

class TestSistemaBancario(unittest.TestCase):
    def setUp(self):
        self.sistema_bancario = SistemaBancario()
        self.aux = AuxTestSistemaBancario()

    def test_moeda_brl(self):
        # implicit setup
        # inline setup
        sym = "R$"
        frac = 100

        # exercise SUT
        moeda = Moeda.BRL

        # result verification
        self.assertEqual(sym, moeda.simbolo(), "Símbolo errado")
        self.assertEqual(frac, moeda.base_fracionaria(), "Base errada")

        # fixture teardown

    def test_criar_agencia(self):
        # implicit setup
        # delegated setup
        banco = self.aux.criar_banco()
        # inline setup
        nome = "Agencia Teste"
        cod = 1

        # exercise sut
        agencia = Agencia(nome, cod, banco)

        # result verification
        self.assertEqual(nome, agencia.nome)
        self.assertEqual(cod, int(agencia.obter_identificador()))

        # fixture teardown

    def test_criar_banco_brl(self):
        # implicit setup
        # inline setup
        nome = "Banco 1"
        moeda = Moeda.BRL

        # exercise sut
        banco = Banco(nome, moeda)

        # result verification
        self.assertEqual(nome, banco.nome, "Nome do Banco inválido")

        # fixture teardown

    def test_criar_banco_usd(self):
        # implicit setup
        # inline setup
        nome = "Banco 1"
        moeda = Moeda.USD

        # exercise sut
        banco = Banco(nome, moeda)

        # result verification
        self.assertEqual(nome, banco.nome, "Nome do Banco inválido")

        # fixture teardown

    def test_criar_banco_chf(self):
        # implicit setup
        # inline setup
        nome = "Banco 1"
        moeda = Moeda.CHF

        # exercise sut
        banco = Banco(nome, moeda)

        # result verification
        self.assertEqual(nome, banco.nome, "Nome do Banco inválido")

        # fixture teardown

    def test_criar_dinheiro_brl(self):
        # implicit setup
        # inline setup
        moeda = Moeda.BRL
        inteiro = 1
        frac = 50

        # exercise sut
        dinheiro = Dinheiro(moeda, inteiro, frac)

        # result verification
        self.assertEqual(moeda, dinheiro.moeda, "Moeda Errada")
        self.assertEqual(inteiro, dinheiro.inteiro, "Porção Inteira Errada")
        self.assertEqual(frac, dinheiro.fracionado, "Centavos Errados")

        # fixture teardwon

    def test_criar_dinheiro_usd(self):
        # implicit setup
        # inline setup
        moeda = Moeda.USD
        inteiro = 1
        frac = 50

        # exercise sut
        dinheiro = Dinheiro(moeda, inteiro, frac)

        # result verification
        self.assertEqual(moeda, dinheiro.moeda, "Moeda Errada")
        self.assertEqual(inteiro, dinheiro.inteiro, "Porção Inteira Errada")
        self.assertEqual(frac, dinheiro.fracionado, "Centavos Errados")

        # fixture teardwon

    def test_criar_dinheiro_chf(self):
        # implicit setup
        # inline setup
        moeda = Moeda.CHF
        inteiro = 1
        frac = 50

        # exercise sut
        dinheiro = Dinheiro(moeda, inteiro, frac)

        # result verification
        self.assertEqual(moeda, dinheiro.moeda, "Moeda Errada")
        self.assertEqual(inteiro, dinheiro.inteiro, "Porção Inteira Errada")
        self.assertEqual(frac, dinheiro.fracionado, "Centavos Errados")

        # fixture teardwon

    def test_criar_banco_pelo_sistema_com_brl(self):
        # implicit setup
        # inline setup
        nome = "Banco 1"
        moeda = Moeda.BRL

        # exercise sut
        banco = self.sistema_bancario.criar_banco(nome, moeda)

        # result verification
        self.assertEqual(nome, banco.nome, "Nome do Banco inválido")
        self.assertEqual(moeda, banco.moeda, "Moeda do Banco inválido")

        # fixture teardown

    def test_criar_banco_pelo_sistema_com_usd(self):
        # implicit setup
        # inline setup
        nome = "Banco 1"
        moeda = Moeda.USD

        # exercise sut
        banco = self.sistema_bancario.criar_banco(nome, moeda)

        # result verification
        self.assertEqual(nome, banco.nome, "Nome do Banco inválido")
        self.assertEqual(moeda, banco.moeda, "Moeda do Banco inválido")

        # fixture teardown

    def test_criar_banco_pelo_sistema_com_chf(self):
        # implicit setup
        # inline setup
        nome = "Banco 1"
        moeda = Moeda.BRL

        # exercise sut
        banco = self.sistema_bancario.criar_banco(nome, moeda)

        # result verification
        self.assertEqual(nome, banco.nome, "Nome do Banco inválido")
        self.assertEqual(moeda, banco.moeda, "Moeda do Banco inválido")

        # fixture teardown

    def test_criar_dinheiro_negativo(self):
        # implicit setup
        # inline setup
        moeda = Moeda.BRL
        inteiro = -1
        frac = 500

        # exercise sut
        # result verification
        with self.assertRaises(ValueError):
            Dinheiro(moeda, inteiro, frac)


        # fixture teardwon

    def test_criar_dinheiro_500_cents(self):
        # implicit setup
        # inline setup
        moeda = Moeda.BRL
        inteiro = 1
        frac = 500

        # exercise sut
        dinheiro = Dinheiro(moeda, inteiro, frac)

        # result verification
        self.assertEqual(moeda, dinheiro.moeda, "Moeda Errada")
        self.assertEqual(inteiro + 5, dinheiro.inteiro, "Porção Inteira Errada")
        self.assertEqual(0, dinheiro.fracionado, "Centavos Errados")

        # fixture teardwon

    def test_criacao_de_agencia_pelo_banco(self):
        # implicit setup
        # delegated setup
        banco = self.aux.criar_banco()
        # inline setup
        agencia_nome = "Agencia-Teste"
        # exercise sut
        agencia = banco.criar_agencia(agencia_nome)
        # result verification
        self.assertEqual(banco, agencia.banco, "Banco Inválido")
        self.assertEqual(agencia_nome, agencia.nome, "Nome Inválido")
        self.assertEqual(1, len(banco.obter_agencias()), "Agencia não adicionadas")
        self.assertEqual(agencia, banco.obter_agencias()[0])
        self.assertEqual(agencia, banco.obter_agencia(agencia_nome))
        # fixture teardown

    def test_criacao_de_conta_pela_agencia(self):
        # implicit setup
        # delegated setup
        agencia = self.aux.criar_agencia()
        # inline setup
        titular = "Titular-Teste"
        # exercise sut
        conta = agencia.criar_conta(titular)
        # result verification
        self.assertEqual(titular, conta.titular, "Titular Inválido")
        self.assertEqual(agencia, conta.agencia, "Agência Inválida")
        # fixture teardown

    def test_deposito(self):
        # implicit setup
        # delegated setup
        conta = self.aux.criar_conta()
        # inline setup
        quantia = Dinheiro(Moeda.BRL, 1, 50)

        # exercise SUT
        op = self.sistema_bancario.depositar(conta, quantia)

        # result verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, op.obter_estado())

        # fixture teardown

    def test_deposito_moeda_invalida(self):
        # implicit setup
        # delegated setup
        conta = self.aux.criar_conta()
        # inline setup
        quantia = Dinheiro(Moeda.USD, 1, 50)

        # exercise SUT
        op = self.sistema_bancario.depositar(conta, quantia)

        # result verification
        self.assertEqual(EstadosDeOperacao.MOEDA_INVALIDA, op.obter_estado())

        # fixture teardown

    def test_sacar(self):
        # implicit setup
        # delegated setup
        conta = self.aux.criar_conta()
        # inline setup
        quantia = Dinheiro(Moeda.BRL, 1, 50)
        self.sistema_bancario.depositar(conta, quantia)

        # exercise SUT
        op = self.sistema_bancario.sacar(conta, quantia)

        # result verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, op.obter_estado())

        # fixture teardown

    def test_transferir(self):
        # implicit setup
        # delegated setup
        conta1 = self.aux.criar_conta()
        conta2 = self.aux.criar_conta()
        # inline setup
        quantia = Dinheiro(Moeda.BRL, 1, 50)
        self.sistema_bancario.depositar(conta1, quantia)

        # exercise SUT
        op = self.sistema_bancario.transferir(conta1, conta2, quantia)

        # result verification
        self.assertEqual(EstadosDeOperacao.SUCESSO, op.obter_estado())
        self.assertEqual(Dinheiro(Moeda.BRL, 0, 0), conta1.calcular_saldo().obter_quantia())
        self.assertEqual(quantia, conta2.calcular_saldo().obter_quantia())

        # fixture teardown

    def test_deposito_0(self):
        # implicit setup
        # delegated setup
        conta = self.aux.criar_conta()
        # inline setup
        quantia = Dinheiro(Moeda.BRL, 0, 0)

        # exercise SUT
        op = self.sistema_bancario.depositar(conta, quantia)

        # result verification
        self.assertEqual(EstadosDeOperacao.SALDO_INSUFICIENTE, op.obter_estado())

        # fixture teardown


if __name__ == '__main__':
    unittest.main()