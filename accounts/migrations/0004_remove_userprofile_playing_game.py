# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180410_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='playing_game',
        ),
    ]
