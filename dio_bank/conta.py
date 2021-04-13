from tipoconta import TipoConta


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
        self._TipoConta = valor
        return valor


    @property
    def Saldo(self):
        return self._Saldo

    
    @Saldo.setter
    def Saldo(self, valor):
        self._Saldo = valor
        return valor

    
    @property
    def Credito(self):
        return self._Credito

    
    @Credito.setter
    def Credito(self,valor):
        self._Credito = valor
        return valor
    

    @property
    def Cliente(self):
        return self._Cliente
    

    @Cliente.setter
    def Cliente(self, nome):
        self._Cliente = nome.title().strip()
        return nome


    def Sacar(self, valor_saque):
        if self.Saldo - valor_saque < self.Credito * -1:
            print(f"Não foi possível completar a operação de {valor_saque}")
            return False
        self.Saldo -= valor_saque
        print(f'Saldo atual da conta de {self.Cliente} é: R$ {self.Saldo:.2f}')
        return True
    

    def Depositar(self, valor_deposito):
        self.Saldo += valor_deposito
        print(f'Saldo atual da conta de {self.Cliente} é R$ {self.Saldo:.2f}')
    

    def Transferir(self, valor_transferencia, conta_destino):
        if self.Sacar(valor_transferencia):
            conta_destino.Depositar(valor_transferencia)
    

    def __str__(self):
        retorno = " "
        retorno += f'TipoConta: {self.TipoConta}'  + " | "
        retorno += f'Nome: {self.Cliente}' + " | "
        retorno += f'Saldo: R$ {self.Saldo:.2f}'  + " | "
        retorno += f'Crédito: R$ {self.Credito:.2f}'
        return retorno


    def __repr__(self):
        return self.__str__