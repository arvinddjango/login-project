# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='terms',
            field=models.BooleanField(default=True),
        ),
    ]
