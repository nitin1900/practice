#done by myself...

user=int(input("Enter a number: "))
p=2
total=1
k=[]
while user/p!=1:
    if user%p==0:
        k.append(p)
        total=total*p
        user=user/p
    else:
        p+=1
k.append(int(user))
print(f"Prime numbers are {k}")
print(f"product of total prime number is {total*(int(user))}")

#solution...

import math
import itertools


def factors(value: int) -> list[int]:
    """Return a list of the prime factors of n."""
    prime_factors = []
    quotient = value
    limit = math.isqrt(quotient) + 1

    # range over (2, 3, 5, 7, .... limit)
    for factor in itertools.chain([2], range(3, limit, 2)):
        if factor > limit:
            break
        # Do we have a new divisor?
        while quotient % factor == 0:
            prime_factors.append(factor)
            quotient = quotient // factor
            limit = math.isqrt(quotient) + 1

    if quotient != 1:
        # quotient is prime: add to our list of prime divisors
        prime_factors.append(quotient)

    return prime_factors