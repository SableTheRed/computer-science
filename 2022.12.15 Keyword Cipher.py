##  string = "["
##  for letter in "abcdefghijklmnopqrstuvwxyz":
##      string += (f'"{letter}",')
##  string += "]"
##  print(string)


# an alphabet to work with
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# determining the keyword
keyword = input("Choose a keyword:\n")
keyword = keyword.replace(" ","").lower()

# creating a new dictionary of letters
dict = []
for letter in keyword:
    if letter not in dict:
        dict.append(letter)

for letter in alphabet:
    if letter in dict:
        pass
    else:
        dict.append(letter)

# print the creation of the key
st = ""
for i in dict:
    st += i
print(st)

# encrypt a phrase
phrase = input("Enter a phrase to encrypt:\n")
phrase = phrase.replace(" ", "").lower()
new = ""
for letter in phrase:
    new += dict[alphabet.index(letter)]
print(new)

# decrypt a phrase
phrase = input("Enter a phrase to decrypt:\n")
phrase = phrase.replace(" ", "").lower()
new = ""
for letter in phrase:
    new += alphabet[dict.index(letter)]
print(new)