from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from hockey.serializers import PlayerSerializer, AbstractUserSerializer, GroupSerializer, TeamSerializer, TimetableSerializer, AbstractMoralEntitySerializer, MatchSerializer, MatchResultSerializer, PartnerSerializer, ClubSerializer
from hockey.models import Player, Team, User, Timetable, AbstractMoralEntity, Match, MatchResult, Partner, Club

class AbstractUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all().order_by('-date_joined') 
    serializer_class = AbstractUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('-id') 
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-id') 
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('-id') 
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all().order_by('-id') 
    serializer_class = TimetableSerializer
    permission_classes = [permissions.IsAuthenticated]

class AbstractMoralEntityViewSet(viewsets.ModelViewSet):
    queryset = AbstractMoralEntity.objects.all().order_by('-id') 
    serializer_class = AbstractMoralEntitySerializer
    permission_classes = [permissions.IsAuthenticated]

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('-id') 
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticated]

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().order_by('-id') 
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

class MatchResultViewSet(viewsets.ModelViewSet):
    queryset = MatchResult.objects.all().order_by('-id') 
    serializer_class = MatchResultSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartnerSerializerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('-id') 
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]