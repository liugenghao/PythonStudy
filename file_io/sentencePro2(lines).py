jsSentence = '['
with open('statistic_cities.txt', 'r', encoding='utf-8') as f:
    for line in f:
        content = line.split(":")
        before = content[0]
        after = content[1].replace('\n', '')
        # print(int(int(after)/50))
        # if int(after) <= 200:
        #     after = 200
        # for i in range(int(int(after)/200)):
        jsSentence += "[{ name: '宜昌' }, { name: '" + before + "'}],"
    jsSentence += ']'
    print(jsSentence)
with open('linesDataJs.txt', 'w', encoding='utf-8') as f2:
    f2.write(jsSentence)