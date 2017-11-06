# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0017_auto_20171004_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parent_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='back.Tag'),
        ),
    ]