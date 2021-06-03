from phonebook import Phonebook
from contact import Contact
import os


def cls():
    print("\n" * os.get_terminal_size().lines)


def check_str(msg):
    while True:
        try:
            value = str(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mThe value must be valid\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return value


def check_int(msg):
    while True:
        try:
            value = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mThe value must be valid\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUser Interrupt;\033[m')
            return 0
        else:
            return value


def valid_number(number):
    number = str(number)
    formated_number = number
    valid_options = (8, 9, 10)
    while len(number) not in valid_options:
        print("Please check the number")
        number = check_int("Number: ")
        number = str(number)
    if len(number) == 8 and number[0] != "8" or "9":
        formated_number = f"{number[0:4]}-{number[4:]}"
    else:
        if len(number) == 8:
            formated_number = f"9-{number[0:4]}-{number[4:]}"
        elif len(number) == 9:
            formated_number = f"{number[0]}-{number[1:5]}-{number[5:]}"
        elif len(number) == 10:
            formated_number = f"({number[0:2]}){number[2]}-{number[3:7]}-{number[7:]}"
    new_number = formated_number
    return new_number


def menu():
    print('1- Add contact')
    print('2- Show phonebook')
    print('3- Save')
    print('4- Clear screen')
    print('0- Quit')
    return int(input("Option: "))


def add_contact(book):
    name = check_str("Name: ")
    number = check_int("Number: ")
    number = valid_number(number)
    contact = Contact(name, number)
    book.add_contact(contact)
    print(f"{name} is on the list")


def save_contacts(book):
    book.save_contacts()
    if len(book.contact_list) != 0:
        print("Contacts are save")
    else:
        print("There's no contacts to save")


def show_phonebook(book):
    print(book.show_phonebook(book))

def load_phonebook(book):
  book.open_phonebook(book)
  
phonebook = Phonebook()
