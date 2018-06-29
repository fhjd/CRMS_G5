# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 满意度
class Satisfaction(models.Model):
    # Satisfaction of results 处理结果满意度
    sor = models.CharField(max_length=100)
    # Service satisfaction 服务满意度
    ss = models.CharField(max_length=100)

    def __unicode__(self):
        return '满意度：%s'%self.sor
    class Meta:
        db_table='t_satisfaction'