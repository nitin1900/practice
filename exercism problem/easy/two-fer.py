#it was an easy code...

name=input("what is your name? ")
if name=="":
    print("One for you, one for me.")
else:
    print(f"One for {name}, one for me.")


#solution...

def two_fer(name="you"):
    return f'One for {name}, one for me.'