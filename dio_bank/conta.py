from tipoconta import TipoConta

class Conta:
    def __init__(self, TipoConta, Saldo, Credito, Cliente):
        self.TipoConta = TipoConta
        self.Saldo = Saldo
        self.Credito = Credito
        self.Cliente = Cliente

    @property
    def tipoConta(self):
        return self._TipoConta

    @tipoConta.setter
    def tipoConta(self, valor):
        self._TipoConta = TipoConta(valor)

    @property
    def saldo(self):
        return self._Saldo

    @saldo.setter
    def saldo(self, valor):
        self._Saldo = valor

    @property
    def credito(self):
        return self._Credito

    @credito.setter
    def credito(self, valor):
        self._Credito = valor

    @property
    def cliente(self):
        return self._Cliente

    @cliente.setter
    def cliente(self, nome):
        self._Cliente = nome.title().strip()
    
    def sacar(self, valor_saque):
        if self.Saldo - valor_saque < self.Credito * -1:
            print(f"Não foi possível completar a operação de {valor_saque}")
            return False
        self.Saldo -= valor_saque
        self.mostrar_saque(valor_saque)
        print(f'Saldo atual da conta de {self.Cliente} é: R$ {self.Saldo:.2f}')
        return True
    
    def mostrar_saque(self,montante):
        total = montante
        cedula = 100
        total_cedulas = 0
        print('Foram sacadas :', end= '')
        while True:
            if total >= cedula:
                total -= cedula
                total_cedulas += 1
            else:
                if total_cedulas > 0:
                    print(f'{total_cedulas} cédulas de R$ {cedula}')
                if cedula == 100:
                    cedula = 50
                elif cedula == 50:
                    cedula = 20
                elif cedula == 20:
                    cedula = 10
                elif cedula == 10:
                    cedula= 5
                elif cedula == 5:
                    cedula = 2
                elif cedula == 2:
                    cedula = 1
                total_cedulas = 0
                if total == 0 or cedula == 1:
                    break


    def depositar(self, valor_deposito):
        self.Saldo += valor_deposito
        print(f'Saldo atual da conta de {self.Cliente} é R$ {self.Saldo:.2f}')

    def transferir(self, valor_transferencia, conta_destino):
        if self.sacar(valor_transferencia):
            conta_destino.depositar(valor_transferencia)

    def __str__(self):
        retorno = " "
        retorno += f'TipoConta: {self.TipoConta}' + " | "
        retorno += f'Nome: {self.Cliente}' + " | "
        retorno += f'Saldo: R$ {self.Saldo:.2f}' + " | "
        retorno += f'Crédito: R$ {self.Credito:.2f}'
        return retorno

    def __repr__(self):
        return self.__str__
