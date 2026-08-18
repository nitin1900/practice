#made silly mistake and copy pasted the reader and writter part from ai...

import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

students=[]
try:
    with open(sys.argv[1]) as file:
        reader=csv.DictReader(file)
        for row in reader:
            last_name, first_name = row["name"].split(",")
            first_name = first_name.strip()
            students.append({"first": first_name, "last": last_name, "house": row["house"]})

    with open(sys.argv[2],"w") as file:
        writer=csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)
except FileNotFoundError:
    sys.exit("file not found")