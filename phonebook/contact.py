class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, Name):
        self.__name = Name.title().strip()

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, Number):
        self.__number = Number

    def save_contact(self, phonebook):
        with open(phonebook, "w") as file:
            file.write(f'{self.name},')
            file.write(f'{self.number}' + '\n')

    @staticmethod
    def separate_information(line):
        separator = line.split(',')
        contact = Contact(separator[0], separator[1])
        return contact

    def __repr__(self):
        return f'{self.name:8},    {self.number:6} '

    def __str__(self):
        return self.__repr__()
