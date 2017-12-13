__Author__ = "Bill Lau"
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
from multiprocessing import Pool
import re
from management import models
from management import BaseData

def genMenus(url):#初始化菜单
    response = requests.get(url)
    try:
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            items = soup.select('.inner-hd a')
            # print(items)
            for item in items:
                code = re.match(r'.*/(\d*)', item['href'], re.S).group(1)
                name = item.get_text()
                menu = models.CFBMenuInfo.objects.filter(code=code)
                layer = len(code)/3 - 1
                url_length = len(code)
                if not menu:
                    print('生成Menu：%s---code：%s'%(name,code))
                    models.CFBMenuInfo.objects.create(code=code, name=name,layer=layer,url_length=url_length)
                if code:
                    genMenus(url+'/'+code)
    except RequestException:
        print('请求索引页出错')
def initialMenu():
    url = BaseData.TOP_URL + '/TPFront/jyxx'
    genMenus(url)

def isCrawlerPage(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return True
        else:
            return False
    except RequestException:
        print('请求索引页出错')
def genUrl():
    urls = []
    numsArr = []
    topMenus = models.CFBMenuInfo.objects.filter(layer=1)
    for menu in topMenus:
        # print('-------------------',menu.name)
        subMenus = models.CFBMenuInfo.objects.filter(code__contains=menu.code,code__startswith=menu.code)
        layers = subMenus.values('code','layer')
        for layer in layers:
            # print("layer:",layer['layer'])
            # print("code:",layer['code'])
            numsArr.append(layer['layer'])
        # print(numsArr)
        max_layer = max(numsArr)#取得当前菜单最大层数
        # print('%s-目录下最大菜单数：%s'%(menu.name,max_layer))
        codes = subMenus.filter(layer=max_layer).values('code')
        for code in codes:
            code = code.get('code')
            url = BaseData.TOP_URL + '/TPFront/jyxx'
            for i in range(1,max_layer+1):#截取各级url地址
                len = subMenus.filter(layer=i).first().url_length
                url += '/'+code[:len]
            urls.append(url)
        numsArr = []
    # for url in urls:
    #     print(url)
    return urls
def getPageNum(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            items = soup.select('.wb-page-number')
            try:
                page_num = int(items[0].get_text().split('/')[1])
                return page_num
            except IndexError:
                return 1
    except RequestException:
        print('请求索引页出错')
def getAllInfo(url):
    def crawl(url,i):
        print('爬取【%s】第【%s】页' % (url, i))
        response = requests.get(url + '/?pageing=' + str(i))
        try:
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')
                items = soup.select('.list-item')
                for item in items:
                    title = item.a.get_text()
                    article = models.CFBInfoDetail.objects.filter(title=title).first()
                    if not article:#详细信息如果还没有存入数据库
                        href = item.a['href']
                        date = item.select('.list-date')[0].get_text()
                        if href and date:
                            code = re.match(r'.*/(\d*)', url, re.S).group(1)#底层子分类
                            menu_Type = models.CFBMenuInfo.objects.filter(code=code).first()
                            href = BaseData.TOP_URL + href
                            article = models.CFBInfoDetail.objects.create(title=title, href=href, publication_date=date,
                                                                code=code)
                            # print('info_id:',article.id)
                            layer = menu_Type.layer
                            models.info_m2m_menu.objects.create(info=article,menu=menu_Type,layer=layer)
                            while layer > 1:#循环到最上层菜单
                                layer = layer - 1
                                # print(layer)
                                code = code[:menu_Type.url_length-3]#上一级菜单的code
                                menu_Type = models.CFBMenuInfo.objects.filter(code=code).first()
                                models.info_m2m_menu.objects.create(info=article, menu=menu_Type,layer=layer)


        except RequestException:
            print('请求索引页出错')
    page_num = getPageNum(url)
    if page_num > 1:
        for i in range(1,page_num+1):
            crawl(url, i)
    else:
        crawl(url, 1)
def getRangeInfo(url):
    pass
import threading
def startCrawler():
    # initialMenu()
    urls = genUrl()
    for url in urls:
        t = threading.Thread(getAllInfo(url))
        t.setDaemon(True)
        t.start()

