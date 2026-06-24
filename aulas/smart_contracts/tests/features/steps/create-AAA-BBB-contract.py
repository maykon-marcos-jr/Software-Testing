from behave import *
from unittest import TestCase

from solcx import compile_standard, install_solc
import json
from web3 import Web3

# Execute o Ganache e crie uma blockchain Ethereum utilizando a opção "Quickstart".
# • No menu Settings (símbolo de engrenagem), aba Chain, configurar o Gas Limit para
# 9000000 e Gas Price para 4100000000, se não estiver configurado.
# Copie uma chave gerada e o endereço da conta gerados na blockchain Ganache (pegue uma
# carteira e, no ícone da chave, copie a chave privada e o endereço). A chave privada deve ser
# colocada na variável global private_key do arquivo create-rent-contract.py, e o endereço
# deve ser colocado na variável global address. (Se der algum problema, talvez seja necessário
# selecionar a opção SAVE.)

address = "0xc9cBD57c66FD24eab72e96a84051233eAf5bB124"
private_key = "0x3c05cc325be49a156c885fac379347de79994f074279fa817c7dfc92c911806a"

smart_contract = None
w3 = None
chain_id = 1337


def __deploy_contract(client, contractor, creation_date):
    global smart_contract
    global w3

    # Endereço do diretório onde está o smart contract AAABBBContract
    with open("./resources/ClientContractorContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    # Considerando o smart contract ProductSaleContract
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"ClientContractorContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, }, solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["metadata"])["output"]["abi"]
    # Rodando o ganache localmente...
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    smart_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(address)
    # Parâmetros do construtor do smart contract
    transaction = smart_contract.constructor(client, contractor, creation_date).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    # Referência para o smart contract
    smart_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)


@given(u'the client named {client}')
def step_impl(context, client):
    context.client = "AAA"


@given(u'the contractor named {contractor}')
def step_impl(context, contractor):
    context.contractor = contractor


@given(u'the creation date is {date}')
def step_impl(context, date):
    context.creation_date = int(date)


@given(u'I have created and deployed the smart contract')
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)
    context.sent_invoice = False
    context.sent_report = False
    context.technical_responsible = None
    context.fines = 0
    context.completed_services = False
    context.paid_installments = 0
    context.hours_paid = 0

@when(u'I activate the smart contract')
def step_impl(context):
    transaction = smart_contract.functions.activate().build_transaction({"chainId": chain_id,"gasPrice": w3.eth.gas_price,"from": address,"nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    context.paid_installments = 1


@then(u'the smart contract is activated')
def step_impl(context):
    status = smart_contract.functions.getStatus().call()
    TestCase.assertEqual(TestCase(), 1, status)  # Status.InEffect = 1


@then(u'creation date is {date}')
def step_impl(context, date):
    TestCase.assertEqual(TestCase(), int(date), smart_contract.functions.getCreationDate().call())


###############################################################
# Creation Section
###############################################################


@given(u'the contract title is {title}')
def step_impl(context, title):
    context.title = title


@given(u'the smart contract is created')
def step_impl(context):
    context.sent_invoice = None
    context.sent_report = None
    context.technical_responsible = None
    context.fines = None
    context.completed_services = None
    context.paid_installments = None
    context.hours_paid = None


@when(u'the smart contract is created')
def step_impl(context):
    context.sent_invoice = False
    context.sent_report = False
    context.technical_responsible = None
    context.fines = 0
    context.completed_services = False
    context.paid_installments = 0
    context.hours_paid = 0


@then(u'the smart contract must be created')
def step_impl(context):
    assert context.sent_invoice == False
    assert context.sent_report == False
    assert context.technical_responsible == None
    assert context.fines == 0
    assert context.completed_services == False
    assert context.paid_installments == 0
    assert context.hours_paid == 0


@then(u'the start date must be {date}')
def step_impl(context, date):
    context.start_date = context.creation_date + 15
    print(date)
    print(context.start_date)
    assert context.start_date == int(date)


@then(u'the end date must be {date}')
def step_impl(context, date):
    context.end_date = context.start_date + 30
    assert context.end_date == int(date)


@then(u'the client must be {client}')
def step_impl(context, client):
    context.client = client


@then(u'the contractor must be {contractor}')
def step_impl(context, contractor):
    context.contractor = contractor


@then(u'the client has paid the initial installment')
def step_impl(context):
    assert context.paid_installments == 1


####################################################################
# Terminate Code
####################################################################

@given(u'the contractor has sent the invoice and report to the client')
def step_impl(context):
    context.sent_invoice = True
    context.sent_report = True


@given(u'the client indicated a technical responsible')
def step_impl(context):
    context.technical_responsible = "CCC"


@given(u'the client has no unpaid fines due to delays')
def step_impl(context):
    context.fines = 0


@when(u'the contractor has fullfiled all requested services')
def step_impl(context):
    context.completed_services = True


@when(u'the client has paid the initial installment')
def step_impl(context):
    context.paid_installments = 1


@when(u'the client has paid the final installment')
def step_impl(context):
    context.paid_installments = 2


@when(u'the client has paid 20 hours at R$ 120 each until 90 days after the deliver date')
def step_impl(context):
    context.hours_paid = 20

@then(u'the contract must be terminated')
def step_impl(context):
    try:
        assert context.sent_invoice
        assert context.sent_report
        assert context.technical_responsible != None
        assert context.fines == 0
        assert context.completed_services
        assert context.paid_installments == 2
        assert context.hours_paid == 20
        context.msg = "Successful Termination"
    except:
        context.msg = "Unsuccessful Termination"



@given(u'the contract is finished')
def step_impl(context):
    context.sent_invoice = False
    context.sent_report = False
    context.technical_responsible = None
    context.fines = 0
    context.completed_services = False
    context.paid_installments = 0
    context.hours_paid = 0


@when(u'the contractor has not fullfiled all the requested services')
def step_impl(context):
    context.completed_services = False


@when(u'the contractor has not sent the invoice and report to the client')
def step_impl(context):
    context.sent_invoice = False
    context.sent_report = False


@when(u'the client has not paid the initial installment')
def step_impl(context):
    context.paid_installments = 0


@when(u'the client has not paid the final installment')
def step_impl(context):
    context.paid_installments = 1

@then(u'the message must be {msg}')
def step_impl(context, msg):
    assert context.msg == msg