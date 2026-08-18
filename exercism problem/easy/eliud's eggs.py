#this problem was easy tho...

binary=input("Enter the binary code: ")
k=0
for i in binary:
    if i=="1": #made silly mistake 1 instead of "1"
        k+=1
print(k)


#solution...

def egg_count(display_value):
    return bin(display_value).count('1')
