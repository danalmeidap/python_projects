from time import sleep
from re import search, IGNORECASE


def value_check(msg):
    """
    Verify inputs value for only acept an integer
    :param msg: text who will be show on the screen
    :return: an intenger value
    """
    while True:
        try:
            value = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mPlease insert a valid integer.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return value


def rolling_dice(dices=1, minimum=1, maximum=2):
    from random import randint
    cont = 0
    while cont != dices:
        roll_dice = randint(minimum, maximum)
        print('Rolling', flush=True)
        sleep(0.5)
        print(roll_dice)
        cont += 1


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


class DiceSimulator:
    def __init__(self):
        self.minimum = 1
        self.maximum = None
        self.message = 'Do you want to play dices? '

    def rolling(self):
        check = False
        print(self.message, end='')
        while not check:
            choice = str(input('Choice: ')).strip()
            print("-" * 15)
            # Checks for a valid input from user
            is_yes = search("^y(es)?$", choice, IGNORECASE)
            is_no = search("^n(o)?$", choice, IGNORECASE)
            if is_yes or is_no:
                if is_yes:
                    self.roll()
                    print('Do you want to play again?')
                else:
                    check = confirm_no()

    def roll(self):
        count = 0
        while count != 1:
            dices = value_check("how many dices: ")
            self.maximum = value_check('What kind of dices: ')
            # checking input
            if self.maximum in dice_options and dices >= 1:
                rolling_dice(dices, self.minimum, self.maximum)  # Rolling the dice
                count += 1
            else:
                print('Please, check the values and try again')


dice_options = (2, 4, 6, 8, 10, 12, 20, 100)
