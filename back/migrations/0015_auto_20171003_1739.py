# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0014_tag_parent_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.Document')),
            ],
        ),
        migrations.AddField(
            model_name='privatedocument',
            name='qrcode',
            field=models.ImageField(default=None, upload_to='uploads/private/qrcode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicdocument',
            name='qrcode',
            field=models.ImageField(default=None, upload_to='uploads/public/qrcode'),
            preserve_default=False,
        ),
    ]
