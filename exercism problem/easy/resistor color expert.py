#my code... simple tha yaar...

colors = {'black': 0, 'brown': 1,'red': 2, 'orange': 3, 'yellow': 4,
         'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

tolerance={
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

user=[]
user=input("Enter color: ").strip().lower().split(" ")
def value(user):
     return (colors[user[0]]*10 + colors[user[1]]) * (10**colors[user[2]])

def metric_prefix(value):
    prefixes = {
        1_000_000_000: 'Giga ',  # Giga
        1_000_000: 'Mega ',      # Mega
        1_000: 'kilo ',          # Kilo
        1: ''                # No prefix
    }
    for factor, prefix in prefixes.items():
        if value >= factor:
            return f"{value // factor} {prefix}ohm"
    return f"{value} ohm"  # Default to grams if no prefix applies

if len(user) == 4:
    print(f"{metric_prefix(value(user))} ±{tolerance[user[3]]}")
elif len(user)>5:
    print("only 4 accepted in input")
else:
    print("invalid user input")


#solution...

RESISTOR_COLORS = (
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
)

RESISTOR_COLORS_TOLERANCE = {
    "silver": "10%",
    "gold": "5%",
    "red": "2%",
    "brown": "1%",
    "green": "0.5%",
    "blue": "0.25%",
    "violet": "0.1%",
    "grey": "0.05%",
}


def value(color):
    return RESISTOR_COLORS.index(color)


def resistor_label(colors):
    tolerance_color = colors[-1]
    color_values = [value(color) for color in colors[:-1]]

    if len(colors) == 4:
        resistance_value = (
            10 * color_values[0] + color_values[1]
        ) * 10 ** color_values[2]
    elif len(colors) == 5:
        resistance_value = (
            100 * color_values[0] + 10 * color_values[1] + color_values[2]
        ) * 10 ** color_values[3]
    else:
        return "0 ohms"

    for factor, prefix in [
        (1_000_000_000, "giga"),
        (1_000_000, "mega"),
        (1_000, "kilo"),
    ]:
        if resistance_value >= factor:
            resistance_value /= factor
            return (
                f"{resistance_value:g}"
                " "
                f"{prefix}ohms"
                " "
                f"±{RESISTOR_COLORS_TOLERANCE[tolerance_color]}"
            )

    return (
        f"{resistance_value:g} ohms"
        " "
        f"±{RESISTOR_COLORS_TOLERANCE[tolerance_color]}"
    )