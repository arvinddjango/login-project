# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_profile_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
    ]
