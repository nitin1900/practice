def main():
    num=int(input("Enter a number: "))
    f=[0,1]
    def series():
        while len(f)!=num:
            k=f[len(f)-1]+f[len(f)-2]
            f.append(k)
    series()
    print(f)
main()
