def main():
    while True:
        fraction=input("fraction: ")
        try:
            p = convert(fraction)
            label = gauge(p)
            print(f"{label}%")
            break
        except (ValueError, ZeroDivisionError, TypeError):
            pass


def convert(fraction):
    (x,y)=fraction.split("/")
    x=int(x)
    y=int(y)
    if x>y:
        pass
    elif x<0:
        raise ValueError
    elif y<=0:
        raise ZeroDivisionError
    else:
        k=x/y
        percentage=round((k)*100)
        return percentage


def gauge(percentage):
    if percentage<=1:
        return ("E")
    elif percentage>=99:
        return ("F")
    else:
        return percentage


if __name__ == "__main__":
    main()