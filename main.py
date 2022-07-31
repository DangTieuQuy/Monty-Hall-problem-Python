import random
from numpy import double

def carLocation(): #The location of the door containing the car
    return (random.randint(1, 3))

def doorOpenedByMontyHall(car,initialSelection): #Open a door that does not contain vehicles and is different from the player's choice
    x=random.randint(1,3)
    while x == car or x==initialSelection:
        x=random.randint(1,3)
    return x

def A(n): #Odds of winning if you DO NOT choose to change doors
    x=double(0)
    for a in range(n):
        if random.randint(1,3) == carLocation():
            x=x+1
    return x/n

def B(n): #Odds of winning if you DO NOT choose to change doors
    x=double(0)
    for a in range (n):
        car=carLocation()
        initialSelection=random.randint(1,3)
        selectionAfterChange=random.randint(1,3)
        while selectionAfterChange == initialSelection or selectionAfterChange == doorOpenedByMontyHall(car,initialSelection):
            selectionAfterChange=random.randint(1,3)
        if selectionAfterChange == car:
            x=x+1
    return x/n

print ('Use the law of large numbers to solve the Monty Hall problem')
print ('Enter number of attempts')
n=int(input())
print ('Odds of winning if you DO NOT choose to change doors' , A(n))
print ('Odds of winning if you choose to change doors' , B(n))
