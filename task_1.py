'''
Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''


class Auto:
    carList = []

    def __init__(self):
        name = input('Name: ')
        year = str(input('Year: '))
        vendor = input('Vendor: ')
        value = str(input('Value of engine: '))
        color = input('Color: ')
        cost = str(input('Cost: '))

        self.carProp = {
            'name': name,
            'year': year,
            'vendor': vendor,
            'value': value,
            'color': color,
            'cost': cost,
        }

        Auto.carList.append(self.carProp)

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
        propChoose = ['name', 'year', 'vendor', 'value', 'color', 'cost']
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

counter = 0

while True:
    enter = userEnter()

    if enter == '1':
        counter += 1
        nameOfObj = 'car' + str(counter)
        print(f'Введите параметры автомобиля {nameOfObj} :')
        nameOfObj = Auto()
    elif enter == '2':
        Auto.showData()
    elif enter == '3':
        Auto.getProp()
    else:
        break

print('Bye!')
