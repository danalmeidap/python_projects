from conta import Conta
from tipoconta import TipoConta
import os
from datetime import datetime


def cls():
    print("\n" * os.get_terminal_size().lines)


def check_int(msg):
    while True:
        try:
            value = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mThe value must be valid\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return value


def check_str(msg):
    while True:
        try:
            value = str(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mThe value must be valid\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return value


def check_float(msg):
    while True:
        try:
            value = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mThe value must be valid\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return value


def listar_contas():
    if len(contas) == 0:
        print("Nenhuma conta cadastrada")
        return
    print(f"Contas existentes em {data} as {hora}")
    for i in range(len(contas)):
        conta = contas[i]
        print(f'{i}', end="")
        print(conta)


def inserir_nova_conta():
    print("Inserir nova conta")
    tipos_conta = range(1)
    modalidade_conta = check_int("Digite 0 para PessoaFisica ou 1 para pessoa jurífica: ")
    while modalidade_conta not in tipos_conta:
        print("Valor Incorreto", end=" ")
        modalidade_conta = check_int("Digite 0 para PessoaFisica ou 1 para pessoa jurífica: ")
    modalidade_conta = TipoConta(modalidade_conta)
    nome_cliente = check_str("Digite o nome do cliente:")
    saldo_inicial = check_float("Digite o saldo inicial:")
    credito_inicial = check_float("Digite o crédito:")
    nova_conta = Conta(modalidade_conta, saldo_inicial, credito_inicial, nome_cliente)
    contas.append(nova_conta)
    print(f'Nova conta criada em {data} as {hora}')


def depositar():
    indice_conta = check_int("Digite o número da conta: ")
    while indice_conta < 0:
        indice_conta = check_int("Digite o número da conta: ")
    valor_depositar = check_float("Digite o valor a ser depositado: ")
    while valor_depositar < 0:
        valor_depositar = check_float("Digite o valor a ser depositado: ")
    if indice_conta < len(contas):
        contas[indice_conta].depositar(valor_depositar)
        print(f'Depósito para a conta de {contas[indice_conta].Cliente} em {data} as {hora}')
    else:
        print(f"Erro de indice em {data} as {hora}")


def sacar():
    indice_conta = check_int("Digite o número da conta: ")
    while indice_conta < 0:
        indice_conta = check_int("Digite o número da conta: ")
    valor_sacar = check_float("Digite o valor a ser sacado: ")
    while valor_sacar < 0:
        valor_sacar = check_float("Digite o valor a ser sacado: ")
    if indice_conta < len(contas):
        contas[indice_conta].sacar(valor_sacar)
        print(f'Saque feito em {data} as {hora}')
    else:
        print(f"Erro de indice em {data} as {hora}")


def transferir():
    indice_conta = check_int("Digite o número da conta: ")
    while indice_conta < 0:
        indice_conta = check_int("Digite o número da conta: ")
    indice_conta_destino = check_int("Digite o número da conta para transferencia: ")
    while indice_conta_destino < 0:
        indice_conta_destino = check_int("Digite o número da conta para transferencia: ")
    valor_transferido = check_float("Digite o valor a ser transferido: ")
    while valor_transferido < 0:
        valor_transferido = check_float("Digite o valor a ser transferido: ")
    if indice_conta and indice_conta_destino < len(contas):
        contas[indice_conta].transferir(valor_transferido, contas[indice_conta_destino])
        print(f'Transferência para a conta de {contas[indice_conta].Cliente} para {contas[indice_conta_destino].Cliente} em {data} as {hora}')


data = datetime.today().strftime('%d/%m/%Y')
hora = datetime.today().strftime('%H:%M')
contas = []
