# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
from facilities.models import Facility
from users.models import User

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Booking(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.CharField(max_length=100)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_hour = models.DecimalField(max_digits=4, decimal_places=2)
    end_hour = models.DecimalField(max_digits=4, decimal_places=2)
    purpose = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.facility.name + ' - ' + self.user.name

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'