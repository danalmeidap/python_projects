from interface import exibir_menu
import operacoes


def obter_opcao_usuario():
    escolha = str(input()).upper()
    return escolha


opcoes = ["1","2","3","4","5","C","X"]
while True:
    exibir_menu()
    opcao_usuario = obter_opcao_usuario()
    if opcao_usuario in opcoes:
        if opcao_usuario == "1":
            operacoes.listar_contas()   
        if opcao_usuario == "2":
            operacoes.inserir_nova_conta()
        if opcao_usuario == "3":
            operacoes.transferir()
        if opcao_usuario == "4":
            operacoes.sacar()
        if opcao_usuario == "5":
            operacoes.depositar()
        if opcao_usuario == "C":
            operacoes.cls()
        if opcao_usuario == "X":
            break
    else:
        print("Por favor, digite uma opção válida")
print("Obrigado por utilizar nossos serviços.")