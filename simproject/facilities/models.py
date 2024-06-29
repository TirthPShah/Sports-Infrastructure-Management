# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from users.models import User

# Create your models here.
class Facility(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100, null=True, blank=True)
    location_url = models.URLField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='facility_logos/', blank=True, null=True)
    facility_manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        # Ensure the associated user is a Facility Manager
        if self.facility_manager.role.role != 'FacilityManager':
            raise ValidationError('Selected user must have the role of Facility Manager.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Perform full clean check before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name