#took help but got misleaded...also made silly mistake

target=input("target: ")
candidate=input("candidate: ").split(",")
final=[]

def check(target,candidate):
    for i in candidate:
        if sorted(i.lower())==sorted(target.lower()):
            final.append(i)

check(target,candidate)
if target in final:
    final.remove(target)
print(final)

#solution...

def find_anagrams(word, candidates):
    return [
        x
        for x in candidates
        if x.casefold() != word.casefold()
        and sorted(x.casefold()) == sorted(word.casefold())
    ]
