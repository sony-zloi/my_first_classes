class Auto:
    carList = []

    def __init__(self):
        name = input('Name: ')
        year = str(input('Year: '))

        self.carProp = {
            'name': name,
            'year': year,
        }

        Auto.carList.append(self.carProp)

    @staticmethod
    def showData():
        print(f'The properties of the car are: ')
        for element in Auto.carList:
            for keys, values in element.items():
                print(keys + ": " + values)
            print()


def userEnter():
    enter = input('Имеется класс \"Автомобиль\" \n'
                  'Для ввода нажмите 1: \n'
                  'Для вывода нажмте 2: \n'
                  'Для выхода нажмите любую другую клавишу:\n'
                  '> ')
    return enter


while True:
    counter = 0
    enter = userEnter()

    if enter == '1':
        counter += 1
        nameOfObj = 'car' + str(counter)
        print(f'Enter the {nameOfObj} properties:')
        nameOfObj = Auto()

    elif enter == '2':
        Auto.showData()
    else:
        break

print('Bye!')
