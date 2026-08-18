#my code logic done by myself but refined by chatgpt...(function new get,zip)

user_input = input("Enter a number: ").replace(" ", "")
if not user_input.isdigit():
    print("invalid")
else:
    user = [int(x) for x in user_input]
    if len(user) <= 1:
        print("invalid")
    else:
        for p, i in enumerate(reversed(range(len(user)))):
            if p % 2 == 1:
                user[i] *= 2
                if user[i] > 9:
                    user[i] -= 9

        total = sum(user)

        if total % 10 == 0:
            print("valid")
        else:
            print("invalid")

#solution...

class Luhn:

    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(card_num)

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(num):
        total = 0
        pos = 0
        for ltr in reversed(num):
            if ltr.isdigit():
                if not pos % 2:
                    total+= int(ltr)
                else:
                    total += Luhn.luhny_tune(int(ltr))
                pos += 1
            elif ltr != " ":
                return False
        return pos > 1 and not total % 10