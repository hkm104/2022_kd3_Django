from enum import Flag
from django.db import models

class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'army_shop'
        #이미 생서어되어 있는 테이블이므로
        managed = False

class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()