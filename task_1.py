'''
Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''


class Auto:
    carList = []
    counter = 1

    def __init__(self):
        self.name = input('Name: ')
        self.year = str(input('Year: '))
        self.vendor = input('Vendor: ')
        self.value = str(input('Value of engine: '))
        self.color = input('Color: ')
        self.cost = str(input('Cost: '))

        self.carProp = {
            'name': self.name,
            'year': self.year,
            'vendor': self.vendor,
            'value': self.value,
            'color': self.color,
            'cost': self.cost,
        }

        Auto.carList.append(self.carProp)
        Auto.counter += 1

    @staticmethod
    def showData():
        print('Перечень автомобилей и их свойства: ')
        for element in Auto.carList:
            for keys, values in element.items():
                print(keys + ": " + values)
            print('------------')
        print()

    @staticmethod
    def getProp():
        propChoose = ('name', 'year', 'vendor', 'value', 'color', 'cost')
        prop = int(input('Какой из параметров вывести на экран:\n'
                         '1 - Имя: \n'
                         '2 - Год: \n'
                         '3 - Произодителя: \n'
                         '4 - Объем двигателя: \n'
                         '5 - Цвет: \n'
                         '6 - Цену: \n'
                         '> '))
        for element in Auto.carList:
            for keys, values in element.items():
                if keys == propChoose[prop - 1]:
                    print(keys + ": " + values)


def userEnter():
    enter = input('Имеется класс \"Автомобиль\" \n'
                  'Для ввода нажмите 1: \n'
                  'Для вывода нажмите 2: \n'
                  'Для вывода отдельных свойств нажмите 3: \n'
                  'Для выхода нажмите любую другую клавишу:\n'
                  '> ')
    return enter


while True:
    enter = userEnter()

    if enter == '1':
        nameOfObj = 'car_' + str(Auto.counter)
        print(f'Введите параметры автомобиля {nameOfObj} :')
        nameOfObj = Auto()
    elif enter == '2':
        Auto.showData()
    elif enter == '3':
        Auto.getProp()
    else:
        break

print('Bye!')
