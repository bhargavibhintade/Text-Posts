# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0036_comments_default_instance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentreplies',
            name='comments_ptr',
        ),
        migrations.DeleteModel(
            name='CommentReplies',
        ),
    ]