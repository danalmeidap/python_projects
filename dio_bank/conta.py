from tipoconta import TipoConta
from enum import Enum


class Conta:
    def __init__(self,TipoConta, Saldo, Credito, Cliente):
        self.TipoConta = TipoConta
        self.Saldo = Saldo
        self.Credito = Credito
        self.Cliente = Cliente
    

    @property
    def TipoConta(self):
        return self._TipoConta

    
    @TipoConta.setter
    def TipoConta(self,valor):
        if isinstance(valor, str):
            valor = TipoConta(valor)
        self._TipoConta = valor
        return valor


    @property
    def Saldo(self):
        return self._Saldo

    
    @Saldo.setter
    def Saldo(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._Saldo = valor
        return valor

    
    @property
    def Credito(self):
        return self._Credito

    
    @Credito.setter
    def Credito(self,valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._Credito = valor
        return valor
    

    @property
    def Cliente(self):
        return self._Cliente
    

    @Cliente.setter
    def Cliente(self, nome):
        if isinstance(nome, int):
            nome = str(nome)
        self._Cliente = nome
        return nome


    def Sacar(self, valor_saque):
        if self.Saldo - valor_saque < self.Credito * -1:
            print("Saldo insuficiente")
            return False
        self.Saldo -= valor_saque
        print(f'Saldo atual da conta de {self.Cliente} é: {self.Saldo}')
        return True
    

    def Depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.Saldo += valor_deposito
            print(f'Saldo atual da conta de {self.Cliente} é {self.Saldo}')
        else:
            print('Reveja o valor de deposito e digite novamente')
            print(f'Saldo atual da conta de {self.Cliente} é: {self.Saldo}')
    

    def Transferir(self, valor_transferencia, conta_destino):
        if self.Sacar(valor_transferencia):
            conta_destino.Depositar(valor_transferencia)
    

    def __str__(self):
        retorno = " "
        retorno += f'TipoConta: {self.TipoConta}'  + " | "
        retorno += f'Nome: {self.Cliente}' + " | "
        retorno += f'Saldo: {self.Saldo}'  + " | "
        retorno += f'Crédito: {self.Credito}'
        return retorno


    def __repr(self):
        return self.__str__