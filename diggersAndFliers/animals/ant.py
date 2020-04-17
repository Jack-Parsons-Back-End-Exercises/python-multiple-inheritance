from movements import Walking
from .animal import Animal

class Ant(Animal, Walking):
    def __init__(self, name):
        Animal.__init__(self, name)
        Walking.__init__(self)

    def __str__(self):
        return f'{self.name} the Ant'

    def walk(self):
        print(f'{self.name} the ant walks')