__Author__ = 'Bill Lau'
import requests
import re
content = requests.get('http://book.douban.com').text
# print(content)
regex = '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?="author".*?(.*?)<.*?="abstract"\s*(.*?)\s*</p'

result = re.findall(regex,content,re.S)
print(result)