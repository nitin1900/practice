#my code...

n=int(input("Enter a number: "))
if n%3==0:
    print("Pling",end="")
if n%5==0:
    print("Plang",end="")
if n%7==0:
    print("Plong",end="")
elif n%3!=0 and n%5!=0 and n%7!=0:
    print(f"{n}")


#solution given...

def convert(num):
    sounds = ''
    
    if num % 3 == 0: sounds += 'Pling'
    if num % 5 == 0: sounds += 'Plang'
    if num % 7 == 0: sounds += 'Plong'
        
    return sounds if sounds else str(num)