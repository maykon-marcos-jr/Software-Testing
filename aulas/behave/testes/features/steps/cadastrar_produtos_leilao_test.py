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

@given(u'o cadastro do usuario {nome_usuario} foi realizado')
def step_impl(context, nome_usuario):
    context.nome_usuario = nome_usuario
    # adding default values for the user, to create the user in the system
    context.endereco_usuario = 'Rua A, 123'
    context.email_usuario = 'usuario@email.com'
    context.cpf_usuario = '055.761.919-00'
    context.data_limite = 100

    context.mercado = MercadoLeilao()

    context.mercado.cadastra_usuario(context.nome_usuario, context.endereco_usuario,
    context.email_usuario, context.cpf_usuario)

@given(u'o nome do produto {nome_produto}')
def step_impl(context, nome_produto):
    context.nome_produto = nome_produto

@given(u'a descricao do produto {descricao_produto}')
def step_impl(context, descricao_produto):
    context.descricao_produto = descricao_produto

@given(u'e o lance {lance_minimo}')
def step_impl(context, lance_minimo):
    context.lance_minimo = lance_minimo

@given(u'e o cpf do leiloador {cpf_leiloador}')
def step_impl(context, cpf_leiloador):
    context.cpf_leiloador = cpf_leiloador

@when(u'cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(context.nome_produto, context.descricao_produto,
        context.lance_minimo, context.cpf_leiloador, context.data_limite)
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
    context.descricao_produto = 'amarelo'
    context.lance_minimo = 100
    context.cpf_leiloador = context.cpf_usuario

    context.mercado.cadastra_produto(context.nome_produto, context.descricao_produto,
    context.lance_minimo, context.cpf_leiloador, context.data_limite)

@then(u'o sistema mostra a mensagem O produto ja existe ou o leiloador nao esta cadastrado.')
def step_impl(context):
    assert context.msg == 'O produto ja existe ou o leiloador nao esta cadastrado.'



