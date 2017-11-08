from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
import os
# Create your views here.
USER_LIST=[
    {'username':'alex','email':'test@test.com','gender':'男'}
]
for index in range(2):
    temp = {'username':'alex'+str(index),'email':'test@test.com','gender':'男'}
    USER_LIST.append(temp)

def cmdb(request):
    return HttpResponse("<h1>CMDB</h1>")

def login(request):
    # with open('templates/login.html','r',encoding='utf-8') as f:
    #     data = f.read()
    error_msg = ''
    if request.method == 'POST':
        #用户通过Post提交过来的数据
        # user = request.POST.get('user')
        # pwd = request.POST.get('pwd')
        # if user=='liugenghao' and pwd=='123qwe':
        #     #跳转
        #     return redirect('http://www.baidu.com')
        # else:
        #     error_msg = '用户名密码错误'
        # v = request.POST.get('gender')
        # v = request.POST.getlist('favor')

        file = request.FILES.get('upload')
        file_path = os.path.join('upload', file.name)
        # print(file,type(file),file.name)
        with open(file_path,'wb') as f:
            for i in file.chunks():
                f.write(i)
    return render(request,'login.html',{'error_msg':error_msg})

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        USER_LIST.append({'username':name,'email':email,'gender':gender})
    return render(request,'home.html',{'user_list':USER_LIST})
