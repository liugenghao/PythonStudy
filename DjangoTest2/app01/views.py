from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator#分页
from app01 import models
# Create your views here.
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
def bookInfo(request):
    import requests
    import re
    # content = requests.get('http://book.douban.com').text
    # # print(content)
    # regex = '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?"author">\s*(.*?)\s*<.*?="abstract">\s*(.*?)\s*</p'
    # result = re.findall(regex, content, re.S)
    # for item in result:
    #     name = item[1]
    #     author = re.sub('&nbsp;/&nbsp','',item[2])
    #     url = item[0]
    #     abstract = item[3]
    #     author = models.Authors.objects.create(name=author)
    #     book = models.Books.objects.create(name=name,url=url,abstract=abstract)
    #     models.author_m2m_book.objects.create(aobj_id=author.id,bobj_id=book.id)

    itemNum = request.COOKIES.get('pageNum', 10)  # 每页信息条数
    # print('pageNum:',pageNum)
    pageRange = 8  # 分页范围
    types = models.UserType.objects.all()
    # for i in range(390):
    #     models.UserInfo.objects.create(username='liugenghao'+str(i),pwd='123qwe'+str(i),email='liugenghao'+str(i)+'@sinc.com',gender='男',user_type_id=1)
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



