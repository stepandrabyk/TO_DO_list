# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-16 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='task',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
