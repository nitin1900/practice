#done by myself but taken help in debugging the code by ai...

dna={"G":"C","C":"G","T":"A","A":"U"}
rna=""
user=input("DNA Sequence: ")
for i in user:
    if i in dna:
        rna=rna+dna[i]
print (f"RNA squence: {rna}")