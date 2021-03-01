from dices import DiceSimulator, end_game

dice = DiceSimulator()
try:
    dice.rolling()
finally:
    end_game()

