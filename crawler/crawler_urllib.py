__Author__ = 'Bill Lau'
from urllib import request,parse,error
from urllib.parse import urlparse,urlunparse,urljoin,urlencode
from http import cookiejar

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

# url = 'http://httpbin.org/post'
# header={
#     'User-Agent':"Mozilla/4.0(compatible;MSIE 5.5;Windows NT)",
#     'Host':'httpbin.org'
# }
# dict={
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict),encoding='utf-8')
# req = request.Request(url=url,data=data,headers=header,method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

#切换代理 防止封IP
# proxy_handler = request.ProxyHandler({
#     'http':'http://jp5.cdd3.com:17230',
#     # 'https':'https://127.0.0.1:9743'
# })
# opener = request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

#cookie处理
# # cookie = cookiejar.CookieJar()
# filename = 'cookie.txt'
# # cookie = cookiejar.MozillaCookieJar(filename)
# cookie = cookiejar.LWPCookieJar(filename)
# # cookie.load(filename,ignore_discard=True,ignore_expires=True)#读取本地保存的cookie
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)
# cookie.save(ignore_discard=True,ignore_expires=True)#存到本地

#异常处理
# try:
#     response = request.urlopen('http://www.baid1u.com/1321kd213dl;kfsjfh1.html')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Reques Successfully!')

#url解析
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# result = urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
# # print(type(result),result)
# #拼接
# data = ['http','www.baidu.com','index.html','user','a=6','commnet']
# print(urlunparse(data))
# print(urljoin('http://www.baidu.com','FAQ.html'))
# print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com#comment','?category=2'))

#将字典转换为GET请求参数
params = {'name':'germey','age':22}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
