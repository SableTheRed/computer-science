import sys

print("This program will encode your message using a ceasar cipher.")
MyChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg = str(input("Enter your message here   "))
msg = msg.lower()
newmsg = []
print("This is your plaintext message:", msg)

Key = int(input("How many characters would you like to shift your message by?"))
pointer = 0
position = 0
for letter in msg:
    position = 0
    while position < len(MyChars) and MyChars[position] !=letter:
        position = position + 1
    pointer = position
    pointer = pointer + Key
    newmsg.append(MyChars[pointer])

print("Your encoded message reads;")
for item in newmsg:
        sys.stdout.write(item)

print("\n\n\n")
input("Press any key to exit")
