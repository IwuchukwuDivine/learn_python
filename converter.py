import random


def kg_to_lbs(weight):
    return weight * 2.2


def lbs_to_kg(weight):
    return weight / 2.2


class Dice:
    def roll(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        return dice_1, dice_2


dice = Dice()
print(dice.roll())
