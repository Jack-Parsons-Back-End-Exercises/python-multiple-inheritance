from .arrangement import Arrangement

class ValentinesArrangement(Arrangement):
    def __init__(self):
        super().__init__()

    def addFlower(self, flower):
        if flower.isOrganic == False:
            self.flowers.append(flower)
        else:
            print(f'{flower} cannot be added to this arrangement.')