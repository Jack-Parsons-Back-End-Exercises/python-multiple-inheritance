from animals import Ant, BettaFish, Copperhead, Earthworm, Finch, Gerbil, Mouse, Parakeet, Rattlesnake, Terrapin
from environments import diggingEnvironment, flyingEnvironment, swimmingEnvironment, walkingEnvironment

bob = Ant("Bob")
bubbles = BettaFish("Bubbles")
killer = Copperhead("Killer")
jim = Earthworm("Jim")
finch = Finch("Finch")
snickers = Gerbil("Snickers")
jerry = Mouse("Jerry")
flaps = Parakeet("Flaps")
death = Rattlesnake("Death")
terry = Terrapin("Terry")

hills = diggingEnvironment("Hills")
plains = walkingEnvironment("Plains")
lake = swimmingEnvironment("Lake")
aviary = flyingEnvironment("Aviary")

hills.addAnimal(death)
hills.addAnimal(jerry)
hills.addAnimal(jim)
hills.addAnimal(killer)

plains.addAnimal(bob)
plains.addAnimal(snickers)

lake.addAnimal(bubbles)
lake.addAnimal(terry)

aviary.addAnimal(flaps)
aviary.addAnimal(finch)

print("----Animals in Hills----")
print("")
for animal in hills.animals:
    print(animal)

print("")

print("----Animals in Plains----")
print("")
for animal in plains.animals:
    print(animal)

print("")

print("----Animals in Lake----")
print("")
for animal in lake.animals:
    print(animal)

print("")

print("---Animals in Aviary----")
print("")
for animal in aviary.animals:
    print(animal)