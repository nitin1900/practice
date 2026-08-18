#my code...

user=list(input("Enter words with space: ").split(" "))
for i in range(len(user)-1):  # suggest by glm-5 small error to prevent indexerror 
    print(f"For want of a {user[i]} the {user[i+1]} was lost.")

#solution...

from itertools import pairwise

def proverb(*lst, qualifier):
    """Produce the proverb."""
    res = [f"For want of a {a} the {b} was lost." for a, b in pairwise(lst)]
    
    # Add the ending
    if lst:
        q_phrase = f"{qualifier} " if qualifier else ""
        res.append(f"And all for the want of a {q_phrase}{lst[0]}.")
    
    return res