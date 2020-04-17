from .animal import Animal
from movements import Digging

class Rattlesnake(Animal, Digging):
    def __init__(self, name):
        Animal.__init__(self, name)
        Digging.__init__(self)

    def __str__(self):
        return f'Why the hell do you keep a rattlesnake named {self.name}!?'

    def dig(self):
        print(f'{self.name} the rattlesnake digs')