import csv,sys
from datetime import datetime
from collections import Counter

birthdays=[]
names=[]
month=[]
with open("birthday.csv") as f:
    reader=csv.DictReader(f)
    for row in reader:
        birthdays.append({"name":row["name"],"date":row["date"]})
#for name=[]
for birthday in birthdays:
    names.append(birthday['name'])
#for month=[]
for birthday in birthdays:
    tempdate=birthday['date'].strip().title()
    try:
        tempmon=datetime.strptime(tempdate,"%B %d, %Y") #mc ek space(before %Y) nahi diya dimag khagaya mc
        month.append(tempmon.strftime("%B"))
    except ValueError:
        month.append("Unknown")

#user want to add name of the person in list...
if len(sys.argv)==4 and sys.argv[1]=="add":
    name=str(sys.argv[2]).capitalize()
    date=str(sys.argv[3])
    if name not in names:
        with open("birthday.csv","a") as f:
            writer=csv.DictWriter(f,fieldnames=["name","date"])
            writer.writerow({"name":name,"date":date})
            sys.exit("done")
    else:
        sys.exit(f"{name} is alredy present")

print("welcome to birthday dictionary, we know the birtday of: ")
print('\n'.join(names))

#user want to know specfic person date...
who=input("whose birthday you want to know? ").strip().capitalize()
found="True"
for birthday in birthdays:
    if who==birthday['name']:
        print(birthday['date'])
        found="True"
        break
    else:
        found="False"

if found=="False":
    print(f"sadly we don't have the {who}'s birthday in the list")
    print('as you can add person name by doing ""python [filename] add [person name] "[DOB in "MM DD, YYYY"]" ')

mon=input("Do you want to know exact month of all birthday falls (y/n): ")

#copy-paste only this part from ai to get clean output...
if mon.strip().lower() == "y":
    counts = Counter(month)

    print("\nBirthday months:")
    for month_name, count in counts.most_common():
        print(f"{month_name:<10} : {count}")
