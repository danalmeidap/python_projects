def card_isvalid(begin, digits_sums, digit):
    if digits_sums != 0:
        return "INVALID"
    elif digit == 15 and begin in [34, 37]:
        return "AMEX"
    elif digit in [13, 16] and begin in range(40, 50):
        return "VISA"
    elif digit == 16 and begin in range(51, 56):
        return "MASTERCARD"
    else:
        return "INVALID"


def get_int(msg):
    while True:
        try:
            value = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mcredit card number must to be an Integer\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mProgram interrupt\033[m')
            return 0
        else:
            return value


def sum_digits(cred_card):
    aux = cred_card
    digits_total = 0
    sum_digit = 0
    while aux > 0:
        digits_total += 1
        digit = int(aux % 10)
        aux = aux / 10
        if digits_total % 2 == 0:
            digit *= 2
            if digit >= 10:
                digit = 1 + digit % 10
        sum_digit += digit
    sum_digit = sum_digit % 10
    return sum_digit


def digits(cred_card):
    return len(str(cred_card))


def card_begining(cred_card):
    begin = int(cred_card / pow(10, (total_digits - 2)))
    return begin


cc_number = get_int("CC:")

total_digits = digits(cc_number)
digits_sum = sum_digits(cc_number)
begining = card_begining(cc_number)
cards_brand = card_isvalid(begining, digits_sum, total_digits)

print(cards_brand)
