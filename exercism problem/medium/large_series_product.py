#purely solved bvy mnyself all logica nd everything...

num=int(input("Enter a number: "))
num=str(num)
n=0
digit=[]
jp=[]
while (True):
    if len(num[n:3+n])==2:
        break
    else:
        digit.append(num[n:3+n])
        n+=1
for i in digit:
    total=1
    for char in i:
        total*=int(char)
    jp.append(total)

print(max(jp))

#solution...

"""Largest Series Product."""
import math


def largest_product(series: str, size: int) -> int:
    """Return the largest series product."""
    if size == 0:
        return 1
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if size < 0:
        raise ValueError("span must not be negative")

    numbers = [int(number) for number in series]
    return max(
        math.prod(numbers[start:start + size])
        for start in range(len(series) - size + 1)
    )
