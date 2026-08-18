#new to me (copy pasted from website)...

def is_isogram(phrase):
    scrubbed = [ltr.lower() for ltr in phrase if ltr.isalpha()]
    return len(set(scrubbed)) == len(scrubbed)