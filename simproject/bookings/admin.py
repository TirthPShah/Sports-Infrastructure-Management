# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Booking, Status

# Register your models here.

admin.site.register(Booking)
admin.site.register(Status)