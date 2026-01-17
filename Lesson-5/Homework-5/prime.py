def factor(n):
    count = 0
    for num in range(1, n+1):
        if n % num == 0:
            count += 1
    return count

n = int(input("Enter a positive number: "))
num_factors = factor(n)

def is_prime(num_factors):
    if num_factors == 2:
        return True
    else:
        return False
    
print(is_prime(num_factors))



