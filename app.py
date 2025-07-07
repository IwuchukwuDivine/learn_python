# weight converter
weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")

if unit.lower() == "l":
    converted = round(weight * 0.45)
    print(f"you are {converted} kilos")
else:
    converted = round(weight / 0.45)
    print(f"you are {converted} pounds")

# guessing game with max of 4 trials
num_of_trials = 0

while num_of_trials < 4:
    guess = int(input("guess: "))
    if guess == 9:
        print("you won!")
        break
    num_of_trials += 1
else:
    print("you lost!")
