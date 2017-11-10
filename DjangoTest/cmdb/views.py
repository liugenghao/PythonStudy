from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views import View
from cmdb import models
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
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=user,pwd=pwd).first()
        if obj:
            return redirect('/cmdb/home/')
        else:
            error_msg = '用户名密码错误'
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
    # def dispatch(self, request, *args, **kwargs):
    #     print('before')
    #     result = super(Home,self).dispatch(request, *args, **kwargs)
    #     print('after')
    #     return result
    def get(self,request):
        # print('get')
        user_list = models.UserInfo.objects.all()
        return render(request, 'home.html', {'user_list': user_list})
    def post(self,request):
        # print('post')
        user_list = models.UserInfo.objects.all()
        return render(request, 'home.html', {'user_list': user_list})

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
        # obj = models.UserInfo.objects.filter(id=nid).first()
        # usertype = models.UserType.objects.filter(id=obj.user_type_id).first()
        # # detail_info = USER_DICT[int(nid)]
        # return render(request, 'detail.html', {'user_info': obj, 'user_type': usertype})
        user_types = models.UserType.objects.all()
        obj = models.UserInfo.objects.filter(id=nid).values('id','username','pwd','gender','email','user_type__name').first()
        return render(request,'detail.html',{'user_info':obj,'user_types':user_types})

class ORM(View):
    def get(self,request):
        #创建
        # usertype = models.UserType.objects.create(name = 'admin')
        # models.UserInfo.objects.create(
        #     username = 'root',
        #     pwd = '123',
        #     email = 'liugenghao@sina.com',
        #     user_type = usertype
        # )
        #修改
        models.UserInfo.objects.filter(username='bill').update(pwd='111qqq')
        #查询
        # usertype = models.UserType.objects.filter(name="admin").first()
        #
        #
        # obj = models.UserInfo(username='Bill',email='bill@sina.com',user_type=usertype)
        # obj.save()
        #删除
        models.UserInfo.objects.filter(id=2).delete()
        return HttpResponse('orm')
class AddUser(View):
    def post(self,request):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        usertype = request.POST.get('type')
        gender = request.POST.get('gender')
        usertype = models.UserType.objects.filter(name=usertype).first()
        models.UserInfo(username=username,pwd=pwd,email=email,gender=gender,user_type=usertype).save()
        return redirect('/cmdb/home/')
    def get(self,request):
        usertypes = models.UserType.objects.all()
        users = models.UserInfo.objects.all()
        return render(request,'adduser.html',{'usertypes':usertypes,'users':users})
class AddGroup(View):
    def post(self,request):
        groupName = request.POST.get('groupname')
        usertype = models.UserType.objects.create(name=groupName)
        groups = models.UserType.objects.all()
        return render(request, 'addgroup.html', {'usertypes': groups})
    def get(self,request):
        groups = models.UserType.objects.all()
        # print(groups[0].name)
        return render(request,'addgroup.html',{'usertypes':groups})
class DeleteUser(View):
    def get(self,request,id):
        models.UserInfo.objects.filter(id=id).delete()
        return redirect('/cmdb/adduser/')
class DeleteGroup(View):
    def get(self,request,id):
        models.UserType.objects.filter(id=id).delete()
        return redirect('/cmdb/addgroup/')

class EditUser(View):
    def post(self,request,*args):
        id = request.POST.get('uid')
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        usertype = request.POST.get('type')
        usertype = models.UserType.objects.filter(name=usertype).first()
        models.UserInfo.objects.filter(id=id).update(username=username, pwd=pwd, gender=gender, email=email, user_type=usertype)
        return redirect('/cmdb/adduser/')
        # return HttpResponse('Done')
    def get(self,request,id):
        user = models.UserInfo.objects.filter(id=id).first()
        usertypes = models.UserType.objects.all()
        usertype = models.UserType.objects.filter(id=user.user_type_id).first()
        return render(request, 'edituser.html', {'user': user,'usertypes':usertypes,'usertype':usertype})

def ajax_test(request):
    id = request.POST.get('uid')
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    usertype = request.POST.get('type')
    usertype = models.UserType.objects.filter(name=usertype).first()
    models.UserInfo.objects.filter(id=id).update(username=username, pwd=pwd, gender=gender, email=email,
                                                 user_type=usertype)
    return HttpResponse('Done')