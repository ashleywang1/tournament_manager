# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-13 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def create_school_tournament_registrations(apps, schema_editor):
    SchoolTournamentRegistration = apps.get_model(
            "tmdb", "SchoolTournamentRegistration")
    SchoolSeasonRegistration = apps.get_model(
            "tmdb", "SchoolSeasonRegistration")
    for tournament_reg in SchoolTournamentRegistration.objects.all():
        tournament_reg.school = tournament_reg.school_season_registration.school
        tournament_reg.save()

def delete_school_tournament_registrations(apps, schema_editor):
    SchoolTournamentRegistration = apps.get_model(
            "tmdb", "SchoolTournamentRegistration")
    for tournament_reg in SchoolTournamentRegistration.objects.all():
        tournament_reg.school = None
        tournament_reg.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0013_create_school_season_registration'),
    ]

    operations = [
        migrations.RunPython(delete_school_tournament_registrations,
                create_school_tournament_registrations),
        migrations.RemoveField(
            model_name='schooltournamentregistration',
            name='school',
        ),
    ]
