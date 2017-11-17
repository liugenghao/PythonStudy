__Author__ = 'Bill Lau'
#与JQuery操作相同
from pyquery import PyQuery
f = open('pyQuery','r',encoding='utf-8')
html = f.read()
doc = PyQuery(html)
# list = doc('p').items()
# print(type(list))
# for k,v in enumerate(list):
#     print(k+1,v.text())

imgs = doc('img').items()
imgs2 = doc('img')
print(imgs2)
#     # print(i.attr.src)
#     print(i.attr('src'))