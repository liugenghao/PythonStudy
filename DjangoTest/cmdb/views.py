from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
import os
# Create your views here.
USER_LIST=[
    {'username':'alex','email':'test@test.com','gender':'男'}
]
USER_DICT = {
    1:{'username':'alex','email':'test@test.com','gender':'男'},
    2:{'username':'alex1','email':'test@test.com','gender':'男'},
    3:{'username':'alex2','email':'test@test.com','gender':'男'},
    4:{'username':'alex3','email':'test@test.com','gender':'男'},
    5:{'username':'alex4','email':'test@test.com','gender':'男'}

}
for index in range(5):
    temp = {'username':'alex'+str(index),'email':'test@test.com','gender':'男'}
    USER_LIST.append(temp)

def cmdb(request):
    return HttpResponse("<h1>CMDB</h1>")
#FBV
class Login(View):
    def post(self,request):
        error_msg = ''
        return render(request, 'login.html', {'error_msg': error_msg})
    def get(self,request):
        return render(request, 'login.html')


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

        # file = request.FILES.get('upload')
        # file_path = os.path.join('upload', file.name)
        # print(file,type(file),file.name)
        # with open(file_path,'wb') as f:
        #     for i in file.chunks():
        #         f.write(i)
    # return render(request,'login.html',{'error_msg':error_msg})



#CBV
class Home(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('after')
        return result
    def get(self,request):
        print('get')
        return render(request, 'home.html', {'user_list': USER_LIST})
    def post(self,request):
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        USER_LIST.append({'username':name,'email':email,'gender':gender})
        return render(request, 'home.html', {'user_list': USER_LIST})

class Index(View):
    def post(self,request):
        from django.urls import reverse
        u = reverse('index')#根据路由的名称生成当前url
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        index = len(USER_DICT) + 1
        USER_DICT[index]={'username': name, 'email': email, 'gender': gender}
        return render(request, 'index.html', {'user_dict': USER_DICT})
    def get(self,request):
        return render(request, 'index.html', {'user_dict': USER_DICT})

class Detail(View):
    def get(self,request,nid):
        # nid = request.GET.get('nid')
        detail_info = USER_DICT[int(nid)]
        return render(request,'detail.html',{'detail_info':detail_info})
from cmdb import models
class ORM(View):
    def get(self,request):
        #创建
        # usertype = models.UserType.objects.create(name = '管理员')
        # models.UserInfo.objects.create(
        #     username = 'root',
        #     pwd = '123',
        #     email = 'liugenghao@sina.com',
        #     user_type = usertype
        # )
        #查询
        result = models.UserInfo.objects.all()
        print(result)
        # obj = models.UserInfo(username='Alex',user_type=1)
        # obj.save()
        return HttpResponse('orm')