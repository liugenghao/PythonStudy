dict = {}
lineNum = 0
PROVINCE = []
with open("china_province.txt",'r',encoding='utf-8') as f0:
    for line in f0:
        province = line.strip()
        PROVINCE.append(province)
with open("data.txt",'r',encoding='utf-8') as f:
    for line in f:
        lineNum += 1
        # line = f.readline()
        content = line.strip().encode('utf-8').decode('utf-8-sig')
        content = content.split(' ')
        s = list(filter(lambda x:x!='',content))
        # print(s)
        if s:
            s = s[0].split('\t')
            # print(s[0])
        if len(s)>1:
            s = s[1]
        if ',' in s:
            s = s.split(',')
            s = s[0].strip('"')
        for item in PROVINCE:
            if item in s:
                s = item

        if s!='' and isinstance(s,str):
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
                # print(str)
dict = sorted(dict.items(),key=lambda item:item[1],reverse=True)
print(dict)
print("-------------------------------------------------")
print("LineNums = %d" %lineNum)
print("-------------------------------------------------")
with open("statistic_provinces.txt",'w',encoding='utf-8') as f2:
    sum = 0
    for item in dict:
        print("%s:%s" %(item[0],item[1]))
        f2.write("%s:%s\n" %(item[0],item[1]))
        sum += item[1]
print("-------------------------------------------------")
print("Sum = %d" % sum)
print("-------------------------------------------------")
