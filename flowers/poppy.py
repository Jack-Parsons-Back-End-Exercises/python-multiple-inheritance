from .flower import Flower
from flowerTypes import MothersDayFlower

class Poppy(Flower, MothersDayFlower):
    def __init__(self):
        Flower.__init__(self)
        MothersDayFlower.__init__(self)

    def __str__(self):
        return "Poppy"