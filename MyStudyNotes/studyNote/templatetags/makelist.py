__Author__ = 'Bill Lau'

from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from studyNote import models

register = template.Library()

@register.simple_tag
def generatelist():
    # # html = '''<li><a href = "javascript:void(0)"> </a> <i id = ""class ="fa fa-plus" > </i></li>'''
    # html = []
    # menusArr = {}
    # menus = models.MenusInfo.objects.all()
    # print(type(menus))
    # def getMenusArr(menus):
    #     for row in menus:
    #         if row.left_child:
    #             menusArr[row.name] = {}
    #             return getMenusArr(menus)
    #                 # html.append('<li><a href = "javascript:void(0)">'+row.name+'</a><i id = ""class ="fa fa-plus" ></i></li>')
    #         else:
    #             menusArr[row.name] = row.name
    #     return menusArr
    # print(menusArr(menusArr))
    # html = ''.join(html)
    return format_html(html)



