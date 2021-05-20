from contact import Contact


class Phonebook:
    def __init__(self, default_file="phonebook.txt"):
        self.contact_list = []
        self.default_file = default_file

    @property
    def default_file(self):
        return self.__default_file

    @default_file.setter
    def default_file(self, file):
        try:
            name, extension = file.split('.')
            if extension != "txt":
                print("Use only a txt file")
                raise SystemExit()
        except FileNotFoundError:
            print("File does not exist")
        self.__default_file = file

    def check_phonebook(self):
        try:
            with open(self.default_file, 'r') as file:
                if file:
                    return True
        except FileNotFoundError:
            return False
        except IOError:
            return False

    @staticmethod
    def create_phonebook(self):
        if self.check_phonebook(self.default_file):
            return "Phonebook Already exists"
        with open(self.default_file, 'w') as file:
            if file:
                return "Phonebook created"

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def save_contacts(self):
        try:
            with open(self.default_file, 'a') as file:
                if file.writable():
                    for contact in self.contact_list:
                        file.write(contact.__repr__() + "\n")
        except FileNotFoundError:
            return "File does not exist"

    def open_phonebook(self):
        try:
            with open(self.default_file, 'r') as file:
                if file.readible():
                    contacts = 0
                    for line in file.readlines():
                        self.contact_list.append(Contact.separate_information(line.rstrip()))
                        contacts += 1
                print(f'{contacts} are found on file')
        except FileNotFoundError:
            return "File does not exist"

    def __repr__(self):
        if len(self.contact_list) == 0:
            return "No contacts in the list"
        else:
            representation = "Contact List"
            representation += "\n--------------------------------------"
            for contact in self.contact_list:
                representation += "\n" + f'{contact.__str__()}'
            representation += "\n--------------------------------------"
            return representation

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def show_phonebook(phonebook):
        return phonebook.__str__()
