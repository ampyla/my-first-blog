# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-25 10:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_commets'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commets',
            new_name='Comments',
        ),
    ]
