# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 21:49
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0024_auto_20171005_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='back.Category'),
        ),
    ]
