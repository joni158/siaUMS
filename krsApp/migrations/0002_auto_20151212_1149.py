# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mata_kuliah',
            name='jumlah_sks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mata_kuliah',
            name='mk_semester',
            field=models.IntegerField(),
        ),
    ]
