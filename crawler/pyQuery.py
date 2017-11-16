__Author__ = 'Bill Lau'
from pyquery import PyQuery
f = open('pyQuery','r',encoding='utf-8')
html = f.read()
doc = PyQuery(html)
print(doc('p').text())
