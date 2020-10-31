import random

def genArray(size, maxValue):
    array = []
    for n in range(0,size):
        array.append((random.randint(0, maxValue)))
    return array