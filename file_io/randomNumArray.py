import random
def randoNumArray(sum,n):
    _sum = sum
    numArray = []
    for i in range(n):
        factor = int(sum/n)
        tempNum = random.randint(factor,factor*2)
        numArray.append(tempNum)
        sum -= tempNum
    numArray.append(sum)
    # avNum = int(reset/n)
    # for i,k in enumerate(numArray):
    #     numArray[i] += avNum
    return numArray

arr = randoNumArray(6993020,6)
arr.sort()
sum_verify = 0
for j in arr:
    sum_verify += j

with open('randomNumArray.txt','w') as f:
    for i in arr:
        f.write(str(i))
        f.write('\n')