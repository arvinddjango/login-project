# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_profile_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=10),
        ),
    ]
