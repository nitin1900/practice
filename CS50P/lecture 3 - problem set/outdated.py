#most of code solved with help of ai...
#new to me


month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "1","2","3","4","5","6","7","8","9","10","11","12"
    ]

while True:
    try:
        date=input("date(MM-DD-YY): ").title()
        if "/" in date:
            (m,d,y)=date.split("/")
        elif "-" in date:
            (m,d,y)=date.split("-")
        elif "," in date:
            date=date.replace(",","")
            (m,d,y)=date.split(" ")
        else:
            raise ValueError
        
        if m in month and 0<int(d)<=31:
            if m.isalpha() and d.isdigit():
                m = month.index(m) + 1
                print(f"YYYY-MM-DD: {y}-{int(m):02}-{int(d):02}")
                break
            elif m.isdigit() and d.isalpha():
                continue
            else:
                print(f"YYYY-MM-DD: {y}-{int(m):02}-{int(d):02}")
                break
        else:
            print("Invalid date")
            continue
    except ValueError:
        print("Invalid date")
        continue