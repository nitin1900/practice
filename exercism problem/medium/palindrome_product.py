#solution...(copy-pasted it i tried mine but couldn't complete in 25 min lol...)

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b >= result:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)
