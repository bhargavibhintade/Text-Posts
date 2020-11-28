# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r', '0044_commentreplies'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='replies',
            field=models.ManyToManyField(null=True, to='r.CommentReplies'),
        ),
        migrations.RemoveField(
            model_name='commentreplies',
            name='main_post',
        ),
        migrations.AddField(
            model_name='commentreplies',
            name='main_post',
            field=models.ManyToManyField(to='r.Comments'),
        ),
    ]
