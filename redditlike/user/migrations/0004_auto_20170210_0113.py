# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-10 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170209_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentkarmapoints',
            name='has_voted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='threadkarmapoints',
            name='has_voted',
            field=models.BooleanField(default=False),
        ),
    ]