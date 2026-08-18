#ahh i took help sort functioni just ask ai how to do that and i just gave ai for error checking as i couldn't do...

grocery={}
while True:
    try:
        key=input("Items: ").upper()
        if key not in grocery:
            grocery[key]=1
        else:
            grocery[key]+=1
    except EOFError:
        break

for i in sorted(grocery):
    print(f"{grocery[i]} {i}")



#dict={key:value}