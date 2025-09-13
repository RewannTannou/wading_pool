text = input(" type something long with space :")
wordList = text.split(" ")
textFinal = ""
# for word in wordList:
#   letter = word[0]
#   textFinal = textFinal + letter

textFinal = "".join([word[0] for word in wordList])
print(textFinal.capitalize())
