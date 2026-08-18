#my code given to chatgpt and chatgpt write code for me just copy and paste...

def classify(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Compute aliquot sum (sum of proper divisors)
    aliquot_sum = sum(i for i in range(1, n) if n % i == 0)

    if aliquot_sum == n:
        return "perfect"
    elif aliquot_sum > n:
        return "abundant"
    else:
        return "deficient"

def main():
    try:
        n = int(input("Enter a positive integer: "))
        result = classify(n)
        print(f"{n} is a {result} number.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

#most submmited solution...

def classify(number):
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')  
    s = 0
    for i in range(1, number):
        if number % i == 0:
            s += i
    if s == number:
        return 'perfect'
    if s > number:
        return 'abundant'
    return 'deficient'