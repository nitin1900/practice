#my code with help of chatgpt...

days = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

i = 1
total = []

while i <= 12:
    gift = input("Today's gift: ")
    total.append(gift)

    # Build the sentence(by chatgpt)
    line = ""

    for j in range(len(total)-1, -1, -1):
        if j == 0 and i > 1:
            line += "and " + total[j]
        else:
            line += total[j]

        if j != 0:
            line += ", "

    print(f"On the {days[i]} day of Christmas my true love gave to me: {line}.")

    i += 1



#solution...(by highest rep user...)



days = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

text = ["Nowhere nohow",
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "]


def one_verse(days, text, start: int) -> str:
    format_string = "On the {} day of Christmas my true love gave to me: "

    result = [format_string.format(days[start])]

    if start == 1:
        # The first time we need to trim the "and " in a Partridge
        gifts = [text[1][4:]]
    else:
        gifts = [text[day] for day in range(1, start + 1)]

    return ''.join(result + gifts[::-1])


def recite(start: int, finish: int) -> list:
    return [one_verse(days, text, i) for i in range(start, finish+1)]
