#solve with help of ai...

from validator_collection import validators


def main():
    try:
        email=input("email: ")
        validators.email(email)
        print("valid")
    except (ValueError, TypeError):
        print("enter valid email")

if __name__ == "__main":
    main()

#another method..

from validator_collection import checkers

def main():
    email = input("What's your email address? ")
    
    # checkers returns True or False
    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()