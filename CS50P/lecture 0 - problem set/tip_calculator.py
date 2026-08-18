#got some confusion but it was easy no doubt

def main():
    dollar=dfloat(input("how much was the meal? "))
    percent=pfloat(input("what percentage would you like to tip? "))
    tip=dollar*percent
    print(f"Leave tip ${tip:.2f}")
    
def dfloat(d):
    return float(d)
    
def pfloat(p):
    return float(p)/100
    
main()