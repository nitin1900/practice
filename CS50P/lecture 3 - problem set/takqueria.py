#moke solved myself but seen some hint in cs50 website and at last ask ai help to identify any error and fixed it

menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


total=0
while True:
    try:
        order=input(f"Item: ").title()
        if order in menu:
            total += menu[order]
            print(f"amount: ${total:.2f}")
    except EOFError:
        print(f"Thanks for ordering, Bill=${total:2f}")
        break

#took almost 1 hr damn...