# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0020_add_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='idv_piid',
            field=models.CharField(db_index=True, max_length=128, verbose_name='contract number'),
        ),
    ]
