from django.contrib.auth.models import Group
from rest_framework import serializers
from hockey.models import Player, User, Team, Timetable, AbstractMoralEntity, Match, MatchResult, Partner

class AbstractUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #model = User
        fields = ['url', 'email', 'date_joined', 'first_name', 'last_name', 'is_active', 'groups']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'user', 'phone', 'birthday', 'location', 'nationality', 'height', 'weigth', 'manualPreference', 'playerRole', 'isMe', 'licence']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'name', 'code', 'players', 'photo', 'captain', 'assistant', 'trainer', 'coach', 'minAge', 'maxAge']

class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timetable
        fields = ['url', 'team', 'typeTimetable', 'day', 'startTime', 'endTime', 'specialInfo']

class AbstractMoralEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbstractMoralEntity
        fields = ['url', 'name', 'logo', 'link']

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['url', 'team', 'club', 'dateTime', 'atHome']

class MatchResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatchResult
        fields = ['url', 'match', 'ourScore', 'theirScore', 'matchPaper']

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ['url', 'moralEntity']