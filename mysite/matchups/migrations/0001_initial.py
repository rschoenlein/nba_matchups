# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-30 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pts_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fga_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ft_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fta_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('drb_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('orb_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('stl_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ast_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('blk_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pf_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
                ('tov_per_g', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='current_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matchups.Team'),
        ),
    ]
