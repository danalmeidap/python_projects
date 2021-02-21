from random import choice
from re import search, IGNORECASE


def player_choice():
    """
    Função em que o jogador escolhe entre as opções existentes para jogar ROck,Paper, Scissors
    :return: A escolha do jogador entre as opções válidas.
    """
    player = str(input('Choose Between Rock, Paper or Scissors')).strip().lower()
    while player not in ['rock', 'paper', 'scissors']:
        player = str(input('Invalid! Please choose between Rock, Paper or Scissors')).strip().lower()
    return player


def enemy_choice():
    """
    Escolha do computador, baseado num random.choise entre as opções existentes.
    :return: A escolha do adversário entre as opções válidas.
    """
    jaken_options = ['rock', 'paper', 'scissors']
    enemy = choice(jaken_options)
    return enemy


def jo_ken_po(player, computer):
    """
    Baseado nas escolhas do jogador e do adversário, são feitas comparações e, assim obtemos o vencedor.
    :param player: Escolha do jogador obtida pela função player_choice
    :param computer: Escolha do jogador obtida pela função player_choice
    :return: Função sem retorno
    """
    print(f'Player choice: {player}')
    print(f'Computer choice {computer}')
    print('-=-' * 15)
    if not (not (player == 'rock' and computer == 'scissors') and not (
            player == 'paper' and computer == 'rock')) or player == 'scissors' and computer == 'paper':
        print(f'{player} beats {computer},You win!')
        print('Let s play again?')
    elif player == computer:
        print(f'We choose the same {player}. Tie.')
        print('Let s play again?')
    else:
        print(f'{computer} beats {player}. You loose')
        print('Let s play again?')
        print('-=-' * 15)


def joken_game():
    """
    Parte de validações para jo jogo, em que o jogador escolhe jogar ou não
    :return: função sem retorno
    """
    print('Do you want to play jo_ken_po?')
    while True:
        answer = str(input('Answer:')).strip().lower()
        if search("^y(es)?$", answer, IGNORECASE):
            player_1 = player_choice()
            player_2 = enemy_choice()
            jo_ken_po(player_1, player_2)
        elif search("^N(o)?$", answer, IGNORECASE):
            break
        else:
            print('Please, use only y(es) or n(o) for answer.')


try:
    joken_game()
except Exception as err:
    print(f'Erro: {err}')
else:
    print('GAME OVER!')
finally:
    print('Thank you for playing')
