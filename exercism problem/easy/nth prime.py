#copy paste from gemini...

def get_nth_prime(number):
    # Error Handling
    if number < 1:
        raise ValueError('there is no zeroth prime')
    
    # The Generator Engine
    counter = 2
    primes = [2]
    
    while len(primes) < number: 
        counter += 1
        # Check if the counter is divisible by any prime we already found
        if all(counter % test != 0 for test in primes):
            primes.append(counter)
            
    return primes[-1]

def main():
    print("--- Nth Prime Engine ---")
    print("Type 'quit' at any time to exit.\n")
    
    while True:
        user_input = input("Which nth prime do you want to find? (e.g., 6): ")
        
        if user_input.lower() == 'quit':
            print("Exiting engine...")
            break
            
        try:
            nth_target = int(user_input)
        except ValueError:
            print("Error: Please enter a valid number.\n")
            continue
            
        try:
            result = get_nth_prime(nth_target)
            print(f"\nSuccess: The {nth_target} prime number is {result}")
            print("---------------------------------\n")
        except ValueError as e:
            # Catches the custom error from the instructions
            print(f"\n[!] CAUGHT EXCEPTION: ValueError: {e}")
            print("---------------------------------\n")

if __name__ == "__main__":
    main()

#solution...

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    counter = 2
    primes = [2]
    while len(primes) < number: 
        counter += 1
        if all(counter % test != 0 for test in primes):
            primes.append(counter)
    return primes[-1]
