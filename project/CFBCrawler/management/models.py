from django.db import models

# Create your models here.
# #信息类别
# class CFBMenu(models.Model):
#     name = models.CharField(max_length=32)
# #工程类别
# class CFBType(models.Model):
#     name = models.CharField(max_length=32)
# #信息状态
# class CFBStatus(models.Model):
#     name = models.CharField(max_length=64)
#菜单表
class CFBMenuInfo(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)
    layer = models.IntegerField()
    url_length = models.IntegerField()
#招标信息详情
class CFBInfoDetail(models.Model):
    title = models.CharField(max_length=128)
    href = models.URLField(max_length=512)
    publication_date = models.DateField()
    code = models.CharField(max_length=64)
#菜单信息关联变
class info_m2m_menu(models.Model):
    info = models.ForeignKey(to='CFBInfoDetail',to_field='id')
    menu = models.ForeignKey(to='CFBMenuInfo',to_field='id')
    layer = models.IntegerField()

