from django.db import models


class TableOne(models.Model):
    project=models.CharField(max_length=100,verbose_name='工程')
    area=models.CharField(max_length=100,verbose_name='面积')


class TableTwo(models.Model):
    project=models.CharField(max_length=100,verbose_name='工程')
    area=models.CharField(max_length=100,verbose_name='面积')
