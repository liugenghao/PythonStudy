from django.db import models

# Create your models here.
class MenusInfo(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=256)
    parentID = models.IntegerField()
    left_child = models.IntegerField()
    right_sibling = models.IntegerField()
    layer = models.IntegerField