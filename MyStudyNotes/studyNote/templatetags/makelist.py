__Author__ = 'Bill Lau'

from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from studyNote import models

register = template.Library()

@register.simple_tag
def generatelist():
    html = []
    menus = models.MenusInfo.objects.all()
    def insertElement(html,content):
        return html[0:-5]+content+html[-5:]
    for row in menus:
        if not row.parentID:
            tempHtml = '<li id="' + str(row.id) + '"><a href = "javascript:void(0)">' + row.name + '</a> <i class ="fa fa-plus"></i></li>'
            childMenus = models.MenusInfo.objects.filter(parentID=row.id)
            subULHtml = ''
            for children in childMenus:
                subULHtml += '<li id="' + str(children.id) + '"><a href = "javascript:void(0)">' + children.name + '</a> <i class ="fa fa-plus"></i></li>'
                childrens2 = models.MenusInfo.objects.filter(parentID=children.id)
                subULHtml2 = ''
                for children2 in childrens2:
                    subULHtml2 += '<li id="' + str(children2.id) + '"><a href = "javascript:void(0)">' + children2.name + '</a> <i class ="fa fa-plus"></i></li>'
                subULHtml2 = insertElement('<ul></ul>', subULHtml2)
                subULHtml = insertElement(subULHtml,subULHtml2)
            subULHtml = insertElement('<ul></ul>', subULHtml)
            tempHtml = insertElement(tempHtml, subULHtml)
            html.append(tempHtml)

    html = ''.join(html)
    print(html)
    return format_html(html)



