# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0028_auto_20171008_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
