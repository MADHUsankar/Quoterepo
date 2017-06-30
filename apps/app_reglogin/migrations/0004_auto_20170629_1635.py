# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_reglogin', '0003_user_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='alias',
        ),
        migrations.AddField(
            model_name='user',
            name='emailid',
            field=models.CharField(default=django.utils.timezone.now, max_length=78),
            preserve_default=False,
        ),
    ]
