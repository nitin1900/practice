#duck ai help me again by telling me len(file.readlines) core logic lol but i mess up now this...

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count=0
try:
    with open(sys.argv[1],"r") as file:
        for line in file:
            if line.strip().startswith("#"):
                pass
            elif line.strip()=="":
                pass
            else:
                count+=1
except FileNotFoundError:
    sys.exit("file doesn't exit")

print(f"count:{count}")