name = input("Veuillez donner votre prénom: ")
rDV = [
    ["Monday", "3:30 PM", "Joe", "Sam "],
    ["Monday ", "4:30 PM", "Bob", "Alice "],
    ["Tuesday ", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday ", "9:30 AM", "Joe", "Bob"],
]
for i in range(len(rDV)):
    if name in rDV[i]:
        print(rDV[i])
