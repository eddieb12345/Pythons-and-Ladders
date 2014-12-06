import random

frequency = [0]*11

for i in range(1000):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2 - 2
    frequency[total] = frequency[total]+1

total = 0
for n in range(11):
    total = total + frequency[n]

for n in range(2,13):
    print(str(n)+ ':' + str(frequency[n-2]))
    






