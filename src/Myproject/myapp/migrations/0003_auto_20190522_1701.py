# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_profilefielditem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profilefielditem',
            new_name='Profilefeeditem',
        ),
    ]