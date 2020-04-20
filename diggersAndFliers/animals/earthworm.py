from .animal import Animal
from movements import Digging

class Earthworm(Animal, Digging):
    def __init__(self, name):
        Animal.__init__(self, name)
        Digging.__init__(self)

    def __str__(self):
        return f'{self.name} the earthworm'

    def swim(self):
        print(f'{self.name} the earthworm digs')