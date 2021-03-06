# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identityApp', '0001_initial'),
        ('krsApp', '0004_krs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mhs_ambil_mk',
            name='id_mhs',
        ),
        migrations.RemoveField(
            model_name='mhs_ambil_mk',
            name='id_mk',
        ),
        migrations.RemoveField(
            model_name='krs',
            name='id_dosen',
        ),
        migrations.RemoveField(
            model_name='krs',
            name='id_mhs_ambil_mk',
        ),
        migrations.AddField(
            model_name='krs',
            name='ambil_di_smt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='krs',
            name='id_mk',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='krsApp.Mata_Kuliah'),
        ),
        migrations.AddField(
            model_name='krs',
            name='kelas',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('X', 'X')], default='A', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='krs',
            name='nik',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='identityApp.Dosen'),
        ),
        migrations.AddField(
            model_name='krs',
            name='nim',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='identityApp.Mahasiswa'),
        ),
        migrations.AlterField(
            model_name='mata_kuliah',
            name='id_mk',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Mhs_Ambil_MK',
        ),
    ]
