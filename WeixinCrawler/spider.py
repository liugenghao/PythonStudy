__Author__ = 'Bill Lau'
import requests
from requests.exceptions import ConnectionError
from urllib.parse import urlencode
base_url = 'http://weixin.sogou.com/weixin?'
keyword = '风景'
headers = {
    'Cookie':'SUID=2383B66F3020910A000000005A1A64B6; usid=_Fd8xPqkrn_lkdFt; SUV=004317506FB683235A1A64B6676D1457; ld=Ekllllllll2zpu6FlllllVobEvolllllbEzRwZllll9lllllpZlll5@@@@@@@@@@; LSTMV=1431%2C361; LCLKINT=42197; IPLOC=CN4205; ABTEST=0|1511952986|v1; weixinIndexVisited=1; sct=3; JSESSIONID=aaaWCcu5bMqTl5a1yQv8v; ppinf=5|1511953222|1513162822|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTUlODglOTglRTglODAlQkYlRTYlOTglOEF8Y3J0OjEwOjE1MTE5NTMyMjJ8cmVmbmljazoyNzolRTUlODglOTglRTglODAlQkYlRTYlOTglOEF8dXNlcmlkOjQ0Om85dDJsdUVKQmhIalJPbGlJbWxfaS1WMVNiRDBAd2VpeGluLnNvaHUuY29tfA; pprdig=ECbKDg_7W9hvb7DAP2o8qAwENe7hXXcAuZQGq0CKz0ADwSqN0PePM9roEx3u4XNOxoaIhQ-pifEnXQC6U_jhE55WiJ7dip7TfHZFLYGKBXI1_HAQhZUox45eRPNe7ZsTIIwSQyUy6gAR5-DiLulM4nZinv_f2Cb5WJGiapGqQE8; sgid=07-30107929-AVoek0bNAtIgTD1qBpSyQlc; ppmdig=151195322200000073287cc64bd851eb42154e58294119fd; PHPSESSID=rsegm32eocc44b15kg9pc82ev3; SUIR=C061548DE2E7BDF8290B9732E35B8030; SNUID=DE7D4891FEF8A1E3EB2DC4E0FEE97BBA',
    'Host':'weixin.sogou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'
}
proxy_pool_url = 'http://localhost:5000/get'
proxy = None
max_count = 5
def get_proxy():
    try:
        respoonse = requests.get(proxy_pool_url)
        if respoonse.status_code == 200:
            return respoonse.text
    except ConnectionError:
        return None
def get_html(url,count=1):
    print('Crawler',url)
    print('Tyring count',count)
    global proxy
    if count >= max_count:
        print('Tried too many count')
        return None
    try:
        if proxy:
            proxies = {
                'http':'http://'+proxy
            }
            response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:#更换IP，设置代理
            proxy = get_proxy()
            if proxy:
                print('Using Proxy:',proxy)
                return get_html(url,count)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred',e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url,count)

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
        print(html)
if __name__ == '__main__':
    main()



