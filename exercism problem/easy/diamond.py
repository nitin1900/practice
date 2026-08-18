#gemini gave me blueprint how to do this and duck ai i searched
#the index and reversed part
#new to me

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
target=input("Enter a alphabet: ").upper()
target_index=alpha.index(target)

top_half=[]
for q in range(0,target_index+1):
    current_letter=alpha[q]
    outer_space=target_index-q
    inner_space=(q*2)-1
    if q==0:
        row=(" " * outer_space) + "A" + (" " * outer_space) #corrected
        top_half.append(row)
    else:
        rows = (" " * outer_space) + current_letter + (" " * inner_space) + current_letter + (" " * outer_space)
        #corrected 👆
        top_half.append(rows)
mirror=list(reversed(top_half[:-1])) #corrected
print("\n".join(top_half + mirror)) #corrected

#solution...

from typing import List


def rows(letter: str) -> List[str]:
    letters = [chr(k) for k in range(ord('A'), ord(letter) + 1)]
    alphabet = letters[:-1] + letters[::-1]
    diamond_line = letters[::-1] + letters[1:]
    return [''.join(x if x == y else ' ' for y in diamond_line) for x in alphabet]