import string

phrase = input("Please enter a sentence or phrase:\n")

phrase = phrase.translate(str.maketrans(" "," ",string.punctuation))
phrase = phrase.lower().split()

dictionary = []
sequence = []
counter = 0

for word in phrase:
    if word not in dictionary:
        dictionary.append(word)

for item in phrase:
    sequence.append(dictionary.index(item)) 

print("Dictionary:")

for i in dictionary:
    print(f"{i, dictionary.index(i)}")

print(sequence)

#decompressor:
mystr = ""
for item in sequence:
    mystr += (" "+dictionary[item])

print(mystr)

