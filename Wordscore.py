word = str(input("Please enter a word or phrase to obtain the Word score! \n"))
i = 0
vv = 0
word = word.lower()
for letter in word:
    if (word[i]) == "a":
        vv = vv + 5
    elif (word[i]) == "e":
        vv = vv + 4
    elif (word[i]) == "i":
        vv = vv + 3
    elif (word[i]) == "o":
        vv = vv + 2
    elif (word[i]) == "u":
        vv = vv + 1
    else:
        vv = vv
    i = i + 1
print("Word score:", vv)
