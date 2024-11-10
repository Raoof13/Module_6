# Задача "Изменять нельзя получать"

class Vehicle:
    def __init__(self):
        self.owner = str
        self.__model = str
        self.__engine_power = int
        self.__color = str
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self, name):
        self.name = name
        return print(f'Модель {self.name}')

    def get_horsepower(self):
        pass

    def get_color(self):
        pass

    def print_info(self):
        pass

class Sedan(Vehicle):
    pass



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()