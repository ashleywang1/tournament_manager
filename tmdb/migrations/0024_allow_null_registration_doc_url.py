# Generated by Django 2.2.4 on 2019-09-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmdb', '0023_rename_weightclass_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooltournamentregistration',
            name='registration_doc_url',
            field=models.URLField(blank=True, null=True, unique=False),
        ),
    ]
