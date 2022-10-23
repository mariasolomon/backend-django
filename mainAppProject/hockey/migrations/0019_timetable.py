# Generated by Django 4.1.2 on 2022-10-20 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hockey', '0018_rename_joueur_player_rename_equipe_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeTimetable', models.CharField(blank=True, choices=[(1, 'Entrainement'), (2, 'Match')], max_length=20, null=True, verbose_name='Type horaire')),
                ('day', models.CharField(blank=True, choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')], max_length=20, null=True, verbose_name='Jour')),
                ('startTime', models.TimeField(blank=True, null=True, verbose_name='Heure de Debut')),
                ('endTime', models.TimeField(blank=True, null=True, verbose_name='Heure de fin')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hockey.team')),
            ],
        ),
    ]