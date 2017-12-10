from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from management import models
from django.core.paginator import Paginator#分页
import json
from django.utils.http import urlquote
#菜单生成器
def genMenus(request):
    result = []
    topMenus = models.CFBMenuInfo.objects.filter(layer=1).values_list('name','code')
    for menu in topMenus:
        result.append(menu)
    # result = json.dumps(list(topMenus))
    # return HttpResponse(topMenus)
    return HttpResponse(json.dumps(result,ensure_ascii=False))
#招标信息列表
def callForBidInfo(request):
    itemNum = request.COOKIES.get('pageNum', 10)  # 每页信息条数
    pageRange = 8  # 分页范围
    url = request.get_raw_uri()
    # print(url)
    action_str = '/callForBidInfo/'
    pos = url.find(action_str)+len(action_str)
    code = url[pos:-1]
    # print(code)
    menu_open = False
    if code:
        menu_open = True;
        cfb_informations = models.CFBInfoDetail.objects.filter(code__contains=code, code__startswith=code).values(
            'title', 'href', 'publication_date', 'code').order_by('-publication_date')
    else:
        cfb_informations = models.CFBInfoDetail.objects.values('title', 'href', 'publication_date', 'code').order_by(
            '-publication_date')
    total_num = cfb_informations.count()
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
                  {'cfb_informations': cfb_informations, 'pageRange': pageRange, 'restPages': restPages,
                   'itemNum': itemNum, 'total_num': total_num,'menu_open':menu_open,'code':code})
# 抓取
def callForBidCrawler(request):
    from management import crawler
    crawler.startCrawler()
    max_num = models.CFBInfoDetail.objects.count()
    return HttpResponse("抓取完毕~！共计%s条数据："%max_num)

