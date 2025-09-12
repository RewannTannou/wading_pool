listOfFiveElement = [1, 7, 3, 4, 5]
newList = []
while listOfFiveElement != []:
    newList.append(max(listOfFiveElement))
    listOfFiveElement.remove(max(listOfFiveElement))

print(newList)
