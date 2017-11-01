
import random
sum = 6993020
n = 0
numbers = []
for i in range(6):
    print(i)
    if i < 2:
        n = random.randint(0,sum/2)
        sum = sum - n
        numbers.append(n)
    elif i>=2 and i <5:
        n = random.randint(0, sum)
        sum = sum - n
        numbers.append(n)
    elif i == 5:
        numbers.append(sum)

print(sorted(numbers))
sum2 = 0
for i in numbers:
    print(i)
    sum2 = sum2 + i
print("sum2=",sum2)