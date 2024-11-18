import random

_DEGREE_OF_DANGER = 0

class Animal:
    speed: int
    live = True
    sound = None


    def __init__(self, _cords, speed: int):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):

        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx, dy, dz] * self.speed

    def get_cords(self, dx, dy, dz):
         print(f"X: {dx}, Y: {dy}, Z: {dz}")

    def attack(self):
        if _DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        ...

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"


    def speak(self):
        pass


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()