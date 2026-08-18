import random
def main():
    play()
    new=input("Enter a new game(y/n): ").lower()
    if new=="y":
        play()
def play():
    u=str(input("What you choose? ")).lower()
    items=["rock","paper","scissors"]
    bot=random.choice(items)
    
    if u==bot:
        print("draw")
    elif (u=="rock" and bot=="scissors") or (u=="scissors" and bot=="paper") or (u=="paper" and bot=="rock"):
        print("You win")
    elif (bot=="rock" and u=="scissors") or (bot=="scissors" and u=="paper") or (bot=="paper" and u=="rock"):
        print("You lose")

main()
