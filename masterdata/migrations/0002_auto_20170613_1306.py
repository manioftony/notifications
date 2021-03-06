# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-13 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2),
        ),
        migrations.AddField(
            model_name='student',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
