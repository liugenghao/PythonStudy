from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.core.paginator import Paginator#分页
from app01 import models
# Create your views here.
#初始化数据库
def initialDatabase():
    from app01 import BaseData
    # models.
#登录验证装饰器
def auth(func):
    def inner(request,*args,**kwargs):
        is_login = request.session.get('is_login')
        if not is_login:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner
from django.views.decorators.csrf import csrf_protect#csrf保护
@csrf_protect
def login(request):
    error = '用户名密码错误'
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = models.UserInfo.objects.filter(username=username,pwd=pwd).first()
        res = redirect('/userInfo/')
        import datetime
        current_time = datetime.datetime.utcnow()
        current_time = current_time + datetime.timedelta(days=1)
        # res.set_signed_cookie('user',username,salt='key')#cookie加密，salt为秘钥
        # res.set_cookie('user', username,max_age=36000)
        # res.set_cookie('user',username,max_age=10)#max_age cookies 10秒过期
        res.set_cookie('user',username,expires=current_time,httponly=True)#expires cookies 一天后过期
        if user:
            #生成随机字符串
            #写到用户浏览器cookie
            #保存到session中
            #在随机字符串对应的字典中设相关内容
            request.session.set_expiry(3600)#设置过期时间（单位秒）---60分钟
            request.session['username'] =  user.username
            request.session['is_login'] = True
            return res
        else:
            return render(request, 'login.html',{'error':error})
#注销
def logout(request):
    # del request.session['is_login']
    request.session.clear()
    return redirect('/login/')
#抓取豆瓣首页书籍
def bookCrawler():
    import requests
    import re
    content = requests.get('http://book.douban.com').text
    # print(content)
    regex = '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?"author">\s*(.*?)\s*<.*?="abstract">\s*(.*?)\s*</p'
    result = re.findall(regex, content, re.S)
    for item in result:
        name = item[1]
        author = re.sub('&nbsp;/&nbsp','',item[2])
        url = item[0]
        abstract = item[3]
        author = models.Authors.objects.create(name=author)
        book = models.Books.objects.create(name=name,url=url,abstract=abstract)
        models.author_m2m_book.objects.create(aobj_id=author.id,bobj_id=book.id)
#书籍列表
def bookInfo(request):
    itemNum = request.COOKIES.get('pageNum', 10)  # 每页信息条数
    pageRange = 8  # 分页范围
    # types = models.UserType.objects.all()
    books = models.Books.objects.values('id', 'name', 'url', 'abstract', 'createTime',
                                           'updateTime','author_m2m_book__aobj__name').order_by("id")
    p_obj = Paginator(books, itemNum)  # 分页
    restPages = p_obj.num_pages - p_obj.num_pages % (pageRange+1)  # 最后一面之前的页数
    p = request.GET.get('p', 1)
    if int(p) > p_obj.num_pages:  # 防止页码超过阈值
        p = p_obj.num_pages
    books = p_obj.page(p)
    return render(request, 'book_info.html',
                  {'books': books,  'pageRange': pageRange, 'restPages': restPages, 'itemNum': itemNum})

#抓取淘宝美食
def foodCrawler(resp):
    from pyquery import PyQuery
    import re
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    browser = webdriver.PhantomJS(service_args=['--load-images=false', '--disk-cache=true'])
    wait = WebDriverWait(browser, 10)
    browser.set_window_size(1400, 900)

    # 获取商品详情
    def get_products():
        print('获取商品详情')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
        html = browser.page_source
        doc = PyQuery(html)
        items = doc('#mainsrp-itemlist .items .item').items()
        for item in items:
            image_url = item.find('.pic .img').attr('src')
            if not image_url:
                image_url = ''
            food = models.Food.objects.create(title=item.find('.title').text(),
                                              shopname=item.find('.shop').text(),
                                              location=item.find('.location').text(),
                                              deal=item.find('.deal-cnt').text(),
                                              image_url=image_url,
                                              price=item.find('.price').text(),
                                              product_url=item.find('.pic-link').attr('href'))
            # product = {
            #     'href':item.find('.pic-link').attr('href'),
            #     'image': item.find('.pic .img').attr('src'),
            #     'price': item.find('.price').text(),
            #     'deal': item.find('.deal-cnt').text(),
            #     'title': item.find('.title').text(),
            #     'shop': item.find('.shop').text(),
            #     'location': item.find('.location').text()
            # }
            # print(product)

    # 开始搜索
    def search():
        print('开始爬取...')
        try:
            browser.get('https://www.taobao.com')
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))  # 选中搜索栏
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))  # 选中搜索栏
            )
            input.send_keys('美食')
            submit.click()
            total = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
            return total.text
        except TimeoutException:
            return search()

    # 下一页
    def next_page(page_number):
        print('当前页面：', page_number)
        try:
            input = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
            )
            submit = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page_number)
            submit.click()
            wait.until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),
                    str(page_number))
            )
            get_products()
        except TimeoutException:
            next_page(page_number)
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        for i in range(2,total+1):
            next_page(i)
    except Exception as e:
        print(e)
    finally:
        browser.close()
    return HttpResponse(resp)
#淘宝美食列表
def taobaoFood(request):
    itemNum = request.COOKIES.get('pageNum', 10)  # 每页信息条数
    pageRange = 12 # 分页范围
    types = models.UserType.objects.all()
    food = models.Food.objects.values('id', 'title', 'shopname', 'location', 'deal',
                                           'price','image_url','product_url').order_by("id")
    p_obj = Paginator(food, itemNum)  # 分页
    if p_obj.num_pages % pageRange == 0:
        restPages = p_obj.num_pages - pageRange + 1 # 最后一面之前的页数
    else:
        restPages = p_obj.num_pages - p_obj.num_pages % pageRange + 1
    p = request.GET.get('p', 1)
    if int(p) > p_obj.num_pages:  # 防止页码超过阈值
        p = p_obj.num_pages
    food = p_obj.page(p)
    return render(request, 'taobao_food.html',
                  {'food': food,  'pageRange': pageRange, 'restPages': restPages, 'itemNum': itemNum})
def temp(request):
    food = models.Food.objects.values('id', 'title', 'shopname', 'location', 'deal',
                                      'price', 'image_url', 'product_url').order_by("id")

    return render(request, 'temp.html',{'food': food })
def callForBidCrawler(request):
    from urllib.parse import urlencode
    import requests
    from requests.exceptions import RequestException
    import json
    from bs4 import BeautifulSoup
    from multiprocessing import Pool
    import re
    def get_page_index(offset):
        data = {
            'pageing': offset,
        }
        url = 'http://www.ycztb.com/TPFront/jyxx/003001/003001001/003001001002/?pageing=' + str(offset)
        response = requests.get(url)
        try:
            if response.status_code == 200:
                # print(response.text)
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

    def parse_page_detail(html):
        soup = BeautifulSoup(html, 'lxml')
        items = soup.select('.list-item')
        for item in items:
            print(item.a.get_text())
        # images_pattern = re.compile('gallery: JSON.parse\((.*?)\),', re.S)
        # result = re.search(images_pattern, html)
        # if result:
        #     data = result.group(1)
        #     data = data.replace('\\', '')
        #     data = data[1:-1]
        #     data = json.loads(data)
        #     # print(data)
        # if data and 'sub_images' in data.keys():
        #     sub_images = data.get('sub_images')
        #     # print(sub_images)
        #     images = [item.get('url') for item in sub_images]
        #     return {
        #         'title': title,
        #         'url': url,
        #         'images': images
        #     }

    def main(offset):
        html = get_page_index(offset)
        parse_page_detail(html)
        # for url in get_page_url(html):
        #     html = get_page_detail(url)
        #     if html:
        #         result = parse_page_detail(html, url)
        #         print(result)
    main(1)
    return HttpResponse(request)
def callForBidInfo(request):
    return render(request, 'call_for_bid_info.html')
@csrf_protect
@auth
def userInfo(request):
    # loginUser = request.COOKIES.get('user')
    # loginUser = request.get_signed_cookie('user',salt='key')
    # if not loginUser:
    #     return redirect('/login/')
    itemNum = request.COOKIES.get('pageNum',10)#每页信息条数
    # print('pageNum:',pageNum)
    pageRange = 8#分页范围
    types = models.UserType.objects.all()
    # for i in range(390):
    #     models.UserInfo.objects.create(username='liugenghao'+str(i),pwd='123qwe'+str(i),email='liugenghao'+str(i)+'@sinc.com',gender='男',user_type_id=1)
    users = models.UserInfo.objects.values('id','username','user_type__name','pwd','email','gender','createTime','updateTime').order_by("id")
    p_obj = Paginator(users,itemNum)#分页
    restPages =  p_obj.num_pages - p_obj.num_pages % pageRange + 1# 最后一面剩余前的页数
    p = request.GET.get('p',1)
    if int(p) > p_obj.num_pages:#防止页码超过阈值
        p = p_obj.num_pages
    users = p_obj.page(p)
    return render(request,'user_info.html',{'users':users,'types':types,'pageRange':pageRange,'restPages':restPages,'itemNum':itemNum})

@auth
def userTypeInfo(request):
    # loginUser = request.get_signed_cookie('user',salt='key')
    # if not loginUser:
    #     redirect('/login/')
    types = models.UserType.objects.all()
    return render(request,'user_type_info.html',{'types':types})
def addUser(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    user_type = request.POST.get('user_type')

    user_type = models.UserType.objects.filter(name=user_type).first()
    users = models.UserInfo.objects.create(username=username,pwd=pwd,email=email,gender=gender,user_type=user_type)
    return HttpResponse('done')

def addUserType(request):
    typename = request.POST.get('typename')
    models.UserType.objects.create(name=typename)
    return HttpResponse('Add done')
def deleteUserType(request):
    id = request.POST.get('id')
    models.UserType.objects.filter(id=id).delete()
    return HttpResponse('Delete done')
def deleteUser(request):
    id = request.POST.get('id')
    obj = models.UserInfo.objects.filter(id=id).first()
    name = obj.username
    data = name + ' has been removed'
    obj.delete()
    return HttpResponse(data)
def modifyUser(request):
    id = request.POST.get('id')
    user_type = request.POST.get('user_type')
    user = models.UserInfo.objects.filter(id=id).first()
    user.username = request.POST.get('username')
    user.pwd = request.POST.get('pwd')
    user.email = request.POST.get('email')
    user.gender = request.POST.get('gender')
    user.user_type = models.UserType.objects.filter(name=user_type).first()
    user.save()
    return HttpResponse('修改完毕')

