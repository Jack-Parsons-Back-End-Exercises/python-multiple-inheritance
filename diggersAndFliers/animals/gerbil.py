from movements import Walking, Digging
from .animal import Animal

class Gerbil(Animal, Walking, Digging):
    def __init__(self, name):
        Animal.__init__(self, name)
        Walking.__init__(self)
        Digging.__init__(self)

    def __str__(self):
        return f'{self.name} the gerbil'

    def dig(self):
        print(f'{self.name} the gerbil digs')

    def walk(self):
        print(f'{self.name} the gerbil walks')