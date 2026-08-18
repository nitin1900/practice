#my code...

number=input("Enter your phone number: ").replace("+1","")
number = ''.join(ch for ch in number if ch.isdigit())
if len(number)<10:
    raise ValueError("must not be fewer than 10 digits")
elif len(number)>11:
    raise ValueError("must not be greater than 11 digits")
elif len(number)==11 and number[0]!="1":
    raise ValueError("11 digits must start with 1")
elif len(number)==11:
    number=number[1:]
elif len(number)==10 and (number[0]=="0" or number[0]=="1"):
    raise ValueError("area code cannot start with zero or one")
else:
    pass
print(number)

#solution...(sorted few line code)

class PhoneNumber:
	def __init__(A,number):
		G='one';F='exchange';E='area';D='zero';C='1';B=number;A.number=''.join([A for A in B if A.isdigit()])
		if len(A.number)==11 and A.number[0]!=C:raise ValueError('11 digits must start with 1')
		if[A for A in B if A.isalpha()]:raise ValueError('letters not permitted')
		elif[A for A in B if A in'@:!']:raise ValueError('punctuations not permitted')
		elif len(A.number)<10:raise ValueError('must not be fewer than 10 digits')
		elif len(A.number)>11:raise ValueError('must not be greater than 11 digits')
		A.number=A.number[-10:];A.area_code=A.number[0:3]
		for(H,I,J,K)in((0,'0',D,E),(3,'0',D,F),(0,C,G,E),(3,C,G,F)):
			if A.number[H]==I:raise ValueError(f"{K} code cannot start with {J}")
	def pretty(A):return f"({A.area_code})-{A.number[3:6]}-{A.number[6:]}"