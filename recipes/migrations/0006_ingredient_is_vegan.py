# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-07 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20170302_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='is_vegan',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
