#my code...

import random
abilities=["strength","dexterity","constitution","intelligence","wisdom","charisma"]

def total():
    k=[]
    n=0
    while len(k)<4:
        k.append(random.randint(1,6))
    k.remove(min(k))
    for j in k:
        n=n+j
    return n

score=[]
for i in range(len(abilities)):
    score.append(total())

power=dict(zip(abilities,score))

modifier=(power["constitution"]-10)//2
health=modifier+10

for i in power:
    print(i,power[i],sep=": ")
print(f"constitution modifier: {modifier}")
print(f"Hit points: {health}")

#solution:

import random

ABILITIES = (
    'strength', 'dexterity', 'constitution',
    'intelligence', 'wisdom', 'charisma')


def modifier(score):
    return (score - 10) // 2


class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dices = sorted(random.randint(1, 6) for _ in range(4))
        return sum(dices[1:])