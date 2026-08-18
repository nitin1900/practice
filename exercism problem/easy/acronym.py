#ask duck ai for help in line 6 and 8 for logic...
import string
user=[]
acronym=""
user=input("enter: ").upper().replace("-"," ")
user = ''.join(char for char in user if char not in string.punctuation)
for i in user.split():
    acronym+=i[0]
print("The acronym is",acronym)
print("user:",user)

#solution...

def abbreviate(to_abbreviate):
    phrase = to_abbreviate.replace('-', ' ').replace('_', ' ').upper().split()
    acronym = ''
    
    for word in phrase:
        acronym += word[0]

    return acronym