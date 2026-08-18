#easy tha lekin time toh laga aur .startswith() mein ai ki help liya

def main():
    user=input("Greeting: ").strip().lower()
    user=value(user)
    print(f"${user}")


def value(input):
    if input.startswith("hello"):
        return 0
    elif input.startswith("h"):
        return 20
    else:
        return 100
        
if __name__ == "__main__":
    main()