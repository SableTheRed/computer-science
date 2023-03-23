## FIZZBUZZ

#takes user input.
#prints all multiples of 3 and 5 up to that number, replacing them with 'fizz' and 'buzz' respectively.

import time,sys

maxnum = int(input("Up to what number would you like to fizzbuzz?"))
time.sleep(2)
no = 1

text = ("...")

for item in text:
    sys.stdout.write(item)
    time.sleep(.2)


for i in range(0,maxnum):
    output = "\n" + str(no) + ":"
    if no % 3 == 0:
        output = output + "fizz"
    if no % 5 == 0:
        output = output + "buzz"
    for item in output:
        sys.stdout.write(item)
        time.sleep(.1)
    no = no + 1
    time.sleep(0.1)
time.sleep(.2)
print("\nFIZZBUZZ COMPLETE")

input()
