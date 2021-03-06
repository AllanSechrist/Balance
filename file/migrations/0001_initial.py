# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('classification', models.CharField(max_length=250)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.Folder')),
            ],
        ),
    ]
