from .animal import Animal
from movements import Digging

class Copperhead(Animal, Digging):
    def __init__(self, name):
        Animal.__init__(self, name)
        Digging.__init__(self)

    def __str__(self):
        return f'Why the hell do you keep a copperhead snake named {self.name}!?'

    def dig(self):
        print(f'{self.name} the copperhead snake digs')