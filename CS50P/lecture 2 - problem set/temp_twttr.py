user=[]
user=input("Input: ").strip("")
vowels=["a","e","i","o","u","A","E","I","O","U"]
for char in user:
    if char not in vowels:
        print(char,sep="",end="")


#or else


word=input("Input: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]

def shorten(word, vowels):
    return ''.join(c for c in word if c not in vowels)

            
result = shorten(word, vowels)
print(result)