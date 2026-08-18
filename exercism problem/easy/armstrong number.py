#my code...

n=[]
n=input("Enter a number: ")
l=len(n)
total=0
for i in n:
    total=total+int(i)**l
if int(n)==total:
    print("Armstrong number")
else:
    print("Not armstrong number")


#top comment ans...

def is_armstrong_number(number):
    s = str(number)
    l = len(s)
    total = sum([int(i)**l for i in s])
    return number == total