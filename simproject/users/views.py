# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def aboutus(request):
    return render(request, 'aboutus.html')
