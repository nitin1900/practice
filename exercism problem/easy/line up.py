#easy question but first i didn't understand the question...

name=input("Enter your name: ")
user=str(int(input("Enter you number: ")))
if user.endswith("11") or user.endswith("12") or user.endswith("13"):
    print(f"{name}, you are the {user}th customer we serve today. Thank you!")
elif user.endswith("1"):
    print(f"{name}, you are the {user}st customer we serve today. Thank you!")
elif user.endswith("2"):
    print(f"{name}, you are the {user}nd customer we serve today. Thank you!")
elif user.endswith("3"):
    print(f"{name}, you are the {user}rd customer we serve today. Thank you!")
else:
    print(f"{name}, you are the {user}th customer we serve today. Thank you!")


#solution...

def line_up(name, number):
    # Determine ordinal suffix
    if 10 <= number % 100 <= 13:
        suffix = "th"
    else:
        last_digit = number % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"