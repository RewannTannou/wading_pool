def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


def prepare_Sandwich(x):
    i = 0
    while i < x:
        bread(), lettuce(), tomato(), ham(), ham(), bread()
        i += 1


prepare_Sandwich(5)
