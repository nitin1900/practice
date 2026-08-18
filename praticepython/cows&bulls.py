import random,string
user=int(input("Enter a 4 digit number: "))
r=0
w=0
k=''.join(random.sample(string.digits,4))
user=str(user)
k=str(k)
for i in range(4):
    if user[i]==k[i]:
        r+=1
    else:
        w+=1
print(f"{r} cows,{w} bulls")
