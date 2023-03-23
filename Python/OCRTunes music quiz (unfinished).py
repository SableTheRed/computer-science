##~~~~~~~~~~~~~~~~~~~~~~##
##### ~ MUSIC QUIZ ~ #####
##~~~~~~~~~~~~~~~~~~~~~~##


#~~~~~~~~~~~~~~#
## MY IMPORTS ##
#~~~~~~~~~~~~~~#
import random #~pseudorandom numbers
import time   #~delay and time control





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
## DECLARING GLOBAL VARIABLES ##
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
global Authenticated
global username
global password



Authenticated = False




#~~~~~~~~~~~~~~~~~~~~~~~#
## DECLARING FUNCTIONS ##
#~~~~~~~~~~~~~~~~~~~~~~~#

def procRegisterUser(Authenticated): # creates a funtion to sign in / register the user
    while Authenticated == False:    # this code will repeat until the user has been authenticated
        
        # stores the username and password entered #
        username=str(input("what is your name"))
        password=str(input("enter your password"))
        userandpass= ((password) + (username))

        f = open('users.txt', 'a') # opens the text file containing the list of usersm

        if (userandpass) in open('users.txt').read():
            
#~~~~this code will only run if the user credentials are found in the text file~~~#
            print("welcome back, " + (username) + "!")
            f.close()
            Authenticated = True

#~~~~~~this code will offer to create a login for a user that does not exist~~~~~#
        else:
            acc = input("sadly you dont exist yet, would you like us to set up an account? [Y/N]  ")
            if acc.upper() == "Y":
                f.write(" " + (userandpass) + " ")
                f.close()
                Authenticated = True
            else:
                print("OK, let's re-enter your credentials")
    return Authenticated






#~~~~~~~~~~~~~~~~~~~#
### THE MAIN GAME ###
#~~~~~~~~~~~~~~~~~~~#
print("WELCOME TO OCR TUNES!")


#Songlist = [["Back In Black","AC-DC"],["Paranoid","Black Sabbath"],["Subdivisions","Rush"],["Stairway To Heaven","Led Zeppelin"],["Brain Damage","Pink Floyd"],["Hayloft","Mother Mother"]]

play = True
count = 0
while play == True:
    chosen = random.choice(Songlist)
    print("artist:", chosen[1])
    song = chosen[0]
    song_list=song.split()
    initials = ""
    for word in song_list:
        initials = initials + word[0] + "__________ "
    print("Initials are:", initials)
    count = count+1
    if count > 3:
        play = False
    
