def func1(s: str, n: int):
    if len(s) == n:
        return True
    else:
        return False


def func2(s: str, n: int):
    compte = 0
    for char in s:
        if not (char.isalnum()):
            compte += 1
    if compte == n:
        return True
    else:
        return False


def func3(s: str, n: int):
    compte = 0
    for char in s:
        if char.isdigit():
            compte += 1
    if compte == n:
        return True
    else:
        return False


def passcheck(fun, n: int, s: str):
    try:
        return fun(s, n)
    except TypeError as e:
        print(f"Erreur de type dans la fonction {e}")


print(passcheck(func1, 16, "mysecretpassword"))
print(passcheck(func2, 3, "mysecretpassword"))
print(passcheck(func3, 1, "mysecretpassword"))
