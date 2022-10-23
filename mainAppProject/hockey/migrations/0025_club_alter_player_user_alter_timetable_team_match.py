# Generated by Django 4.1.2 on 2022-10-23 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hockey', '0024_alter_timetable_specialinfo_delete_specialinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ville')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hockey.abstractmoralentity')),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hockey.team', verbose_name='Equipe'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hockey.club', verbose_name='Club')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hockey.team', verbose_name='Equipe')),
            ],
        ),
    ]
