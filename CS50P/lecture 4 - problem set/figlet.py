# I hate library concept ahhh...
#new to me

import sys
import random
from pyfiglet import Figlet


if len(sys.argv)==1:
    figlet = Figlet()
    f=Figlet(font=random.choice(figlet.getFonts()))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet = Figlet()
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid Usage")
    f = Figlet(font=sys.argv[2])
else:
    sys.exit("Invalid Usage")


text=input("Input: ")


print(f.renderText(text))