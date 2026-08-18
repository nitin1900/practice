#copy from ai...

def is_pangram(sentence):
    sentence = sentence.lower()  # ignore case
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in sentence:
            return False
    return True

# Example usage
sentence = input("sentence: ")
if is_pangram(sentence):
    print("Pangram")
else:
    print("Not Pangram")

#solution...

from string import ascii_lowercase


def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)