__Author__ = 'Bill Lau'
from multiprocessing import Pool
import re
import json
import requests
from requests.exceptions import RequestException
def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36'}
        response = requests.get(url=url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return e
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?'
                         +'star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'name':item[2],
            'actor':item[3].strip(),
            'releasetime':item[4],
            'score':item[5]+item[6]
        }
def write_to_file(content):
    with open('maoyan.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
# f = open('maoyan.txt','w')
# f.write(content)