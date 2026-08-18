import random
import string
alpha = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}

beta = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

msg=input("Enter your message: ")
key=input("Enter your key(alpahbet only and no space): ")
shift=[]
if key.isalpha():
    for char in key:
        shift.append(beta[char])
elif key=="": #just copy-pasted from glm-5 turbo...
    key = ''.join(random.choices(string.ascii_lowercase, k=input("what is the lenght of key: ")))

cipher = "" #stuggled from here and just copy-pasted code from chatgpt...

for i in range(len(msg)):
    if msg[i].isalpha():
        s = shift[i % len(shift)]
        new_val = (beta[msg[i]] + s) % 26
        cipher += alpha[new_val]
    else:
        cipher += msg[i]

print(cipher)

#solution...

import random
from string import ascii_lowercase as letters
from itertools import cycle


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(random.choice(letters) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            encoded.append(letters[(ord(ch1) % 97 + ord(ch2) % 97) % 26])
        return "".join(encoded)

    def decode(self, text):
        decoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            decoded.append(letters[(ord(ch1) % 97 - ord(ch2) % 97) % 26])
        return "".join(decoded)
