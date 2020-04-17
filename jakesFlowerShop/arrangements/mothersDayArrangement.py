from .arrangement import Arrangement

class MothersDayArrangement(Arrangement):
    def __init__(self):
        super().__init__()

    def addFlower(self, flower):
        if flower.isOrganic == True:
            self.flowers.append(flower)
        else:
            print(f'{flower} cannot be added to this arrangement.')