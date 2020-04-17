from .animal import Animal
from movements import Walking, Swimming, Digging

class Terrapin(Animal, Walking, Swimming, Digging):
    def __init__(self, name):
        Animal.__init__(self, name)
        Walking.__init__(self)
        Swimming.__init__(self)
        Digging.__init__(self)

    def __str__(self):
        return f'{self.name} the terrapin'

    def walk(self):
        print(f'{self.name} the terrapin walks')

    def swim(self):
        print(f'{self.name} the terrapin swims')

    def dig(self):
        print(f'{self.name} the terrapin digs')