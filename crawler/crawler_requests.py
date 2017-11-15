__Author__ = 'Bill Lau'

import requests
import json
# url = 'http://www.baidu.com'
# url = 'http://www.zhihu.com'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36'}
# response = requests.get(url=url,headers=headers)
# for key,value in response.cookies.items():
#     print(key+'='+value)
# response.encoding = 'utf-8'
# # print(type(response))
# # print(response.status_code)
# # print(type(response.text))
# print(response.text)
# print(response.cookies)
# print(response.content)
# data = {'name':'germy','age':22}
# response = requests.get('http://httpbin.org/get',params=data)
# print(type(response.text))
# print(response.json())
#
# print(type(response.json()))
# print(json.loads(response.text))

#文件上传
# with open('Violin.png','rb') as f:
#     files = {'file':f}
#     response = requests.post('http://httpbin.org/post',files=files)
#     print(response.text)

#session
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# #12306
# import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn',verify=False)
# response.encoding = 'utf-8'
# print(response.text)

#代理
proxies = {
    'http':'socks5://17230:x5tK93@jp5.cdd3.com:17230',
    'https':'socks5://17230:x5tK93@jp5.cdd3.com:17230'
}
from requests.exceptions import ReadTimeout,ConnectTimeout
try:
    response = requests.get('http://www.baidu.com',proxies=proxies,timeout=2)
    print(response.status_code)
except ConnectTimeout as e:
    print(e)