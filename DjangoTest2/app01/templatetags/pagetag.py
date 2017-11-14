__Author__ = "Bill Lau"

from django import template
from  django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
#分页curr_page：当前页面值，max_page：总页面数，page_range：分页范围
def circle_page(curr_page,max_page,page_range):
    if max_page < page_range:
        page_range = max_page
    a_pages = []
    # if max_page/page_range > 2:
    if curr_page <= page_range:
        start_num = 1
    else:
        if curr_page%page_range != 0:#不可除尽时的初始值
            start_num = int(curr_page/page_range)*page_range + 1
        else:#可以除尽时的初始值
            start_num = curr_page - page_range + 1
        a_pages.append('<li><a href="/userInfo/?p=%s">...</a></li>' % (start_num-1))  # 省略号，直接跳转到上一个范围

    end_num = start_num+page_range#末尾值
    if end_num > max_page:#末位數如果小于页面总数则等于页面最大数
        end_num = max_page + 1

    for i in range(start_num,end_num):
        if i == curr_page:
            temp = '<li class="actived"><a href="/userInfo/?p=%s">%s</a></li>'%(i,i)
        else:
            temp = '<li><a href="/userInfo/?p=%s">%s</a></li>' % (i, i)
        a_pages.append(temp)
    if end_num < max_page:
        a_pages.append( '<li><a href="/userInfo/?p=%s">...</a></li>' % (end_num))#省略号，直接跳转岛下一个范围
    page_str = ''.join(a_pages)
    return format_html(page_str)

@register.filter
def test2(str1,str2):
    return str1 + str2