"""DjangoTest2 URL Configuration

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
from django.views.generic.base import RedirectView
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
    # url(r'^',include('app01.urls'))
    url(r'^$',views.login),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^userInfo/',views.userInfo,name='userInfo'),
    url(r'^addUser/',views.addUser,name='addUser'),
    url(r'^userTypeInfo/', views.userTypeInfo, name='userTypeInfo'),
    url(r'^addUserType/', views.addUserType, name='addUserType'),
    url(r'^deleteUserType/', views.deleteUserType, name='deleteUserType'),
    url(r'^deleteUser/', views.deleteUser, name='deleteUser'),
    url(r'^modifyUser/', views.modifyUser, name='modifyUser'),
    url(r'^bookInfo/',views.bookInfo,name='bookInfo')
]
