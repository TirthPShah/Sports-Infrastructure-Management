# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-06-29 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='membership_end_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='membership_start_date',
        ),
    ]
