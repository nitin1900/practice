#my code...

import string

code={
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 
    'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 
    'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 
    'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
}
user=input("enter a word or sentence: ").lower()
final=""
for i in user:
    if i in code:
        final=final+code[i]
    elif i.isalnum():
        final=final+i

chunks = [final[i:i+5] for i in range(0, len(final), 5)]
output = " ".join(chunks)

print(output)


#solution...

rom string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(text: str):
    res = "".join(chr for chr in text.lower() if chr.isalnum()).translate(ENCODING)
    return " ".join(res[index:index+5] for index in range(0, len(res), 5))

def decode(text: str):
    return "".join(chr.lower() for chr in text if chr.isalnum()).translate(ENCODING)
