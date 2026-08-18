#my code...

user=input("Enter your list: ")
add=[]
for i in user:
    if i.isdigit(): #using this function idea given by duck ai as i use i=int(i) and got error
        add.append(i)
    else:
        pass
print(add)


#solution...

def flatten(iterable):
    flat = []
    for item in iterable:
        if isinstance(item, list):
            flat.extend(flatten(item))
        elif item is not None:
            flat.append(item)
    return(flat)

#wth is my code even correct?