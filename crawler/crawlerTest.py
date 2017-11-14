__Author__ = 'Bill Lau'
from urllib import request,parse,error

# response = request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(response.getheaders())
# print(response.getheader('date'))


# data = bytes(parse.urlencode({'world':'hello'}),encoding='utf-8')
# response = request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# response = request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())

# try:
#     response = request.urlopen('http://httpbin.org/get',timeout=0.1)#设置超时时间
#     print(response.read())
# except error.URLError as e:
#     print(e)

url = 'http://httpbin.org/post'
header={
    'User-Agent':"Mozilla/4.0(compatible;MSIE 5.5;Windows NT)",
    'Host':'httpbin.org'
}
dict={
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=header,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))