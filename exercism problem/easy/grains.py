#my code:

try:
    square = int(input("Number of squares: "))
except ValueError:
    print("enter valid number")
grains = 1
i = 1

while i < square:
    grains *= 2
    i += 1

print(grains)


#community code:

def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    return 1 << number - 1


def total():
    return (1 << 64) - 1