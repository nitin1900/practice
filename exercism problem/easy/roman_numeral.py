#my code...
#logic given by gemini and most of works done with help of gemini...
#new to me(Greedy Algorithm)
roman_values = [
    (1000, "M"),
    (900, "CM"), # We treat the exceptions as their own specific "bills"(by gemini)
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

try:
    user = int(input("Enter a number: "))
except:
    print("Enter a valid number")
    exit()
result=""
if 0<user<=3999:
    for value,letter in roman_values:
        while user>=value:
            result+=letter
            user-=value
else:
    print("Enter number between 1 to 3999")
print(result)





#solution...




ROMAN = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def roman(number: int) -> str:
    result = ''
    while number:
        for arabic in ROMAN.keys():
            if number >= arabic: 
                result += ROMAN[arabic]
                number -= arabic
                break
    return result