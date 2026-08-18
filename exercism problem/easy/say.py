#took help from ai as giving the logic and blueprint how to do these things...

under_20 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def main():
    user=int(input("Enter a number: "))
    final=hundred(user)
    print(final)
def hundred(user):
    if 0<=user<=999999999999:
        if user<20:
            word=under_20[user]
            return word
        elif 20<=user<=99:
            t=(user//10)*10
            o=user%10
            if o==0:
                word=tens[t]
            else:
                word=tens[t]+"-"+under_20[o]
            return word
        elif 100 <= user <= 999:
            h = user // 100
            rest = user % 100
            hundreds_word = under_20[h] + " hundred"
            if rest == 0:
                return hundreds_word
            else:
                word = hundreds_word + " " + hundred(rest) 
                return word
        elif 1_000<=user<=999_999:
            thou=user//1_000
            rest=user%1_000
            thousand_word=hundred(thou)+" thousand"
            if rest==0:
                return thousand_word
            else:
                word=thousand_word+" "+hundred(rest)
                return word
        elif 1_000_000<=user<=999_999_999:
            milli=user//1_000_000
            rest=user%1_000_000
            million_word=hundred(milli)+" million"
            if rest==0:
                return million_word
            else:
                word=million_word+" "+hundred(rest)
                return word
        elif 1_000_000_000<=user<=999_999_999_999:
            billi=user//1_000_000_000
            rest=user%1_000_000_000
            billion_word=hundred(billi)+" billion"
            if rest==0:
                return billion_word
            else:
                word=billion_word+" "+hundred(rest)
                return word
    else:
        raise ValueError("input out of range")
main()

#solution

ONES = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'ninteen',
]
TENS = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety']
BASES = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (1e2, 'hundred'),
)


def say(num):
    parts = []
    if not 0 <= num < 1e12:
        raise ValueError('input out of range')

    if num == 0:
        return ONES[num]

    for base, name in BASES:
        if num >= base:
            parts.append(say(int(num // base)))
            parts.append(name)
            num = int(num % base)

    out = ''
    if num >= 20:
        out += TENS[num // 10]
        num = int(num % 10)
        if num:
            out += '-'
    if num and num < 20:
        out += ONES[num]
    if out:
        parts.append(out)

    return ' '.join(parts)