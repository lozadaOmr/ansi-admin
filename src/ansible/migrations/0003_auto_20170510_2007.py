# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0002_auto_20170510_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ansible_config_path',
            field=models.CharField(default=b'~/', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='playbook_path',
            field=models.CharField(default=b'~/', max_length=200),
        ),
    ]
