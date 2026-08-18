#copy-paste from gemini
a = input("Enter numbers for a (separated by spaces): ").split()
b = input("Enter numbers for b (separated by spaces): ").split()

# Assuming a and b are both lists of the exact same length
if a == b:
    print("Equal")

#trying to so myself with gemini given blueprint
elif len(a) > len(b):
    is_superlist = False
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            is_superlist = True
            break
            
    if is_superlist == True:
        print("Superlist")
    else:
        print("Unequal")

elif len(a) < len(b):
    is_sublist = False
    for i in range(len(b)):
        if b[i:i+len(a)] == a:
            is_sublist = True
            break
            
    if is_sublist == True:
        print("Sublist")
    else:
        print("Unequal")

else:
    print("Unequal")


#solution:

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def check_sub_sequences(list_one, list_two):
    n1 = len(list_one)
    n2 = len(list_two)
    return any(list_two[i:i+n1] == list_one for i in range(n2 - n1 + 1))
    
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sub_sequences(list_one, list_two):
        return SUBLIST
    if check_sub_sequences(list_two, list_one):
        return SUPERLIST
    return UNEQUAL