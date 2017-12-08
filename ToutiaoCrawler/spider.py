__Author__ = 'Bill Lau'
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
from multiprocessing import Pool
import re
def get_page_index(offset,keyword):
    data ={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None
def get_page_detail(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None
def get_page_url(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile('gallery: JSON.parse\((.*?)\),',re.S)
    result = re.search(images_pattern,html)
    if result:
        data = result.group(1)
        data = data.replace('\\','')
        data = data[1:-1]
        data = json.loads(data)
        # print(data)
        if data and 'sub_images'in data.keys():
            sub_images = data.get('sub_images')
            # print(sub_images)
            images = [item.get('url') for item in sub_images]
            return {
                'title':title,
                'url':url,
                'images':images
            }
def main(offset):
    html = get_page_index(offset,'街拍')
    for url in get_page_url(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            print(result)

if __name__ == '__main__':
    groups = [x * 20 for x in range(1,20 + 1)]
    pool = Pool()
    pool.map(main,groups)
    pool.close()
    pool.join()