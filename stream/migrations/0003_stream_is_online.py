# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_stream_streamkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
