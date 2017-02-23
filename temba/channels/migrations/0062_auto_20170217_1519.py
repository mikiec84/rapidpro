# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0061_channelcount_is_squashed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelsession',
            name='channel',
            field=models.ForeignKey(help_text='The channel that created this session', null=True, on_delete=django.db.models.deletion.CASCADE, to='channels.Channel'),
        ),
    ]