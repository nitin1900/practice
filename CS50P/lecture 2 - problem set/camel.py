#bhai sabse jayada maaza aaya isme let's go!!!!


user=[]
user=input("name? ").strip("")


for i in user:
    if i==user[0].upper():
        print("first letter is capital ",i.lower(),sep="",end="")
    elif i==i.upper():
        print(f"_{i.lower()}",sep="",end="")
    else:
        print(i,sep="",end="")