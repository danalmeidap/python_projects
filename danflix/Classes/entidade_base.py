class EntidadeBase:
    def __init__(self):
        self.id = id

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor