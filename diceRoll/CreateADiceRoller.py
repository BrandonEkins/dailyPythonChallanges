from random import randint

output = []
with open("input.txt", "r") as file:
    file = file.readlines()
    for line in file:
        dice = []
        line = line.split("d")
        for i in range(int(line[0])):
            dice.append(randint(0,int(line[1])))
        dice.insert(0,sum(dice))
        output.append(dice)

print(output)

