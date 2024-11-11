import random

count=1
while True:
    if random.choice(range(10000))==111:
        break
    print("let me out")
    count +=1

print("At last ",count)