## REVERSE IT

# takes in a string for user
# reverses the string

import time, sys, random




#stolen code
colour = sys.stdout.shell
#color.write(YourText,Color)
#stolen code

userinpt = str(input("Input a string you would like to have reversed: \n"))
rvrs = ""
for item in userinpt:
        rvrs = (item) + rvrs

colours = ["SYNC", "stdin", "BUILTIN", "STRING", "console", "COMMENT", "stdout", "TODO", "stderr", "hit", "DEFINITION", "KEYWORD", "ERROR", "sel"]
        
for item in rvrs:
    number = random.randint(0,13)
    Color = colours[number]
    #Color = "BUILTIN"
    colour.write((item),Color)
    time.sleep(.01)
input()



