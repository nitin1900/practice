#my code... use duck ai for help in metric_prefix function just copy and pasted...

colors = {'black': 0, 'brown': 1,'red': 2, 'orange': 3, 'yellow': 4,
         'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

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
            return f"{value // factor} {prefix}ohms"
    
    return f"{value} ohms"  # Default to grams if no prefix applies


print(metric_prefix(value(user)))

#solution...

def label(bands):
    COLOURS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    ohms = (10 * COLOURS.index(bands[0]) + COLOURS.index(bands[1])) * (10 ** COLOURS.index(bands[2]))
    
    if ohms > 1_000_000_000:
        prefix = "giga"
        ohms //= 1_000_000_000
    elif ohms > 1_000_000:
        prefix = "mega"
        ohms //= 1_000_000
    elif ohms > 1_000:
        prefix = "kilo"
        ohms //= 1_000
    else:
        prefix = ""
    
    return f"{ohms} {prefix}ohms"