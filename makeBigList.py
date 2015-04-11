import random
def makeBigList(size):
    thelist =[]
    for i in range (0,size):
        thelist.append(random.randint(0,size))
    return thelist
    
