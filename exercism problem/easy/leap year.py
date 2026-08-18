#my code

y=int(input("year: "))
if (y%400==0) or (y%100!=0 and y%4==0):
    print("Leap year")
else:
    print("Not leap year")
    
    
#solution in site

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)