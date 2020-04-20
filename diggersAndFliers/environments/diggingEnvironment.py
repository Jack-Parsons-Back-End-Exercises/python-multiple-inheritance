class diggingEnvironment:
    def __init__(self, name):
        self.name = name
        self.animals = set()

    def addAnimal(self, animal):
        if animal.digSpeed > -1:
            self.animals.add(animal)
        else:
            print(f'This animal cannot be added to this environment')