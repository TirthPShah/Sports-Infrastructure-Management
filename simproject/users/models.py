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

class MembershipType(models.Model):
    type = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name

class User(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    membership_start_date = models.DateField(blank=True, null=True)
    membership_end_date = models.DateField(blank=True, null=True)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Admin(BaseProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'