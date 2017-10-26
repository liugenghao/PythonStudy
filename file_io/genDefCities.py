# Authot:Bill Lew
import re
cities = []
with open('defaultCities','r',encoding='utf-8') as f:
    for line in f:
        s = (line.strip()).split('"')
        s = s[1]
        cities.append(s)
print(cities)
c = '北京1'
if c in cities:
    print("222")
else:
    print('none')
        # partten = re.compile('"(.*)"')
        # print(partten.findall(s))