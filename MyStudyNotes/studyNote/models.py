from django.db import models

# Create your models here.
class MenusInfo(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=256)
    layer = models.IntegerField(null=True)
    parentID = models.IntegerField(default=0)
    left_child = models.IntegerField(default=0)
    right_sibling = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
