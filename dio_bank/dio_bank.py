from conta import Conta
from tipoconta import TipoConta
import os

# Para ser usado no módulo interface
def cls():
    os.system('cls' if os.name=='nt' else 'clear')




minha_conta = Conta(1, "R$1200.00", 200, "Daniel Almeida")
print(minha_conta)

