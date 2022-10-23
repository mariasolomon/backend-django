# Generated by Django 4.1.2 on 2022-10-17 16:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('hockey', '0008_alter_joueur_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='joueur',
            name='height',
            field=models.IntegerField(blank=True, null=True, verbose_name='Taille'),
        ),
        migrations.AddField(
            model_name='joueur',
            name='weigth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Poids'),
        ),
        migrations.AlterField(
            model_name='joueur',
            name='phone',
            field=models.CharField(blank=True, max_length=30, validators=[django.core.validators.RegexValidator(regex='^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$')], verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='joueur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Adresse mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Prenom'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='auth.group', verbose_name='Groupes'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Actif'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nom'),
        ),
    ]