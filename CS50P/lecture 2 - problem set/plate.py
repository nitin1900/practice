#solved by ai...




import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = s.strip()
    if any(char in string.punctuation + " " for char in s):
        return False
    
    
    if len(s) < 2 or len(s) > 6:
        return False

    
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    

    digit_started = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] == '0' and not digit_started:
                return False
            digit_started = True
        elif digit_started:
            return False
    
    return True




if __name__ == "__main__":
    main()