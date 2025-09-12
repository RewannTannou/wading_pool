import random

listOfNumber = []

for i in range(0, 1000000):
    number = random.randint(0, 100)
    listOfNumber.append(number)

listOfNumber = sorted(listOfNumber)
print(listOfNumber)
