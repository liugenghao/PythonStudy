# Author:Bill Lew
import re
cities = []
with open('defaultCities','r',encoding='utf-8') as f:
    for line in f:
        s = (line.strip()).split('"')
        s = s[1]
        cities.append(s)
# print(cities)
dict = {}
lineNum = 0
def txt_wrap_by(start_str, end, word):
    start = word.find(start_str)
    # print("start:",type(start))
    if start >= 0:
        start += len(start_str)
        end = word.find(end, start)
        if end >= 0:
            return word[start:end].strip()
    return False


cities1 = 0
with open("data.txt",'r',encoding='utf-8') as f:
    for line in f:
        lineNum += 1
        content = line.encode('utf-8').decode('utf-8-sig')
        content = content.split(' ')
        s = ''
        if len(content) <=2:
            content = content[0].strip().split()
            if len(content) > 1:
                content = content[1]
                if txt_wrap_by(',','市',content):
                    s = txt_wrap_by(',','市',content)
                elif txt_wrap_by('区','市',content):
                    s = txt_wrap_by('区','市',content)
        else:
            s = content[1].replace('市','')


        # s = list(filter(lambda x:x!='',content))
        # s = s[1].replace('市','').strip()
        # # s = s.split(' ')
        # index = s.find('\t')
        # if index != -1:
        #     s = s[index:].strip()
        if s in cities:
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
        # if s:
        #     s = s[0].split('\t')
        #     print(s[0])

# if s!='' and isinstance(s,str) and len(s) <= 4 and len(s) != 1 and not '省' in s:
#             match = re.search('^[a-zA-Z]+$', s)
#             if not match:
# print(sorted(dict.items(),key=lambda item:item[1],reverse=True))

print("-------------------------------------------------")
print("LineNums = %d" %lineNum)
print("-------------------------------------------------")
with open("statistic_cities.txt",'w',encoding='utf-8') as f2:
    for k in dict:
        # print("%s:%d" % (k, dict[k]))
        f2.write("%s:%d\n" %(k,dict[k]))
print("-------------------------------------------------")
print("-------------------------------------------------")

with open("statistic_cities_top5.txt",'w',encoding='utf-8') as f3:
    for k in dict:
        if dict[k] > 890:
            # print("%s:%d" % (k, dict[k]))
            f3.write("%s:%d\n" %(k,dict[k]))

with open("statistic_cities_res.txt",'w',encoding='utf-8') as f4:
    for k in dict:
        if dict[k] < 890:
            # print("%s:%d" % (k, dict[k]))
            f4.write("%s:%d\n" %(k,dict[k]))