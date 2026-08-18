#idk why i took so much time and i asked ai for this at last...


def main():
    coin_values = [25, 10, 5]  # List of acceptable coin denominations
    due = 50  # Amount due in cents
    total_inserted = 0  # Initialize total amount inserted
    
    while total_inserted < due:  # Continue until 50 cents or more is inserted
        try:
            insert_coin = int(input(f"Insert coin (Accepted: {coin_values}): "))
            if insert_coin in coin_values:
                total_inserted += insert_coin  # Add the inserted coin to the total
                amount_due = due - total_inserted  # Calculate remaining amount due
                
                if amount_due > 0:
                    print(f"Amount due: {amount_due} cents")
                else:
                    change = -amount_due  # Calculate change if total inserted >= due
                    print(f"Amount due: 0 cents. Your change is {change} cents.")
                    break  # Exit the loop once the payment is complete
            else:
                print("Invalid coin. Please insert a coin of 25, 10, or 5 cents.")
        except ValueError:
            print("Please insert a valid integer coin.")

if __name__ == "__main__":
    main()