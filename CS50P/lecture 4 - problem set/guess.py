#made some silly mistakes...

import random

while True:
    try:
        l=int(input("Level: "))
        if 0<l:
            break
        elif l<=0:
            print("Level are always after 0")
            continue
    except:
        print("Enter valid number")

r=random.randint(1,l)

while True:
    try:
        g=int(input("Guess: "))
        if g<=0:
            print("invalid number")
            continue
        if g<r:
            print("Think big for correct guess")
            continue
        elif g>r:
            print("You are very high")
            continue
        elif g==r:
            print("You guess correct")
            break
    except ValueError:
        print("Enter valid number")