# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='latest_version',
        ),
        migrations.AddField(
            model_name='package',
            name='versions',
            field=models.ManyToManyField(default=None, related_name='versions', to='WEIPDCRM.Version', verbose_name='Versions'),
        ),
    ]