import operations
import os.path

my_phonebook = operations.phonebook
valid_options = range(0, 5)
if(os.path.isfile(f'{my_phonebook.default_file}')):
  operations.load_phonebook(my_phonebook)
option = operations.menu()

while option in valid_options:
    if option == 1:
        operations.add_contact(my_phonebook)
    if option == 2:
        operations.show_phonebook(my_phonebook)
    if option == 3:
        operations.save_contacts(my_phonebook)
    if option == 4:
        operations.cls()
    if option == 0:
        break
    option = operations.menu()
