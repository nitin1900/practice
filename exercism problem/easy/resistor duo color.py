#my code:

colour=[
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

user=[]
final=""
user=input("enter the colour of resistor: ").strip().lower().split("-")
for i in user:
    if i in colour:
        final=final+str(colour.index(i))
print(final)

#solution:

codes = {'black': 0, 'brown': 1,'red': 2, 'orange': 3, 'yellow': 4,
         'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

def value(colors):
    return int(str(codes[colors[0]]) + str(codes[colors[1]]))
