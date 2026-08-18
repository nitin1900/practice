#my code...it was easy and done some silly mistake...

def main():
    user=[]
    user=input("Enter numbers: ").split(" ")
    diff=ws(user)-ss(user)
    print(diff)

def ws(user):
    sum=0
    for i in user:
        sum=sum+int(i)
    tsum=sum**2
    return tsum

def ss(user):
    ssum=0
    for i in user:
        sqaure=int(i)**2
        ssum=ssum+sqaure
    return ssum

if __name__ == "__main__":
    main()


#solution...(by highest rep user)

def square_of_sum(count: int) -> int:
    """Return the square of the sum of the first count integers."""
    x = sum(range(count + 1))
    return x * x


def sum_of_squares(count: int) -> int:
    """Return the sum of the first count squares."""
    return sum(i * i for i in range(count + 1))


def difference_of_squares(count: int) -> int:
    """Return the difference of the two sums."""
    return square_of_sum(count) - sum_of_squares(count)