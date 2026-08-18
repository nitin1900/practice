#copy-paste from ai...


vlq_num_mask = 0b1111111
vlq_continue_mask = 1 << 7


def encode(numbers):
    encoded = []

    for number in numbers:

        # how many 7-bit groups needed
        max_i = ((number >> 1).bit_length()) // 7

        for i in range(max_i, -1, -1):

            # get current 7-bit chunk
            chunk = (number >> (7 * i)) & vlq_num_mask

            # add continue bit if more chunks follow
            if i != 0:
                chunk |= vlq_continue_mask

            encoded.append(chunk)

    return encoded


def decode(bytes_):
    decoded = []
    code = 0

    # invalid if last byte still says "continue"
    if bytes_[-1] & vlq_continue_mask:
        raise ValueError("incomplete sequence")

    for byte in bytes_:

        # shift previous bits left by 7
        code = (code << 7) | (byte & vlq_num_mask)

        # if continue bit is NOT set, number finished
        if not (byte & vlq_continue_mask):
            decoded.append(code)
            code = 0

    return decoded


# ---------------- INTERACTIVE PART ----------------

print("1. Encode numbers")
print("2. Decode bytes")

choice = input("Choose option (1 or 2): ")

if choice == "1":

    nums = input(
        "Enter numbers separated by spaces: "
    ).split()

    nums = [int(n) for n in nums]

    result = encode(nums)

    print("\nEncoded bytes (decimal):")
    print(result)

    print("\nEncoded bytes (hex):")
    print([hex(x) for x in result])

elif choice == "2":

    bytes_input = input(
        "Enter bytes separated by spaces: "
    ).split()

    # supports decimal or hex like 81 00 OR 0x81 0x00
    bytes_ = [int(b, 0) for b in bytes_input]

    result = decode(bytes_)

    print("\nDecoded numbers:")
    print(result)

else:
    print("Invalid option")

#solution...

vlq_num_mask = 0b1111111
vlq_continue_mask = 1<<7

def encode(numbers):
    # 1-liner 
    return [((number>>(7*i)) & vlq_num_mask) | (bool(i)<<7)
            for number in numbers
            for i in range(((number>>1).bit_length())//7, -1, -1)]

def decode(bytes_):
    return list(_decode(bytes_))

def _decode(bytes_):
    code = 0
    if bytes_[-1] & vlq_continue_mask:
        raise ValueError('incomplete sequence')

    for byte in bytes_:
        code = (code << 7)|(byte & vlq_num_mask)
        if not(byte & vlq_continue_mask):
            yield code
            code = 0

    
    
