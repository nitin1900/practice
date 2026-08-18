#my code...

import random
dice=[]
while len(dice)<5:
    dice.append(random.randint(1,6))
print(dice)
choice=input("choose you category: ").lower()
total=0
if choice=="one":
    total=1*dice.count(1)
    print(total)
elif choice=="two":
    total=2*dice.count(2)
    print(total)
elif choice=="three":
    total=3*dice.count(3)
    print(total)
elif choice=="four":
    total=4*dice.count(4)
    print(total)
elif choice=="five":
    total=5*dice.count(5)
    print(total)
elif choice=="six":
    total=6*dice.count(6)
    print(total)
elif choice=="full house":
    house=[]
    for number in set(dice):
        frequency = dice.count(number)
        if frequency == 2:
            house.append(2)
        elif frequency == 3:
            house.append(3)
    if house==[2,3] or house==[3,2]:
        for i in dice:
            total = total+int(i)
    print(total)
elif choice=="four of a kind":
    for number in set(dice):
        frequency=dice.count(number)
        if frequency>=4:
            total=number*4
    print(total)
elif choice=="straight":
    new=set()
    for i in dice:
        new.add(i)
    new=sorted(new)
    if new==[1,2,3,4,5] or new==[2,3,4,5,6]:
        total+=30
    print(total)
elif choice=="yacht":
    if len(set(dice))==1:
        total+=50
    print(total)
elif choice=="choice":
    for i in dice:
        total=total+i
    print(total)
else:
    print("Ivalid category")

#solution...

def digits(num):
    return lambda dice: dice.count(num) * num
YACHT = lambda dice: 50 if dice.count(dice[0]) == len(dice) else 0
ONES = digits(1)
TWOS = digits(2)
THREES = digits(3)
FOURS = digits(4)
FIVES = digits(5)
SIXES = digits(6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else 0
FOUR_OF_A_KIND = lambda dice: 4 * dice[1] if dice[0] == dice[3] or dice[1] == dice[4] else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum
def score(dice, category):
    return category(dice)