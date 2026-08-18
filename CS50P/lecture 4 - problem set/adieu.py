import inflect
p=inflect.engine()
names=[]
while True:
    try:
        name=input("Name: ").title()
        names=names+[name]
    except EOFError:
        break


pnames=p.join(names)
print(f"Adieu, adieu, to {pnames}")