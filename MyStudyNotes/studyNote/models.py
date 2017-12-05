from django.db import models

# Create your models here.
class MenusInfo(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=256)
    layer = models.IntegerField(null=True)
    parentID = models.IntegerField(null=True)
    left_child = models.IntegerField(null=True)
    right_sibling = models.IntegerField(null=True)
    status = models.IntegerField(default=0)
