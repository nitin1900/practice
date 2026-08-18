#from glm 5-turbo...
import re

text = input("Enter a subtitle: ").lower()

# \b matches word boundaries
# \w+ matches one or more word characters (letters, numbers, underscores)
# (?:'\w+)* matches an apostrophe followed by more word characters, zero or more times
pattern = r"\b\w+(?:'\w+)*\b"

results = re.findall(pattern, text) #from chatgpt...(but solve myself refining done by chatgpt...)
my_dict = {}
for i in results:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(my_dict)

#solution...

import re
from collections import Counter


def count_words(sentence):
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))
