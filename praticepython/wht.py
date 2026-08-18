from collections import Counter

names=[]
with open ("nameslist.txt","r") as f:
    for name in f:
        names.append(name.strip())

print(Counter(names))
