# Generated by Django 4.1.2 on 2022-10-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hockey', '0023_abstractmoralentity_alter_player_licence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='specialInfo',
            field=models.CharField(blank=True, choices=[(1, '(*) RDV 1h15 avant pour la séance'), (2, '(**) shooters sur convocation'), (3, 'HG = Hors Glace')], max_length=20, null=True, verbose_name='Informations spéciales'),
        ),
        migrations.DeleteModel(
            name='SpecialInfo',
        ),
    ]
