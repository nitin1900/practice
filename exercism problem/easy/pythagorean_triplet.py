#copy-paste from ai...

n = int(input("Enter your number: "))
triplets = []

if n > 1:
    for a in range(1, n // 3):
        for b in range(a + 1, n // 2):
            c = n - a - b

            if a * a + b * b == c * c:
                triplets.append([a, b, c])

print(triplets)

#solution...

def triplets_with_sum(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a**2 + b**2 == c**2 and a + b + c == n:
                    triplets.append([a, b, c])
    return triplets