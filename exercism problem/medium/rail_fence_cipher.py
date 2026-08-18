#i decode the logic but couldn't write the code properly inm time...

def encode(message, rails):
    # Step 1: Create an empty string "bucket" for each rail
    # If rails = 3, this makes: ["", "", ""]
    fence = []
    for _ in range(rails):
        fence.append("") 
    
    # Step 2: Set up our starting position and direction
    current_rail = 0
    direction = 1  # 1 means moving down, -1 means moving up
    
    # Step 3: Walk through the message one letter at a time
    for char in message:
        # Drop the letter into the current rail's bucket
        fence[current_rail] += char 
        
        # Move to the next rail
        current_rail += direction
        
        # Step 4: The Boundary Check (The Zig-Zag)
        # If we hit the bottom rail, turn around and go up
        if current_rail == rails - 1:
            direction = -1 
            
        # If we hit the top rail, turn around and go down
        elif current_rail == 0:
            direction = 1
            
    # Step 5: Combine all the buckets together
    encoded_message = ""
    for bucket in fence:
        encoded_message += bucket
        
    return encoded_message

# ---- Interactive Testing ----
message = input("Enter a sentence: ")
rails = int(input("Enter number of rails: "))

result = encode(message, rails)
print("Encoded Message:", result)


#solution...


def fence_pattern(rails, message_size):
    r = 2 * (rails - 1)
    return sorted(((z % r) if (z % r) < rails else r - (z % r), z) for z in range(message_size))


def encode(msg, rails):
    return ''.join(msg[i] for _, i in fence_pattern(rails, len(msg)))


def decode(msg, rails):
    xx = zip(fence_pattern(rails, len(msg)), msg)
    return ''.join(ch for _, ch in sorted(xx, key=lambda i: i[0][1]))