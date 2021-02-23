from random import randint


def chosen_number():
  return randint(1,100)


def isequal(number1, number2):
  return number1 == number2


def validate_shot(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mPlease! insert a valid integer.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mInterrupted by user\033[m')
            return 0
        else:
            return n 


def how_many_attempts():
  number = chosen_number()
  attempt_count = 0
  while True:
    shot =validate_shot('shot: ')
    if isequal(shot, number):
      print('Congratulations! You win!')
      break
    else:
      if shot < number:
        print('My number is bibber then yours. Try again!')
      else:
        print('Your number is bigger then mine. Try again!')
      attempt_count += 1
  return attempt_count
