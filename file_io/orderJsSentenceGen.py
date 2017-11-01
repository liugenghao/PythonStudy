import random
order = []
with open("data.txt",'r',encoding='utf-8') as f:
    count = 0
    for line in f:
        # line = f.readline()
        content = line.encode('utf-8').decode('utf-8-sig')
        content = content.replace('\t', ' ')
        order.append(content.strip())
        count += 1
        if count > 20000:
            break
random.shuffle(order)
# print(order)
jsSentence = '['
with open("orderJsSentence.txt",'w',encoding='utf-8') as f2:
    for line in order:
        jsSentence += "'"+line+"',"
    jsSentence += ']'
    f2.write(jsSentence)