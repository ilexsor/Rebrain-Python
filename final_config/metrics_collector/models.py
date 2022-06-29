from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField('name', max_length=255)
    ip_address = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    description = models.TextField('description', max_length=255, default='no_description')

    class Meta:
        managed = True
        verbose_name = 'Client'


class Metrics(models.Model):
    host_info = models.TextField('host_info', max_length=1000, default='noname')
    disk_info = models.TextField('host_info', max_length=1000, default='noname')
    memory_info = models.TextField('host_info', max_length=1000, default='noname')
    cpu_info = models.TextField('host_info', max_length=1000, default='noname')
    load_avg = models.TextField('host_info', max_length=1000, default='noname')

    class Meta:
        managed = True
        verbose_name = 'Metrics'
