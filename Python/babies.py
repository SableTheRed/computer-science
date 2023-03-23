import random as r

weight = []
for n in range(100):
    weight.append(r.randint(1500,4000))
nobabies = len(weight)
print(weight)

#avg
total = 0
for i in weight:
    total += i
mean = total / nobabies
print(mean)


#avg below 500
bracket = mean - 500
lightweight = 0
num = 0
for i in weight:
    if i < bracket:
        num += 1
        lightweight += i
lightmean = lightweight/num
print(num)
print(lightmean)
