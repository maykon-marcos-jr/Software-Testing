#  Feature: Cadastrar Produto Usando Setup
#     Cadastrar usuarios

# Background:
# Given o cadastro do usuario Ernani Cesar foi realizado

# Scenario: Cadastrar Produto com Sucesso
# Given o nome do produto sofa
#     And a descricao do produto amarelo
#     And e o lance 100
#     And e o cpf do leiloador 055.761.919-00
# When cadastrar o produto
# Then o sistema cadastra com sucesso

# Scenario: Cadastro de Produto com Problema
# Given sofa amarelo ja foi cadastrado
#     And o nome do produto sofa
#     And a descricao do produto amarelo
#     And e o lance 100
#     And e o cpf do leiloador 055.761.919-00
# When cadastrar o produto
# Then o sistema mostra a mensagem O produto ja existe ou o leiloador nao esta cadastrado.

from behave import *
from src.mercado_leilao import MercadoLeilao


"""
Feature: Cadastrar Usuario
Cadastrar usuarios
Scenario: Cadastrar Usuario com Sucesso
Given O nome de usuario Ernani Cesar
And o endereco Campus Universitario
And o CPF 055.761.919-00
And o e-mail ernani.santos@posgrad.ufsc.br
When O usuario eh cadastrado
Then O sistema deve possuir usuarios
"""

@given(u'o cadastro do usuario {nome_usuario} foi realizado')
def step_impl(context, nome_usuario):
    context.nome_usuario = nome_usuario
    context.endereco_usuario = 'Rua AAA, 123'
    context.email_usuario = 'user@email.com'
    context.leiloador_cpf = '055.761.919-00'
    context.data_limite = 100

    context.mercado = MercadoLeilao()

    context.mercado.cadastra_usuario(context.nome_usuario, context.endereco_usuario, context.email_usuario, context.leiloador_cpf)


@given(u'o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto


@given(u'a descricao do produto {produto_descricao}')
def step_impl(context, produto_descricao):
    context.produto_descricao = produto_descricao


@given(u'e o lance {lance_value}')
def step_impl(context, lance_value):
    context.lance_value = lance_value


@given(u'e o cpf do leiloador {leiloador_cpf}')
def step_impl(context, leiloador_cpf):
    context.leiloador_cpf = leiloador_cpf


@when(u'cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(context.nome_produto, context.produto_descricao, context.lance_value, context.leiloador_cpf, context.data_limite)
        context.msg = 'Produto cadastrado com sucesso'
    except Exception as e:
        context.msg = e.__str__()


@then(u'o sistema cadastra com sucesso')
def step_impl(context):
    assert context.msg == 'Produto cadastrado com sucesso'
    assert context.mercado.existe_produto(context.nome_produto)


@given(u'sofa amarelo ja foi cadastrado')
def step_impl(context):
    context.nome_produto = 'sofa'
    context.produto_descricao = 'amarelo'
    context.lance_value = 100
    context.leiloador_cpf = context.leiloador_cpf

    context.mercado.cadastra_produto(context.nome_produto, context.produto_descricao, context.lance_value, context.leiloador_cpf, context.data_limite)


@then(u'o sistema mostra a mensagem O produto ja existe ou o leiloador nao esta cadastrado.')
def step_impl(context):
    assert context.msg == "O produto ja existe ou o leiloador nao esta cadastrado."