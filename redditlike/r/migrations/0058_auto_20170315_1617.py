# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-15 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0057_auto_20170314_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreplies',
            name='has_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comments',
            name='has_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='posttext',
            name='has_read',
            field=models.BooleanField(default=False),
        ),
    ]
