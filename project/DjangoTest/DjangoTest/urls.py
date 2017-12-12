"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'cmdb/',include("cmdb.urls"))
]
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^cmdb/', views.cmdb),
#     url(r'^login/',views.login),
#     url(r'^home/',views.Home.as_view()),
#     # url(r'^detail/', views.Detail.as_view()),
#     # url(r'^detail/(\d+).html', views.Detail.as_view()),
#     url(r'^detail/(?P<nid>\d+).html', views.Detail.as_view()),#(?P<nid>\d+)值固定传递给nid这个形参
#     url(r'^',views.Index.as_view(),name='index'),
# ]
