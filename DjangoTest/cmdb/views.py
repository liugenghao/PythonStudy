from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
# Create your views here.

def cmdb(request):
    return HttpResponse("<h1>CMDB</h1>")
def login(request):
    # with open('templates/login.html','r',encoding='utf-8') as f:
    #     data = f.read()
    error_msg = ''
    if request.method == 'POST':
        #用户通过Post提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user=='liugenghao' and pwd=='123qwe':
            #跳转
            return redirect('http://www.baidu.com')
        else:
            error_msg = '用户名密码错误'
    return render(request,'login.html',{'error_msg':error_msg})
