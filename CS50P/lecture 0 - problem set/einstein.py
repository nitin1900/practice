#my fav fromula-done some silly mistake but completed!!

def main():
    mass=int(input("what is the mass of body? "))
    c=300000000
    energy= mass*square(c)
    print(f"the energy of the given mass is:{energy}")

def square(n):
    return n*n
    
main()