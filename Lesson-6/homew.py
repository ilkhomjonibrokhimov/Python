def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper


@check
def div(a, b):
    return a / b


# Examples
print(div(6, 2))  # Output: 3.0
print(div(6, 0))  # Output: Denominator can't be zero
