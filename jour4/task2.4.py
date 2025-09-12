for i in range(-30, 31, 1):
    if i % 3 != 0 and i % 5 != 0:
        print("\n", i)
    if i % 3 == 0:
        print("fizz", end="")
    if i % 5 == 0:
        print("buzz", end="")


# print(i, end="")
