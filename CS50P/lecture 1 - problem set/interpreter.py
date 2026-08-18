#new to me ^x, y, z = expression.split(" ")&

expression=input("Expression: ").strip()
x, y, z = expression.split(" ")
x=int(x)
z=int(z)
if "+" in expression:
    print(x+z)
elif "-" in expression:
    print(x-z)
elif "*" in expression:
    print(x*z)
elif "/" in expression and z!=0:
    print(x/z)
elif "%" in expression and z!=0:
    print(x%z)
else:
    print("Expression is invalid")