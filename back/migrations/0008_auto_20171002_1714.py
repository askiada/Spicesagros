# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_category_subcategories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='category',
            name='subcategories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='back.Category'),
        ),
    ]