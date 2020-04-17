from .flower import Flower
from flowerTypes import ValentinesFlower

class Rose(Flower, ValentinesFlower):
    def __init__(self, color):
        Flower.__init__(self)
        ValentinesFlower.__init__(self)
        if color == "red" or color == "pink" or color == "blue":
            self.color = color
        else:
            print(f'We do not offer roses in {color} at this time.')

    def __str__(self):
        return f"Rose, {self.color}"