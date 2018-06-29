# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *


class Satisfaction_View(View):
    def get(self, request):
        # table of satisfaction 满意度表
        ts = Satisfaction.objects.all()
        return render(request, 'satisfaction.html', {'ts': ts})
