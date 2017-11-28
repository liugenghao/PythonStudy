from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    pwd = models.CharField(max_length=32,verbose_name='密码')
    email = models.CharField(max_length=32,verbose_name='邮箱')
    gender = models.CharField(max_length=10,null=True,verbose_name='性别')
    createTime = models.DateField(auto_now_add=True,null=True)
    updateTime = models.DateField(auto_now=True,null=True)
    user_type = models.ForeignKey(UserType)#约束
#书
class Books(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    abstract = models.TextField(max_length=500)
    createTime = models.DateField(auto_now_add=True)
    updateTime = models.DateField(auto_now=True)
#作者
class Authors(models.Model):
    name = models.CharField(max_length=32)
#作者书籍关联表
class author_m2m_book(models.Model):
    aobj = models.ForeignKey(to='Authors',to_field='id')
    bobj = models.ForeignKey(to='Books',to_field='id')

#淘宝美食
class Food(models.Model):
    title = models.CharField(max_length=128)
    shopname = models.CharField(max_length=128)
    location = models.CharField(max_length=16)
    deal = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    image_url = models.CharField(max_length=256)