## quiz ##

print("""
###   Welcome to the python quiz on networks!   ###


### You will now face 101 questions on networks ###
###     (that is, 5 questions on networks)      ###
""")
score = 0
def correct():
    print("\nCorrect! that is the right answer!\n")
    score = score + 1
def wrong():
    print("\nUh-oh! that is not the right answer...\n")

def f_checkfortrue():
    if answer.upper() == "T":
        correct()
    else:
        wrong()
    print("your score so far is: ",score)

def f_checkforfalse():
    if answer.upper() == "F":
        correct()
    else:
        wrong()
    print("your score so far is: ",score)

input("Press enter to continue...")

answer = input("""

### QUESTION 1 ###
True or False; all networks require a server...
Press 'T' or 'F' to answer.
""")
f_checkforfalse()

answer = input("""

### QUESTION 2 ###
True or False; a Wide area network, or WAN, is used over a large geographical location...
Press 'T' or 'F' to answer.
""")
f_checkfortrue()

answer = input("""

### QUESTION 3 ###
True or False; a computer connected to a network is called a server...
Press 'T' or 'F' to answer.
""")
f_checkforfalse()
          
answer = input("""

### QUESTION 2 ###
True or False; all networks must be connected through physical cables...
Press 'T' or 'F' to answer.
""")
f_checkforfalse()

answer = input("""

### QUESTION 2 ###
True or False; 2 computers connected together make a network...
Press 'T' or 'F' to answer.
""")
f_checkfortrue()




















