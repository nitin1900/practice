#copy-paste from ai...

number = int(input("Find prime numbers till: "))
pn = []

for i in range(2, number + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        pn.append(i)

print(pn)

#solution...

def primes(number):
    not_prime = []
    prime = []
    
    for item in range(2, number+1):
        if item not in not_prime:
            prime.append(item) 
            for element in range(item*item, number+1, item):
                not_prime.append(element)
    
    return prime