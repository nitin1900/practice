#my code...

point={
    "a":1,
    "e":1,
    "i":1,
    "o":1,
    "u":1,
    "l":1,
    "n":1,
    "r":1,
    "s":1,
    "t":1,
    "d":2,
    "g":2,
    "b":3,
    "c":3,
    "m":3,
    "p":3,
    "f":4,
    "h":4,
    "v":4,
    "w":4,
    "y":4,
    "k":5,
    "j":8,
    "x":8,
    "q":10,
    "z":10,
}
score=0
user=list(input("enter letter: "))
for i in user:
    score=score+point[i]
print("your score is: ",score)


#correct code would be...(copy and pasted from ai...)
# Old data: grouped by score
old_data = {
    1: ["A","E","I","O","U","L","N","R","S","T"],
    2: ["D","G"],
    3: ["B","C","M","P"],
    4: ["F","H","V","W","Y"],
    5: ["K"],
    8: ["J","X"],
    10: ["Q","Z"]
}

# New dictionary (like your understanding)
point = {}

for score, letters in old_data.items():   # go through each score group
    for letter in letters:                # go through each letter in the group
        point[letter.lower()] = score     # store letter: score

print(point)


#solution...

def transform(old_data):
	new_data = {}
	for score, letters in old_data.items():
		for letter in letters:
			new_data[letter.lower()] = score
	return new_data