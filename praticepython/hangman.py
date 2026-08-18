import random

def hangman():
    word=[]
    with open("sowpods.txt","r") as f:
        lines=f.readlines()
    word=list(random.choice(lines).strip())
    print(word)

    temp=["_"]*len(word)

    noot=[]
    n=0

    while n!=6: 
        letter=str(input("Enter a letter: ")).upper()

        if letter in word:
            for index,x in enumerate(word):
                if x==letter:
                    temp[index]=letter
            print(f"Congrats you won {''.join(temp)}")
            if word==temp:#for infinite guess (word!=temp)
                print(''.join(word))
                break
        else:
            if letter not in noot:
                print("Incorrect guess")
                noot.append(letter)
                n+=1
                print(f"You have {6-n} guess left")
            else:
                print("Already guessed")
        
hangman()

while True:
    ask=input("Do you want to continue new game?(yes/no): ").strip().lower()
    if ask=="yes":
        hangman()
    else:
        print("Hope you had fun!!")
        break
