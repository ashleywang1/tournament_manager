# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-29 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0007_rename_team'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TournamentDivision',
            new_name='TournamentSparringDivision',
        ),
        migrations.RenameModel(
            old_name='TournamentDivisionBeltRanks',
            new_name='TournamentSparringDivisionBeltRanks',
        ),
    ]