def factor(n):
    for num in range(1, n+1):
        if n % num == 0:
            print(f"{num} is a factor of {n}")

n = int(input("Enter a positive number: "))
factor(n)



