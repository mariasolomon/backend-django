# Generated by Django 4.1.2 on 2022-10-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hockey', '0010_joueur_isme_alter_joueur_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='joueur',
            name='manualPreference',
            field=models.CharField(blank=True, choices=[(1, 'Droitier'), (2, 'Gaucher')], max_length=8, null=True, verbose_name='Preference manuelle'),
        ),
    ]
