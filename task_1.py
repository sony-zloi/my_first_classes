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

    def addData(self):
        self.carProp['name'] = input('Name: ')
        self.carProp['year'] = str(input('Year: '))


nameOfObj1 = Auto()
nameOfObj2 = Auto()
carList = Auto()
carList.showData()
