from re import search, IGNORECASE
from time import sleep


def rolling_dice(dice=1, value=6):
    from random import randint
    cont = 0
    while cont != dice:
        roll_dice = randint(1, value)
        print('Rolling', flush=True)
        sleep(0.5)
        print(roll_dice)
        cont += 1


def value_check(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mPlease insert a valid integer.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return n


def game_start():
    print('Do you want to play dices? ', end='')
    dice_options = (2, 4, 6, 8, 10, 12, 20, 100)
    while True:
        choice = str(input('Choice: ')).strip()
        print("-" * 15)
        # Checks for a valid input from user
        if search("^y(es)?$", choice, IGNORECASE):
            count = 0
            while count != 1:
                # takes the type of dice and how many devices will be played
                type_of_dice = value_check('What kind of dices? ')
                dices = value_check('How many dices? ')
                # checking input
                if type_of_dice in dice_options and dices >= 1:
                    rolling_dice(dices, type_of_dice)
                    count += 1
                else:
                    print('Please, check the values and try again')
            print('Do you want to play again?')
        # Exits when user say  he will not play anymore
        elif search("^n(o)?$", choice, IGNORECASE):
            print('Logging out', flush=True)
            sleep(0.5)
            break
        # Other possibilities
        else:
            print('Please, use only y(es) or n(o) for answer.')


def end_game():
    # Gamer Over
    print("-" * 15)
    print('Thank you for playing.')
    print("-" * 15)
    print('GAME OVER!')
