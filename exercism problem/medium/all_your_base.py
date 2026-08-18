#my code...

user=int(input("Enter the number: "))
num=[int(digit) for digit in str(user)] #copy-pasted from duck ai...

inbase=int(input("What is the base of number? "))
outbase=int(input("What is the base you except? "))

deci=[]
for index,i in enumerate(num): #idea gave by duck ai...i forgot abt this...
    deci.append(i*(inbase**(len(num)-index-1))) #copy-pasted by duck ai...

rem=[]
current = sum(deci) #copy-paste by gemini...

while current>0: #condition by gemini... idk why it didn't come to my mind?
    k = current % outbase
    rem.append(k)
    current = current // outbase

final=int(''.join(map(str, reversed(rem)))) #copy-paste from duck ai...
print(final)

#solution...

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
        
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    if any(d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    if any(d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    number = sum(d*input_base**i for i,d in enumerate(digits[::-1]))
    if number == 0:
        return [0]
        
    new_digits = []
    while number != 0:
        new_digits.insert(0, number%output_base)
        number = number//output_base
        
    return new_digits