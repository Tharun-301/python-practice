from datetime import date

class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.__first_name = first_name
        self.__last_name = last_name
        self.birth_year = birth_year

    @property 
    def name(self):
        return f"{self.__first_name} {self.__last_name}"

    @name.setter
    def name(self, name):
        names = name.strip().split()
        if len(names) != 2: 
            raise ValueError("Full name must include first and last name.")
        self.__first_name, self.__last_name = names

    @property 
    def age(self):   
        current_year = date.today().year
        return current_year - self.birth_year


if __name__ == "__main__":
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    birth_year = int(input('Enter birth year: '))

    p = Person(first_name, last_name, birth_year)

    print("---Personal Details---")
    print("Full Name:",p.name)
    print("Age:",p.age)