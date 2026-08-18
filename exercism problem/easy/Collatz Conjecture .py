#my code...
try:
    n=int(input("Enter a number: "))
except:
    print("Enter valid number")
i=0
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=(n*3)+1
    i=i+1
print(i)


#solution by website...

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        counter += 1
    return counter