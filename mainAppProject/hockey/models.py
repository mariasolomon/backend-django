from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import Group

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from hockey.UserManager import UserManager
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator, validate_image_file_extension
from hockey.enumTypes import MANUAL_PREFERENCES, PLAYER_ROLE, TYPE_TIMETABLE, WEEK_DAY, SPECIAL_INFO

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Adresse mail'), unique=True)
    first_name = models.CharField(_('Prenom'), max_length=30, blank=True)
    last_name = models.CharField(_('Nom'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    groups = models.ManyToManyField(Group, verbose_name=_("Groupes"))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Player(models.Model):

    user = models.ForeignKey(User, parent_link=True, on_delete=models.CASCADE, verbose_name=_("Utilisateur"))
    phone = models.CharField(_('Telephone'), max_length=30, blank=True, validators=[RegexValidator(regex="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")])
    birthday = models.DateField(_('Date de naissance')) 
    location = models.CharField(_('Lieu de naissance'), max_length=30, blank=True)
    nationality = models.CharField(_('Nationalite'), max_length=30, blank=True) 
    height = models.IntegerField(_('Taille'), blank=True, null=True, validators=[MaxValueValidator(250), MinValueValidator(100)]) 
    weigth = models.IntegerField(_('Poids'), blank=True, null=True, validators=[MinValueValidator(15), MaxValueValidator(200)]) 
    manualPreference = models.CharField(_('Preference manuelle'), choices = MANUAL_PREFERENCES, max_length=8, blank=True, null=True)
    playerRole = models.CharField(('Role'), choices = PLAYER_ROLE, max_length=20, blank=True, null=True)
    isMe = models.BooleanField(_("C'est moi"), default=True)
    licence = models.FileField(upload_to='uploads/Player_files', blank=True, null=True)


class Team(models.Model):
    name = models.CharField(_("Nom de l'equipe"), max_length=255, blank=True)
    code = models.IntegerField(_("Code de l'equipe"), blank=True, null=True)
    players = models.ManyToManyField(Player, verbose_name=_("Joueur"))
    photo = models.ImageField(upload_to='uploads/Team_files', blank=True, null=True)
    captain = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name=_("Capitaine "), related_name='captain', null=True)
    assistant = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name=_("Assistant"), related_name='assistant', null=True)
    trainer = models.ForeignKey(Player, on_delete=models.CASCADE,verbose_name=_("Entreneur"), related_name='trainer', null=True)
    coach = models.ForeignKey(Player, on_delete=models.CASCADE,verbose_name=_("Coach"), related_name='coach', null=True)
    minAge = models.IntegerField(_("L'age minimal"), blank=True, null=True)
    maxAge = models.IntegerField(_("L'age maximal"), blank=True, null=True)
    
class Timetable(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Equipe")) 
    typeTimetable = models.CharField(_('Type horaire'), choices = TYPE_TIMETABLE, max_length=20, blank=True, null=True)
    day = models.CharField(_('Jour'), choices = WEEK_DAY, max_length=20, blank=True, null=True)
    startTime = models.TimeField(_('Heure de Debut'), blank=True, null=True)
    endTime = models.TimeField(_('Heure de fin'), blank=True, null=True)
    specialInfo = models.CharField(_('Informations spéciales'), choices = SPECIAL_INFO, max_length=20, blank=True, null=True) 

class AbstractMoralEntity(models.Model):
    logo = models.ImageField(upload_to='uploads/AbstractMoralEntity_files', blank=True, null=True)
    name = models.CharField(_('Nom'), max_length=255, blank=True, null=True)
    link = models.URLField(_('Link'))

class Club(models.Model):
    name = models.ForeignKey(AbstractMoralEntity, on_delete=models.CASCADE) 
    city = models.CharField(_('Ville'), max_length=255, blank=True, null=True)

class Match(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Equipe")) 
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name=_("Club")) 
    opposingTeam = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Equipe adverse"), related_name='opposed_team', blank=True, null=True) 
    dateTime = models.DateTimeField(_('Date et heure du match'), blank=True, null=True)
    atHome = models.BooleanField(_('Match à la maison?'), default=True)

class MatchResult(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name=_("Match")) 
    ourScore = models.IntegerField(_("Score de l'equipe maison"), blank=True, null=True) 
    theirScore = models.IntegerField(_("Score de l'equipe adverse"), blank=True, null=True) 
    matchPaper = models.FileField(_('Feuille de match'), upload_to='uploads/MatchResult_files', blank=True, null=True)

class Partner(models.Model):
    moralEntity = models.ForeignKey(AbstractMoralEntity, on_delete=models.CASCADE, verbose_name=_("Entité morale associe")) 
    
class ExternalLink(models.Model):
    name = models.CharField(_('Nom'), max_length=255, blank=True, null=True)
    link = models.URLField(_('Link'))
        
class Rink(models.Model):
    telephone = models.CharField(_('Telephone'), max_length=30, blank=True, validators=[RegexValidator(regex="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")])
    localisation = models.CharField(_('Localisation'), max_length=30, blank=True)
    email = models.EmailField(_('Adresse mail'), unique=True)
    link = models.URLField(_('Link'))
       