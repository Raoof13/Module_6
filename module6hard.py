# Задача "Съедобное, несъедобное"

class Animal:
    def __init__(self, name):
        self.eat()
        self.name = name
        alive = True
        fed = False

class Mammal(Animal):
    def eat(self, food):
            ...

class Predator(Animal):
    def eat(self, food):
            ...


class Plant:
    def __init__(self, name, edible):
        self.eat()
        edible = False
        self.name = name

class Flower(Plant):
    def eat(self, food):
        if food.name:




class Fruit(Plant):
    def eat(self, food):
        edible = True


print(f"{self.name} съел {food.name}")
print(f"{self.name} не стал есть {food.name}")
