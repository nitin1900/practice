#my code I have really trouble to write the syntax although i got the rough idea of logic:
s = "pwwkew"

window = []
max_len = 0

for char in s:
    while char in window:
        window.pop(0)
    window.append(char)
    if len(window) > max_len:
        max_len = len(window)

print("Longest non-repeating length:", max_len)

#submmited in leetcode:

