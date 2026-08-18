#dimag ka daahi ho gaya lekin kese bhi dekh ke kar liya...(no ai but use in debugging)...
#used binary search algo...
arr=[i for i in range(1,101)]
low=0
high=len(arr)-1
def pick(low,high):
        return low+(high-low)//2
while True:
    print(f"picked:{arr[pick(low,high)]}")
    x=input("yes/low/high(1-100): ").strip().lower()
    if x=="yes":
        print("I am smart enough for you")
        break
    elif x=="low":
        low=pick(low,high)+1
        pick(low,high)
    elif x=="high":
        high=pick(low,high)-1
        pick(low,high)
