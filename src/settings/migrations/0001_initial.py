# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('playbook_path', models.CharField(max_length=200)),
            ],
        ),
    ]
