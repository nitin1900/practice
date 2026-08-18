#ask ai to help in question undersatnding and all done by myself

colour={
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

user=input("enter the colour of resistor: ").strip().lower()
if user in colour:
    print(colour[user])

#solution on the exercise....

def color_code(color):
    return colors().index(color)


def colors():
    return [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'     
    ]
