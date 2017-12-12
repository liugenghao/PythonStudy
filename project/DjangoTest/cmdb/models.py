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

class Books(models.Model):
    name = models.CharField(max_length=64)

class Author(models.Model):
    name = models.CharField(max_length=32)

class author_m2m_book(models.Model):
    aobj = models.ForeignKey(to='Author',to_field='id')
    bobj = models.ForeignKey(to='Books',to_field='id')