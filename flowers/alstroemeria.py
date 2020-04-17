from .flower import Flower
from flowerTypes import ValentinesFlower

class Alstroemeria(Flower, ValentinesFlower):
    def __init__(self):
        Flower.__init__(self)
        ValentinesFlower.__init__(self)

    def __str__(self):
        return "Alstroemeria"