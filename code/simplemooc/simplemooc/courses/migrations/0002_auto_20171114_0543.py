# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Bitch', 'verbose_name_plural': 'Bitches'},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Image'),
        ),
    ]
