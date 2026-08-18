#ny solution...

def triangle():
    l= int(input("lenght of first side: "))
    m= int(input("lenght of second side: "))
    n= int(input("lenght of thrid side: "))
    
    if l==m==n:
        print("Equilateral triangle")
    elif l==m or m==n or l==n:
        print("isosceles triangle")
    elif (l + m ≥ n) or (m + n ≥ l) or (l + n ≥ m):
        print("Degentrate triangle")
    else:
        print("scalene triangle")