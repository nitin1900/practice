#my code...

s = input("word: ")
l = len(s)
v = ""

while l != 0:
    v = v + s[l-1]  # use l-1 because indexing starts at 0(correct by chatgpt)-silly mistake by me
    l -= 1

print(v)

#code by chatgpt...

def reverse_string(s):
    v = ""
    l = len(s)
    while l != 0:
        v += s[l-1]
        l -= 1
    return v

word = input("word: ")
print(reverse_string(word))

#solution...(damn only 2 line of code and i wrote 7 line...)

def reverse(text):
  return text[::-1]