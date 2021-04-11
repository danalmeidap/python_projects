from conta import Conta
from tipoconta import TipoConta
import os

# Para ser usado no módulo interface
def cls():
    os.system('cls' if os.name=='nt' else 'clear')




minha_conta = Conta(TipoConta.PessoaFisica, 1200.00, 200, "Daniel Almeida")
outra_conta = Conta(TipoConta.PessoaJuridica, 2000.00, 500, "Maria Patricio")

