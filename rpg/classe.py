class personagem:
    def __init__(self, nome_personagem, pv, ca, iniciativa):
        self.nome_personagem = nome_personagem
        self.pv = pv
        self.ca = ca
        self.iniciativa = iniciativa

    def setNome_personagem(self, nome_personagem):
        self.nome_personagem = nome_personagem

    def setPv(self, pv):
        self.pv = pv

    def setCa(self, ca):
        self.ca = ca

    def setIniciativa(self, iniciativa):
        self.iniciativa = iniciativa

    def getNome_personagem(self):
        return self.nome_personagem

    def getPv(self):
        return self.pv

    def getCa(self):
        return self.ca

    def getIniciativa(self):
        return self.iniciativa
