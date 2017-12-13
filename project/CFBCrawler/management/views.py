from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from management import models
from django.core.paginator import Paginator  # 分页
import json
from django.utils.http import urlquote


# 菜单生成器
def genMenus(request):
    result = []
    topMenus = models.CFBMenuInfo.objects.filter(layer=1).values_list('name', 'code')
    # print(topMenus)
    for menu in topMenus:
        result.append(menu)
    # print(result)
    # result = json.dumps(list(topMenus))
    # return HttpResponse(topMenus)
    return HttpResponse(json.dumps(result, ensure_ascii=False))


# 招标信息列表
def callForBidInfo(request, code):
    code = code[:-1]
    action_url = '/callForBidInfo/' + code
    active_code = code
    sec_menu_code = request.GET.get('s')
    thd_menu_code = request.GET.get('t')
    sec_menu = None
    sec_active_code = None
    def get_article(code):
        return models.CFBInfoDetail.objects.filter(code__contains=code, code__startswith=code).values(
            'title', 'href', 'publication_date', 'code').order_by('-publication_date')
    def get_menu(code, layer):
        return models.CFBMenuInfo.objects.filter(code__contains=code, code__startswith=code,
                                                 layer=layer).values('name', 'code')

    menu_open = False#子菜单中menu默认打开
    top_cfb_menu = None
    cfb_informations = get_article(code)
    if code == '':
        cfb_informations = models.CFBInfoDetail.objects.values('title', 'href', 'publication_date', 'code').order_by(
            '-publication_date')
    else:
        menu_open = True
        top_cfb_menu = get_menu(code, 2)
        if sec_menu_code:
            sec_active_code = sec_menu_code
            sec_menu = get_menu(sec_menu_code,3)
            cfb_informations = get_article(sec_menu_code)


    total_num = cfb_informations.count()
    ################ 分页###################
    itemNum = request.COOKIES.get('pageNum', 10)  # 每页信息条数
    pageRange = 8  # 分页范围
    p_obj = Paginator(cfb_informations, itemNum)  # 分页
    if p_obj.num_pages % pageRange == 0:
        restPages = p_obj.num_pages - pageRange + 1  # 最后一面之前的页数
    else:
        restPages = p_obj.num_pages - p_obj.num_pages % pageRange + 1
    p = request.GET.get('p', 1)
    if int(p) > p_obj.num_pages:  # 防止页码超过阈值
        p = p_obj.num_pages
    cfb_informations = p_obj.page(p)
    return render(request, 'call_for_bid_info.html',
                  {'cfb_informations': cfb_informations, 'top_cfb_menu': top_cfb_menu,'sec_menu':sec_menu,
                   'pageRange': pageRange, 'restPages': restPages,'menu_open':menu_open,
                   'itemNum': itemNum, 'total_num': total_num, 'action_url': action_url,'code': code,'active_code':active_code,'sec_active_code':sec_active_code })
# 抓取
def callForBidCrawler(request):
    from management import crawler
    crawler.startCrawler()
    max_num = models.CFBInfoDetail.objects.count()
    return HttpResponse("抓取完毕~！共计%s条数据：" % max_num)
