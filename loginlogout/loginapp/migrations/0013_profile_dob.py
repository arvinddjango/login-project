# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 05:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0012_auto_20190402_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
