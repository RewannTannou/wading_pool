def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" ============ ")


def prepare_Sandwich(x, veg=False):
    i = 0
    while i < x:
        if veg == True:
            print(bread(), lettuce(), tomato(), lettuce(), tomato(), bread())
        else:
            print(bread(), lettuce(), tomato(), ham(), ham(), bread())
        i += 1


prepare_Sandwich(5, True)
