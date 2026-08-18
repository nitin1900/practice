def main():
    user = input("Input: ").strip()
    shortened_word = shorten(user)
    print(shortened_word)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = "" 
    
    for char in word:
        if char not in vowels:
            result = result + char
    return result

if __name__ == "__main__":
    main()