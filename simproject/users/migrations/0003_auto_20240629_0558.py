# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-06-29 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240629_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='membership_type',
        ),
        migrations.DeleteModel(
            name='MembershipType',
        ),
    ]
