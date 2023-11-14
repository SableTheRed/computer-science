# something about calculations and alcohol

age = int(input("How old are you?\n"))

match age:
    case range(0,4):
        print("Definitely too young to drink.")
    case range(5,15):
        print("It's up to your parents, but legally you can drink at home.")
    case range(16,17):
        print("You may drink beer, wine, or cider with a meal on licensed premises, but may not purchase it.")
    case _:
        print("You may drink and purchase alcohol on licensed premises. Drink responsibly :)")

