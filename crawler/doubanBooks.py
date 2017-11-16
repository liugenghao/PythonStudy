__Author__ = 'Bill Lau'
import requests
import re
content = requests.get('http://book.douban.com').text
# print(content)
regex = '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?"author">\s*(.*?)\s*<.*?="abstract">\s*(.*?)\s*</p'

result = re.findall(regex,content,re.S)
for item in result:
    print(re.sub('&nbsp;/&nbsp','',item[2]))