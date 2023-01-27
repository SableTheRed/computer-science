staff = ["Anna", "Bob", "Carol"]

quartersales = [[100,110,120,110],
[350,355,360,360],
[200,210,220,220]]

for s in range(0,3):
    annualsales = 0
    print(f"\n{staff[s]}:\n")

    for q in range(0,4):
        print("Quarter", q+1, quartersales[s][q])
        annualsales += quartersales[s][q]
    
    print(f"\nAnnual sales: {annualsales}\n")