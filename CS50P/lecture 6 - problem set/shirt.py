#i tried myself but failed then copy pasted some code from ai... 


import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

root1, ext1 = splitext(sys.argv[1].lower())
root2, ext2 = splitext(sys.argv[2].lower())

if ext1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
if ext2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")

if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = Image.open(sys.argv[1])
    resized_photo = ImageOps.fit(photo, size)
    resized_photo.paste(shirt, shirt)
    resized_photo.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("image was not found")