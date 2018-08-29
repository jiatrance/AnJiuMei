from django.db import models


class TableOne(models.Model):
    project=models.CharField(max_length=100,verbose_name='工程')
    area=models.CharField(max_length=100,verbose_name='面积')

    class Meta:
        verbose_name='工程1'
        verbose_name_plural=verbose_name


class TableTwo(models.Model):
    project=models.CharField(max_length=100,verbose_name='工程')
    area=models.CharField(max_length=100,verbose_name='面积')

    class Meta:
        verbose_name='工程2'
        verbose_name_plural=verbose_name


class SystemType(models.Model):
    name=models.CharField(max_length=100,verbose_name='ID',default='')
    types=models.CharField(max_length=100,verbose_name='产品类型',default='')

    class Meta:
        verbose_name='产品类型'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.types


class TypeImage(models.Model):
    the_type=models.ForeignKey(SystemType,verbose_name='产品类型',on_delete=models.CASCADE)
    image = models.ImageField('详情', upload_to='img/%Y%M', max_length=100, null=True,
                              blank=True)

    class Meta:
        verbose_name='详情'
        verbose_name_plural=verbose_name