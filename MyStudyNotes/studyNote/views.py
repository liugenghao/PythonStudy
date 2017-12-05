from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from studyNote import models
import json
# Create your views here.
def index(request):
    menus = models.MenusInfo.objects.all()
    # menus2 = models.MenusInfo.objects.o
    # print(menus.first().name)
    return render(request,'index.html',{"menus":menus})
def addTopMenu(request):
    menuName = request.POST.get('menuName')
    lastTopMenu = models.MenusInfo.objects.filter(layer=1).order_by('code').last()
    if lastTopMenu:
        code = int(lastTopMenu.code)+ 1
        if code <= 9:
            code = '0'+ str(code)
        else:
            code = str(code)
        addedMenu = models.MenusInfo.objects.create(name=menuName, code=code, layer=1)
        lastTopMenu.right_sibling=addedMenu.id
        lastTopMenu.save()
    else:
        addedMenu = models.MenusInfo.objects.create(name=menuName,code='01',layer=1)
    return HttpResponse('')
def addSubMenu(request):
    parentID =  int(request.POST.get('menuID'))
    menuName = request.POST.get('menuName')
    parentMenu = models.MenusInfo.objects.filter(id=parentID).first()
    if not parentMenu.left_child:
        code = parentMenu.code
        code = code + '01'
        layer = parentMenu.layer+1
        addedMenu = models.MenusInfo.objects.create(parentID=parentID, name=menuName, code=code, layer=layer)
        parentMenu.left_child = addedMenu.id
        parentMenu.save()
    return HttpResponse('')
def getSubMenu(request):
    menuID = int(request.POST.get('menuID'))
    menu = models.MenusInfo.objects.filter(id=menuID).first()
    data = []
    def getChild(menu):
        if menu.left_child:
            subMenu = models.MenusInfo.objects.filter(id=menu.left_child).first()
            data.append({'id':subMenu.id,'name':subMenu.name})
            return getChild(subMenu)
    print(data)
    return HttpResponse('')