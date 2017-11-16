__Author__ = 'Bill Lau'
from bs4 import BeautifulSoup
f = open('beautifulSoupTest','r',encoding='utf-8')
html = f.read()
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.find_all('a')[0]['title'])
# print(soup.find_all(attrs={'class':'dd-content'}))
# print(soup.find_all(class_='dd-content'))
print(soup.select('i.ic-folder-open2'))

# print(soup.head)
# print(soup.p)
