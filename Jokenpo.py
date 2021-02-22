from random import choice
from re import search, IGNORECASE


def player_choice():
    """
    jogador escolhe entre as opções existentes.
    :return: A escolha do jogador entre as opções válidas.
    """
    player = str(input('Choose:[Rock, Paper or Scissors]: ')).strip().lower()
    while player not in jaken_options:
        player = str(input('Invalid!Rock, Paper or Scissors:')).strip().lower()
    return player


def enemy_choice():
    """
    Escolha do computador baseada nas opções existentes.
    :return: A escolha do adversário entre as opções válidas.
    """
    enemy = choice(jaken_options)
    return enemy


def jo_ken_po(player, computer):
    """
    Realiza a jogada do jokenpo
    :param player: Escolha do jogador obtida pela função player_choice
    :param computer: Escolha do jogador obtida pela função player_choice
    :return: Função sem retorno
    """
    print(f'Player choice: {player}')
    print(f'Computer choice {computer}')
    print('-=-' * 15)
    if (not (not ('rock' == player and computer == 'scissors')
             and not (player == 'paper' and computer == 'rock')))\
            or (not 'scissors' != player and computer == 'paper'):
        winner = print_winner(player, computer, winner=True)
        print(winner)
        print('Let s play again?')
        print('-=-' * 15)
    elif player == computer:
        winner = print_winner(player, computer, tie=True)
        print(winner)
        print('Let s play again?')
        print('-=-' * 15)
    else:
        winner = print_winner(player, computer)
        print(winner)
        print('Let s play again?')
        print('-=-' * 15)


def joken_game():
    """
    Valida as entradas do usuário para jogar ou não.
    :return: função sem retorno
    """
    print('Do you want to play jo_ken_po?')
    while True:
        answer = str(input('Answer: ')).strip().lower()
        if search("^y(es)?$", answer, IGNORECASE):
            player_1 = player_choice()
            player_2 = enemy_choice()
            jo_ken_po(player_1, player_2)
        elif search("^N(o)?$", answer, IGNORECASE):
            answer = str(input('Are you sure? [Yes/No]: ')).strip().lower()
            check = False
            if search("^y(es)?$", answer, IGNORECASE):
                print('Thank you for Playing')
                print('-=-' * 15)
                check = True
            elif search("^N(o)?$", answer, IGNORECASE):
                joken_game()
            else:
                print('Please, use only y(es) or n(o) for answer.')
            if check:
                break
        else:
            print('Please, use only y(es) or n(o) for answer.')


def print_winner(player1, enemy, winner=False, tie=False):
    if winner:
        return f'{player1} beats {enemy}, You win!'
    if tie:
        return 'We choose the same.Tie.'
    return f'{enemy} beats {player1}, You loose!'


jaken_options = ['rock', 'paper', 'scissors']
joken_game()
