#my code with the help of ai(as almost ai gave me prompt what to do and how to do... )

def check():
    # 1. THE DICTIONARY: Maps every opening bracket (key) to its matching closing bracket (value).
    bracket = {"(": ")", "{": "}", "[": "]"}
    
    # 2. THE STACK: Our empty pile of plates. We ONLY put opening brackets in here.
    stack = []
    
    user = input("Enter your text: ")
    
    # 3. THE SCANNER: Loop through the string, looking at one character at a time.
    for char in user:
        
        # STEP A: Is it an OPENING bracket? (Is it a key in our dictionary?)
        if char in bracket:
            stack.append(char) # Push the new plate onto the top of the stack.
        
        # STEP B: Is it a CLOSING bracket? (Is it a value in our dictionary?)
        elif char in bracket.values():
            
            # TRAP 1: THE EMPTY STACK. Are we trying to close a bracket when zero are open?
            if len(stack) == 0:
                print("Unbalanced")
                return # Emergency stop. The function completely halts here.
            
            # STEP C: THE INSPECTION. We have plates! Let's check the top one.
            else:
                top_plate = stack.pop() # Take the very last plate OFF the top of the stack.
                
                # TRAP 2: THE MISMATCH. Ask the dictionary: "What is the correct closing bracket for this top_plate?"
                # If the dictionary's answer doesn't match the current 'char', we fail.
                if bracket[top_plate] != char:
                    print("unbalanced")
                    return # Emergency stop. The brackets are crossed.
    
    # 4. THE FINAL AUDIT: The loop is finished. Are there any leftover plates?
    if len(stack) == 0:
        print("balanced") # The stack is empty. Every opening bracket was properly closed.
    else:
        print("unbalanced") # The loop ended, but plates are still sitting on the stack!
        
    print(stack) # Prints the final state of the list.

check()

#solution...

def is_paired(input_string):
    bracket_map = {"]" : "[", "}": "{", ")":"("}
    tracking = []

    for element in input_string:
        if element in bracket_map.values():
            tracking.append(element)
        if element in bracket_map:
            if not tracking or (tracking.pop() != bracket_map[element]):
                return False
    return not tracking