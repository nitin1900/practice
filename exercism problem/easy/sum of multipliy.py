#done some silly mistake but i did it...

level=int(input("what is your level: "))
magical_item=input("magical item found: ").split(",")
my_set=set()
total=0
for i in magical_item:
    for j in range(level):
        if j%int(i)==0:
            my_set.add(j)
for k in my_set:
    total=total+k
print(total)


#solution...

def sum_of_multiples(limit, numbers):
    return sum(
        {
            i
            for n in numbers if n
            for i in range(n, limit, n)
        }
    )