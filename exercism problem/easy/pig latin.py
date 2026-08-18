#my code...

def main():
    word=input("Enter a word: ").lower()
    final=check(word)
    print(final)

def check(word):
    vowel=("a","e","i","o","u")
    if word.startswith(vowel) or (word.startswith("xr") or word.startswith("yt")):
        return f"{word}ay"
    for i in range(len(word)):
        if word[i] in vowel or (word[i]=="y" and i>0):
            if word[i]=="u" and word[i-1]=="q":
                return f"{word[i+1:]+word[:i+1]}ay"
            else:
                return f"{word[i:]+word[:i]}ay"

if __name__ == "__main__":
    main()

#solution...

VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}


def translate(text):
    piggyfied = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            piggyfied.append(word + "ay")
            continue

        for pos in range(1, len(word)):
            if word[pos] in VOWELS_Y:
                pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
                piggyfied.append(word[pos:] + word[:pos] + "ay")
                break

    return " ".join(piggyfied)