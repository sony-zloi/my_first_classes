'''
Задание 2
Реализуйте класс «Книга». Необходимо хранить в полях класса:
- название книги
- год выпуска
- издателя,
- жанр
- автора,
- цену
Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''

class Book:
    bookList = []

    def __init__(self):
        name = input('Name: ')
        year = str(input('Year: '))
        publisher = input('Publisher: ')
        genre = str(input('Genre: '))
        autor = input('Autor: ')
        cost = str(input('Cost: '))

        self.bookProp = {
            'name': name,
            'year': year,
            'publisher': publisher,
            'genre': genre,
            'autor': autor,
            'cost': cost,
        }

        Book.bookList.append(self.bookProp)

    @staticmethod
    def showData():
        print('Перечень автомобилей и их свойства: ')
        for element in Book.bookList:
            for keys, values in element.items():
                print(keys + ": " + values)
            print('------------')
        print()

    @staticmethod
    def getProp():
        propChoose = ['name', 'year', 'publisher', 'genre', 'autor', 'cost']
        prop = int(input('Какой из параметров вывести на экран:\n'
                         '1 - Имя: \n'
                         '2 - Год: \n'
                         '3 - Издателя: \n'
                         '4 - Жанр: \n'
                         '5 - Автор: \n'
                         '6 - Цену: \n'
                         '> '))
        for element in Book.bookList:
            for keys, genres in element.items():
                if keys == propChoose[prop - 1]:
                    print(keys + ": " + genres)


def userEnter():
    enter = input('Имеется класс \"Книги\" \n'
                  'Для ввода книги нажмите - 1: \n'
                  'Для вывода списка книг нажмите - 2: \n'
                  'Для вывода отдельных параметров книг нажмите -  3: \n'
                  'Для выхода нажмите любую другую клавишу:\n'
                  '> ')
    return enter

counter = 0

while True:
    enter = userEnter()

    if enter == '1':
        counter += 1
        nameOfObj = 'book' + str(counter)
        print(f'Введите параметры книги {nameOfObj} :')
        nameOfObj = Book()
    elif enter == '2':
        Book.showData()
    elif enter == '3':
        Book.getProp()
    else:
        break

print('Bye!')

