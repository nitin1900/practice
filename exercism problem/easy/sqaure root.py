#made some silly mistake in range function but solved it...

target=int(input("Enter a number: "))
k=0
for i in range(0,target+1):
    if i**2==target:
        k=k+i
        break

if k==0:
    print("Square root not found")
else:
    print(f"Sqaure root is {k}")


#solution...

def square_root(number):
    return number ** 0.5