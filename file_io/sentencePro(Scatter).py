# Author:Bill Lew

jsSentence = '['
with open('statistic_cities.txt', 'r', encoding='utf-8') as f:
    for line in f:
        content = line.split(":")
        before = content[0]
        after = content[1].replace('\n', '')
        jsSentence += "[[{ name: '夷陵' }, { name: '" + before + "', value:" + after + "}]],"
    jsSentence += ']'
with open('scatterDataJs.txt', 'w', encoding='utf-8') as f2:
    f2.write(jsSentence)


jsSentence2 = '['
with open('statistic_cities_top5.txt', 'r', encoding='utf-8') as f3:
    for line in f3:
        content = line.split(":")
        before = content[0]
        after = content[1].replace('\n', '')
        jsSentence2 += "[[{ name: '夷陵' }, { name: '" + before + "', value:" + after + "}]],"
    jsSentence2 += ']'
with open('scatterDataJs_top5.txt', 'w', encoding='utf-8') as f4:
    f4.write(jsSentence2)




