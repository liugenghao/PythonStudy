__Author__ = 'Bill Lau'

import re

# content = 'Extra Hello 1234567 World_This is a Regex Demo Extra'
# result = re.sub('\d+','tihuan',content)#替换
# result = re.sub('(\d+)',r'\1 替换',content)#包含原字符串一起替换
# print(result)
# # regex = '^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$'
# regex = 'Hello.*?(\d+).*?Demo'
# # result = re.match(regex,content,re.S)#re.S匹配所有字符 包含\n等
# result = re.search(regex,content)

#读取文档
f = open('regextest','r',encoding='utf-8')
content = f.read()

# print(content)
# regex = '<a.*?title=".*?">(.*?)<'
# regex = '<a.*?title="(.*?)">(.*?)<'
regex = '<div.*?>\s*|<i.*?>\s*|</div>\s*|</i>\s*'
result = re.sub(regex,'',content)
print(result)
# result = re.findall(regex,content,re.S)
# print(result)
# print(result.group(1))
# i = 1
# for item in result:
#     print(str(i)+'.'+item[0]+':'+item[1])
#     i+=1
# print(result.span())



