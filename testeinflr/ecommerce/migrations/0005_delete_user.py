# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20170329_1334'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
