# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-18 00:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0028_privatemessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrivateMessage',
        ),
    ]