import string,random
n=int(input("how much long pass want to genrate: "))
all=string.ascii_letters+string.digits+string.punctuation
k=''.join(random.sample(all,n))
print(k)
