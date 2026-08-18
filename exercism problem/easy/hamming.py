#just gave up after infinte loop of code and copy pasted the code...

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            count += 1
    return count


#my code with error:
dna=input("original dna: ")
new=input("new dna: ")
e=0
c=0
if len(dna)==len(new):
    pass
else:
    print("invaild input dna!=new dna")
    raise ValueError
while c<len(dna):
    if dna[c]!=new[c]:
        e+=1
    else:
        c+=1
print("Hamming Distance is:",e)
