# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('sentat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='from_users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='to_users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='api.User'),
        ),
    ]
