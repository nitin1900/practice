#copy-pasted from chatgpt...(although i was having some basic logic...)

rows = list(input("Enter rows as row1,row2: ").split(","))

max_len = max(len(r) for r in rows)

for i in range(max_len):
    for r in rows:
        if i < len(r):
            print(r[i], end=" ")
        else:
            print(" ", end=" ")
    print()

#solution...

import itertools

def transpose(s):
    a = itertools.zip_longest(*s.splitlines(), fillvalue='$')
    return '\n'.join(''.join(w).rstrip('$').replace('$', ' ') for w in a)