#copy pasted code from previous lines.py code and made some silly misatke...


import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


menu=[]
try:
    with open(sys.argv[1]) as file:
        reader=csv.reader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("file not found")
    

print(tabulate(menu,headers="firstrow",tablefmt="grid"))