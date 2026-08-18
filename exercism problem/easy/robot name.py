#copy-paste the logic from duck ai and condition from gemini...

import random
import string

x=int(input("Enter number of names: "))
random_name=set()
while len(random_name)<x:
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=3))
    random_name.add(letters + numbers)
print(random_name)

#solution:

from itertools import product
from random import shuffle
from string import ascii_uppercase as letters

letter_pairs = (''.join(p) for p in product(letters, letters))
numbers = (str(i).zfill(3) for i in range(1000))
names = [l + n for l, n in product(letter_pairs, numbers)]
shuffle(names)
NAMES = iter(names)
class Robot(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.name = next(NAMES)