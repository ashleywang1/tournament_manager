# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-10 16:25
from __future__ import unicode_literals

from django.db import migrations, models

def create_slug(apps, schema_editor):
    Season = apps.get_model("tmdb", "Season")
    for season in Season.objects.all():
        season.slug = '%d-%d' %(season.start_date.year, season.end_date.year)
        season.save()

def delete_slug(apps, schema_editor):
    Season = apps.get_model("tmdb", "Season")
    for season in Season.objects.all():
        season.slug = None
        season.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0014_remove_tournament_registration_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.RunPython(create_slug, delete_slug),
        migrations.AlterField(
            model_name='season',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
