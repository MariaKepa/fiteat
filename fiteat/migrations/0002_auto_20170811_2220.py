# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiteat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pathtopicture',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
