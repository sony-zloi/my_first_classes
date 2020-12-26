class Book:
    """
    Задание 2
    Реализуйте класс «Книга». Необходимо хранить в полях класса:
    - название книги
    - год выпуска
    - издателя,
    - жанр
    - автора,
    - цену
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self):
        self.name = input('Name: ')
        self.year = str(input('Year: '))
        self.publisher = input('Publisher: ')
        self.genre = input('Genre: ')
        self.author = input('Author: ')
        self.cost = str(input('Cost: '))

    def __repr__(self):
        return f'name: {self.name} year: {self.year} publisher: {self.publisher} genre: {self.genre} ' \
               f'author: {self.author} cost: {self.cost}'

    def __str__(self):
        return f'name: {self.name} year: {self.year} publisher: {self.publisher} genre: {self.genre} ' \
               f'author: {self.author} cost: {self.cost} '

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

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, value):
        if not value:
            raise ValueError
        self.publisher = value

    def getGenre(self):
        return self.genre

    def setGenre(self, value):
        if not value:
            raise ValueError
        self.genre = value

    def getAuthor(self):
        return self.author

    def setAuthor(self, value):
        if not value:
            raise ValueError
        self.author = value

    def getCost(self):
        return self.cost

    def setCost(self, value):
        if not value:
            raise ValueError
        self.cost = value
