def recurciveFunction(x):
    number = x
    if number <= 0:
        return 0
    return number + recurciveFunction(x - 1)


recurciveFunction(42)
