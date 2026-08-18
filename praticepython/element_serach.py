#used linear search but binary search can also be done...
num=input("Enter the element of the list(sep by ,): ").split(",")
num=[int(i) for i in num]
num=sorted(num)
c=int(input("Enter a digit to check in list: "))
ans="Found"
for i in num:
    if c in num:
        ans="Found"
        break
    ans="Not found"
print(ans)
