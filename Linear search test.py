# Linear search
# I Ryder
# 17/11/2020
melist = ['trump', 'biden', 'obama', 'bush', 'clinton', 'reagan', 'carter', 'ford', 'nixon', 'johnson', 'kennedy']
searched = str(input("Which president are you looking for?"))
searched = searched.lower()
pointer = 0
while pointer < len(melist) and melist[pointer] != searched:
    pointer = pointer + 1
if pointer >= len(melist):
    print("Item not found")
else:
    print("Item is at location ",pointer)
