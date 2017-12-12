__Author__ = 'Bill Lau'
import requests
from requests.exceptions import ConnectionError
from urllib.parse import urlencode
from pyquery import PyQuery
base_url = 'http://weixin.sogou.com/weixin?'
keyword = '风景'
headers = {
    'Cookie':'SUID=9BAD2CAB2613910A0000000059F1CB01; IPLOC=CN4205; SUV=00C75A9EAB2CAD9B59F1CB019C8A2495; ld=Mkllllllll2BDtsflllllVozG21lllll$hhHuZllll9lllllpklll5@@@@@@@@@@; SNUID=E036B433999CC67B344F432D99E6CC3E; usid=4mp2T4IqVthgX2g9; ABTEST=1|1511957812|v1; weixinIndexVisited=1; sct=2; JSESSIONID=aaa9uuFag1Tll8KiiNv8v; ppinf=5|1511957842|1513167442|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTUlODglOTglRTglODAlQkYlRTYlOTglOEF8Y3J0OjEwOjE1MTE5NTc4NDJ8cmVmbmljazoyNzolRTUlODglOTglRTglODAlQkYlRTYlOTglOEF8dXNlcmlkOjQ0Om85dDJsdUVKQmhIalJPbGlJbWxfaS1WMVNiRDBAd2VpeGluLnNvaHUuY29tfA; pprdig=G1PuNrDx5A5-bhi08hkujhrxmtNJIkaj5yiQnvTxfBvNjGLE47PFeDsleErAgCl0_v8BnNWtiGC0GfoUIJ0yrf-tRvVtrKHkWtkcUre5cU5uBmZBGe43mzz-R-sFPYujLcsIvPaucU1D7NDrDqkzf6ppvOnAlbk-ugNCXAanbQk; sgid=07-30107929-AVoepVJzjxfWKPTBDyPPiaFM; ppmdig=151195784400000060cd6e56bc107c6e6c80f24e1ac48572',
    'Host':'weixin.sogou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'
}
proxy_pool_url = 'http://localhost:5000/get'
proxy = None
def parse_index(html):
    doc = PyQuery(html)
    items = doc('.news-box .news-list li a').items()
    for item in items:
        yield item.attr('href')
def get_proxy():
    try:
        respoonse = requests.get(proxy_pool_url)
        if respoonse.status_code == 200:
            return respoonse.text
    except ConnectionError:
        return None
def get_html(url):
    print('Crawler',url)
    global proxy
    try:
        if proxy:
            proxies = {
                'http':'http://'+proxy
            }
            response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            print('No proxy......')
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:#更换IP，设置代理
            print('IP被封，更换代理后访问...')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy:',proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred',e.args)
        proxy = get_proxy()
        return get_html(url)

def get_index(keyword,page):
    data={
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def main():
    for page in range(1,101):
        html = get_index(keyword,page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                print(article_url)
if __name__ == '__main__':
    main()



