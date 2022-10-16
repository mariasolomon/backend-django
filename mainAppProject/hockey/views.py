from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
#from hockey.serializers import AbstractUserSerializer, GroupSerializer
from hockey.serializers import JoueurSerializer, AbstractUserSerializer, GroupSerializer
from hockey.models import Joueur
from hockey.models import User

class AbstractUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all().order_by('-date_joined') 
    serializer_class = AbstractUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]