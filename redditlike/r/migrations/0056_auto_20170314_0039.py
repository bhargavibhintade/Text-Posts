# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0055_auto_20170314_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscirbed',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscription_list', to='r.SubForum'),
        ),
    ]