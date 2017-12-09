from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from management import models

# Create your views here.


def callForBidInfo(request):
    cfb_informations = models.CFBInfoDetail.objects.all()
    return render(request, 'call_for_bid_info.html',{'cfb_informations':cfb_informations})

# 抓取
def callForBidCrawler(request):
    from management import crawler
    crawler.startCrawler()
    # return HttpResponse(request)
    return render(request, 'call_for_bid_info.html')
