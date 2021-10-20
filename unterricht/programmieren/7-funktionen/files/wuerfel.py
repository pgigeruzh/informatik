from random import random

def wuerfle():
    zufallszahl = random()
    if zufallszahl < (1/6):
        return 1
    elif zufallszahl < (2/6):
        return 2
    elif zufallszahl < (3/6):
        return 3
    elif zufallszahl < (4/6):
        return 4
    elif zufallszahl < (5/6):
        return 5
    elif zufallszahl < (6/6):
        return 6

for i in range(5):
    print(wuerfle())

print("...")