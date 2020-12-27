class Car:
    """
    Задание 1
    Реализуйте класс «Автомобиль». Необходимо хранить
    в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
    методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self):
        self.name = input('Name: ')
        self.year = str(input('Year: '))
        self.vendor = input('Vendor: ')
        self.power = str(input('Power of engine: '))
        self.color = input('Color: ')
        self.cost = str(input('Cost: '))

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

    def getVendor(self):
        return self.vendor

    def setVendor(self, value):
        if not value:
            raise ValueError
        self.vendor = value

    def getPower(self):
        return self.power

    def setPower(self, value):
        if not value:
            raise ValueError
        self.power = value

    def getColor(self):
        return self.color

    def setColor(self, value):
        if not value:
            raise ValueError
        self.color = value

    def getCost(self):
        return self.cost

    def setCost(self, value):
        if not value:
            raise ValueError
        self.cost = value

car1 = Car()
