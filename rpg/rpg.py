from classe import personagem

lista_personagens = []
char = {'nome': '', 'pv': '', 'ca': '', 'iniciativa': ''}
quantidade_de_personagens = int(input('Quantidade de personagens:'))
cont = 0
while cont < quantidade_de_personagens:
    nome: str = str(input('Nome do personagem:'))
    pv = int(input(f'Pontos de vida do(a) {nome}: '))
    ca = int(input(f'Classe de armadura do(a) {nome}:'))
    iniciativa = int(input(f'Valor da iniciativa de {nome}:'))
    a = personagem(nome, pv, ca, iniciativa)
    char['nome'] = a.getNome_personagem()
    char['pv'] = a.getPv()
    char['ca'] = a.getCa()
    char['iniciativa'] = a.getIniciativa()
    lista_personagens.append(char.copy())
    char.clear()
    cont = cont + 1
print(sorted(lista_personagens, key=lambda personagem: personagem['iniciativa'], reverse=True))
