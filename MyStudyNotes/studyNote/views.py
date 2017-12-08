from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from studyNote import models
import json
# Create your views here.
def index(request):
    return render(request,'index.html')
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
    # print('parentID:',parentID)
    menuName = request.POST.get('menuName')
    parentMenu = models.MenusInfo.objects.filter(id=parentID).first()
    # print('parentName:',parentMenu.name)
    layer = parentMenu.layer + 1
    subMenus = models.MenusInfo.objects.filter(parentID=parentID)
    subMenusNum = subMenus.count()
    # print('subMenusNum:',subMenusNum)
    if subMenusNum == 0:
        code = parentMenu.code
        code = code + '01'
        addedMenu = models.MenusInfo.objects.create(parentID=parentID, name=menuName, code=code, layer=layer)
        # print('subMenusNum = 0')
        parentMenu.left_child = addedMenu.id
        parentMenu.save()
    else:
        modifySubMenu = subMenus.filter(right_sibling=0).first()#修改right_sibling
        code = modifySubMenu.code
        codeBefore = code[:-2]
        codeAfter = code[-2:]
        codeAfter =  int(codeAfter) + 1
        if codeAfter <= 9:
            codeAfter = '0' + str(codeAfter)
        else:
            codeAfter = str(codeAfter)
        code = codeBefore + codeAfter
        addedMenu = models.MenusInfo.objects.create(parentID=parentID, name=menuName, code=code, layer=layer)
        modifySubMenu.right_sibling = addedMenu.id
        modifySubMenu.save()
        # pass
    return HttpResponse('')
def getSubMenu(request):
    menuID = int(request.POST.get('menuID'))
    print("parentID:",menuID)
    menus = models.MenusInfo.objects.filter(parentID=menuID).all()
    print('childID:',menus.left_child)
    data = []
    for item in menus:
        data.append({'id':item.id,'name':item.name})
    data =  json.dumps(data)
    return HttpResponse(data)