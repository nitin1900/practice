#duck.ai help he and gave me this r'\b(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b'


import re
import sys

def main():
    print(validate(input("IPV4 Address: ")))

def validate(ip):
    if re.search(rf"^(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()