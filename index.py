from arrangements import MothersDayArrangement, ValentinesArrangement
from flowerTypes import MothersDayFlower, ValentinesFlower
from flowers import Alstroemeria, BabysBreath, Daisy, Lilly, Poppy, Rose 

val_arrangement = ValentinesArrangement()
mom_arrangement = MothersDayArrangement()

alstro = Alstroemeria()
baby = BabysBreath()
daisy = Daisy()
lilly = Lilly()
poppy = Poppy()
red_rose = Rose("red")
pink_rose = Rose("pink")
blue_rose = Rose("blue")

val_arrangement.addFlower(alstro)
val_arrangement.addFlower(lilly)
val_arrangement.addFlower(red_rose)
val_arrangement.addFlower(pink_rose)
val_arrangement.addFlower(blue_rose)

mom_arrangement.addFlower(daisy)
mom_arrangement.addFlower(baby)
mom_arrangement.addFlower(poppy)

print("Mother's Day Flower Arrangement")
print("---------------")
for flower in mom_arrangement.flowers:
    print(flower)

print("")
print("")
print("Valentine's Day Flower Arrangement")
print("---------------")
for flower in val_arrangement.flowers:
    print(flower)