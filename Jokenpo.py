from random import choice
from re import search, IGNORECASE


def play_round():
    player_1 = player_choice()
    player_2 = computer_choice()
    jo_ken_po(player_1, player_2)


def player_choice():
    """
    jogador escolhe entre as opções existentes.
    :return: A escolha do jogador entre as opções válidas.
    """
    player = str(input('Choose:[Rock, Paper or Scissors]: ')).strip().lower()
    while player not in jaken_options:
        player = str(input('Invalid!Rock, Paper or Scissors:')).strip().lower()
    return player


def computer_choice():
    """
    Escolha do computador baseada nas opções existentes.
    :return: A escolha do adversário entre as opções válidas.
    """
    cpu = choice(jaken_options)
    return cpu


def jo_ken_po(player, computer):
    """
    Realiza a jogada do jokenpo
    :param player: Escolha do jogador obtida pela função player_choice
    :param computer: Escolha do jogador obtida pela função computer_choice
    :return: Função sem retorno
    """
    print(f'Player choice: {player}')
    print(f'Computer choice {computer}')
    print('-=-' * 15)
    result = check_play(player, computer)
    print(result)


def joken_game():
    """
    Valida as entradas do usuário para jogar ou não.
    :return: função sem retorno
    """

    check = False
    while not check:
        answer = str(input('Do you wanna play a round of jo_ken_po? [y/n]: ')).strip().lower()
        is_yes = search("^y(es)?$", answer, IGNORECASE)
        is_no = search("^n(o)?$", answer, IGNORECASE)
        if is_yes or is_no:
            if is_yes:
                play_round()
            else:
                check = confirm_no()
        else:
            print('Please, use only y(es) or n(o) for answer.')


def confirm_no():
    answer = str(input('Are you sure? [y/n]: ')).strip().lower()
    is_yes = search("^y(es)?$", answer, IGNORECASE)
    is_no = search("^n(o)?$", answer, IGNORECASE)
    if is_yes or is_no:
        if is_yes:
            return True
        else:
            return False
    else:
        print('Please, use only y(es) or n(o) for answer.')


def end_game():
    print("*" * 15)
    print('Thank you for playinh!')
    print("*" * 15)


def check_play(player1_choice, player_target):
    if choice_map[player1_choice] == player_target:
        return f'{player1_choice} beats {player_target}. You win!'
    if choice_map[player_target] == player1_choice:
        return f'{player_target} beats {player1_choice}. You loose!'
    return 'We choose the same. Tie.'


choice_map = {"rock": "scissors", "sicssors": "paper", "paper": "rock"}
jaken_options = ["rock", "paper", "scissors"]
joken_game()
