# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 18:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('r', '0043_auto_20170204_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True, verbose_name='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('instance', models.IntegerField(default=0, editable=False)),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('main_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r.Comments')),
            ],
        ),
    ]
