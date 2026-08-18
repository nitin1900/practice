#everything done by myself by using my brains and breaking into small parts like
#doing separately break of word and what question asked to do...

rna={
  "AUG": "Methionine",
  "UUU": "Phenylalanine",
  "UUC": "Phenylalanine",
  "UUA": "Leucine",
  "UUG": "Leucine",
  "UCU": "Serine",
  "UCC": "Serine",
  "UCA": "Serine",
  "UCG": "Serine",
  "UAU": "Tyrosine",
  "UAC": "Tyrosine",
  "UGU": "Cysteine",
  "UGC": "Cysteine",
  "UGG": "Tryptophan",
  "UAA": "STOP",
  "UAG": "STOP",
  "UGA": "STOP"
}
#break of word...
user=input("Enter a RNA sequence: ")
i=1
j=0
part=[]
while j%3==0 and j<=len(user):
    part.append(user[j:i*3])
    i+=1
    j+=3
#question instruction...
total=""
for k in part:
    if rna[k]=="STOP":
        break
    elif total=="" and rna[k]!="STOP":
        total=total+rna[k]
    else:
        total=total+","+rna[k]
print(total)

#solution...

from itertools import takewhile
from textwrap import wrap


catalogue = {
    'AUG': 'Methionine',
    'UUC': 'Phenylalanine',
    'UUU': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAC': 'Tyrosine',
    'UAU': 'Tyrosine',
    'UGC': 'Cysteine',
    'UGU': 'Cysteine',
    'UGG': 'Tryptophan',
}


def is_not_stop(pattern):
    return pattern not in ('UAG', 'UAA', 'UGA')


def proteins(strand):
    print(wrap(strand, 3))
    return [protein
            for pattern in takewhile(is_not_stop, wrap(strand, 3))
            for protein in (catalogue.get(pattern, None),)
            if protein]

