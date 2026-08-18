#solution...(just copy pasted)

def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    question = question.strip()

    if not question:
        raise ValueError("syntax error")

    formula = question.split()
    while len(formula) > 1:
        try:
            x_value = int(formula[0])
            y_value = int(formula[2])
            symbol = formula[1]
            remainder = formula[3:]

            if symbol == "plus":
                formula = [x_value + y_value] + remainder
            elif symbol == "minus":
                formula = [x_value - y_value] + remainder
            elif symbol == "multiplied":
                formula = [x_value * y_value] + remainder
            elif symbol == "divided":
                formula = [x_value / y_value] + remainder
            else:
                raise ValueError("syntax error")
        except:
            raise ValueError("syntax error")

    return int(formula[0])