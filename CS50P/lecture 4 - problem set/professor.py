#i tried doing but failed with heavy error but at last i took help of AI...



import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0
        while tries < 3:
            try:
                g = int(input(f"{x} + {y} = "))
                if g == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
                    
            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level in (1,2,3):
                return level
            else:
                 raise ValueError
        except ValueError:
            print("Enter valid number")
            continue


def generate_integer(l):
    level=get_level()
    if level == 1:
        start = 0
        end = 9
    elif level == 2:
        start = 10
        end = 99
    elif level == 3:
        start = 100
        end = 999
    else:
        raise ValueError
    
    return random.randint(start, end)


if __name__ == "__main__":
    main()