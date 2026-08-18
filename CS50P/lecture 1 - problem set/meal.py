#just copy and pasted the code - new to me


def main():
    user = input("What time is it? ")
    time = convert(user)

    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")
    hour = float(hour)
    minutes = float(minutes)/60
    new_time = hour+minutes

    return new_time


if __name__ == "__main__":
    main()