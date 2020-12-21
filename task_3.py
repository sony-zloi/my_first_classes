'''
Задание 3
Реализуйте класс «Стадион». Необходимо хранить в полях класса:
- название стадиона,
- дату открытия,
- страну,
- город,
- вместимость.
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''


class Stadium:
    stadiumList = []

    def __init__(self):
        self.name = input('Name: ')
        self.year = str(input('Year: '))
        self.country = input('country: ')
        self.city = input('city: ')
        self.capacity = str(input('capacity: '))

        self.stadiumProp = {
            'name': self.name,
            'year': self.year,
            'country': self.country,
            'city': self.city,
            'capacity': self.capacity,
        }

        Stadium.stadiumList.append(self.stadiumProp)

    @staticmethod
    def showData():
        print('Перечень стадионов и их свойства: ')
        for element in Stadium.stadiumList:
            for keys, values in element.items():
                print(keys + ": " + values)
            print('------------')
        print()

    @staticmethod
    def getProp():
        propChoose = ['name', 'year', 'country', 'city', 'capacity']
        prop = int(input('Какой из параметров вывести на экран:\n'
                         '1 - Имя: \n'
                         '2 - Год: \n'
                         '3 - Страну: \n'
                         '4 - Город: \n'
                         '5 - Вместимость: \n'
                         '> '))
        for element in Stadium.stadiumList:
            for keys, values in element.items():
                if keys == propChoose[prop - 1]:
                    print(keys + ": " + values)


def userEnter():
    enter = input('Имеется класс \"Cтадионы\" \n'
                  'Для ввода стадиона нажмите - 1: \n'
                  'Для вывода списка стадионов нажмите - 2: \n'
                  'Для вывода отдельных параметров стадиона нажмите -  3: \n'
                  'Для выхода нажмите любую другую клавишу:\n'
                  '> ')
    return enter

counter = 0

while True:
    enter = userEnter()

    if enter == '1':
        counter += 1
        nameOfObj = 'stadium' + str(counter)
        print(f'Введите параметры стадиона {nameOfObj} :')
        nameOfObj = Stadium()
    elif enter == '2':
        Stadium.showData()
    elif enter == '3':
        Stadium.getProp()
    else:
        break

print('Bye!')
