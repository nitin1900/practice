#soultion...just copy pasted...new to me

def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")

    index = len(search_list)//2
    middle_value = search_list[index]
    if value > middle_value:
        return index + 1 + find(search_list[(index+1):], value)
    if value < middle_value:
        return find(search_list[:index], value)
    return index
