from movements import Swimming
from .animal import Animal

class BettaFish(Animal, Swimming):
    def __init__(self, name):
        Animal.__init__(self, name)
        Swimming.__init__(self)

    def __str__(self):
        return f'{self.name} the betta fish'

    def swim(self):
        print(f'{self.name} the betta fish swims')