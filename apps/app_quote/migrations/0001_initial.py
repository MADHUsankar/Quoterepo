# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_reglogin', '0003_user_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotetext', models.TextField(max_length=1000)),
                ('quotedby', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favquotes', models.ManyToManyField(related_name='favquotes', to='app_reglogin.User')),
                ('quotecreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotecreators', to='app_reglogin.User')),
            ],
        ),
    ]
