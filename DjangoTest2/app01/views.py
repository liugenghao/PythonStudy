from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.

def index(request):
    return render(request,'_layout_index.html')

def userInfo(request):
    types = models.UserType.objects.all()
    users = models.UserInfo.objects.values('id','username','pwd','email','gender','createTime','updateTime','user_type__name')
    return render(request,'user_info.html',{'users':users,'types':types})

def addUser(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    gender = request.POST.get('gender')
    user_type = request.POST.get('user_type')

    user_type = models.UserType.objects.filter(name=user_type).first()
    users = models.UserInfo.objects.create(username=username,pwd=pwd,email=email,gender=gender,user_type=user_type)
    return redirect('/app01/userInfo/')
    # return HttpResponse('done')
def userTypeInfo(request):
    types = models.UserType.objects.all()
    return render(request,'user_type_info.html',{'types':types})
def addUserType(request):
    typename = request.POST.get('typename')
    models.UserType.objects.create(name=typename)
    return redirect('/app01/userTypeInfo/')
def deleteUserType(request):
    id = request.POST.get('id')
    models.UserType.objects.filter(id=id).delete()
    return redirect('/app01/userTypeInfo/')
