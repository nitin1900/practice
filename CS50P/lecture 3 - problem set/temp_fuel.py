#15-min trick works bro but yes i took help like searching let's goo...

while True:
    try:
        (x,y)=input("fraction: ").split("/")
        x=int(x)
        y=int(y)
        if x>y or x<0 or y<=0:
            continue
        k=round((x/y)*100)
        if k<=1:
            print("E")
        elif k>=99:
            print("F")
        else:
            print(f"{k}%")
    except ValueError:
        print("It is not an integer")
    except ZeroDivisionError:
        print("y should not be zero")
    else:
        break

# I guess it took almost 2 hours damn...