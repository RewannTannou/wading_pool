def func1(s: str, n: int):
    if len(s) == n:
        print("True")
    else:
        print("False")


def func2(s: str, n: int):
    compte = 0
    for char in s:
        if not (char.isalnum()):
            compte += 1
    if compte == n:
        print("True")
    else:
        print("False")


def func3(s: str, n: int):
    compte = 0
    for char in s:
        if char.isdigit():
            compte += 1
    if compte == n:
        print("True")
    else:
        print("False")


func1("caca", 4)
func2("*été*", 2)
func3("3étéen1", 2)
