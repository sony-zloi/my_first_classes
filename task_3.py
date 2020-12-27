class Stadium:
    """
    Задание 3
    Реализуйте класс «Стадион». Необходимо хранить в полях класса:
    - название стадиона,
    - дату открытия,
    - страну,
    - город,
    - вместимость.
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self):
        self.name = input('Name: ')
        self.year = str(input('Year: '))
        self.country = input('country: ')
        self.city = input('city: ')
        self.capacity = str(input('capacity: '))
    

    def getName(self):
        return self.name

    def setName(self, value):
        if not value:
            raise ValueError
        self.name = value

    def getYear(self):
        return self.year

    def setYear(self, value):
        if not value:
            raise ValueError
        self.year = value

    def getCountry(self):
        return self.country

    def setCountry(self, value):
        if not value:
            raise ValueError
        self.country = value

    def getCity(self):
        return self.city

    def setCity(self, value):
        if not value:
            raise ValueError
        self.city = value

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, value):
        if not value:
            raise ValueError
        self.capacity = value

stad1 = Stadium()

print(stad1)
stad1.setCapacity(90)
print(stad1)
