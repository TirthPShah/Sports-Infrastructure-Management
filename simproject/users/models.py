# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from base.models import BaseProfile

from django.db import models

# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role

class User(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    membership_start_date = models.DateField(blank=True, null=True)
    membership_end_date = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=100, default='testing_password')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
