from django.db import models

# Create your models here.
from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField('标题',max_length=20)
    bpub_date = models.DateTimeField('时间')
    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = "书籍信息"

class HeroInfo(models.Model):
    hname = models.CharField('英雄',max_length=20)
    hgender = models.BooleanField('男')
    hcontent = models.CharField('介绍',max_length=100)
    hBook = models.ForeignKey('BookInfo')
    def __str__(self):
        return self.hname