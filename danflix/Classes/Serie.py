from entidade_base import EntidadeBase
from genero import Genero

class Series(EntidadeBase):
    def __init__(self,id, genero, titulo, descricao, ano):
        self.id = id
        self.genero = genero
        self.titulo = titulo
        self.ano = ano
        self.excluido = False
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, tipo):
        self.__genero = Genero(tipo)
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, Titulo):
        self.__titulo = Titulo.title().strip()
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    def retorna_titulo(self):
        return self.titulo

    def retorna_id(self):
        return self.id    
    
    def retorna_excluido(self):
        return self.excluido
    
    def excluir(self):
        self.excluido = True
