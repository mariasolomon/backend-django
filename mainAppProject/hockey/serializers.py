from django.contrib.auth.models import User, Group
from rest_framework import serializers
#from hockey.models import Joueur
from hockey.models import Joueur, User


class AbstractUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #model = User
        fields = ['url', 'email', 'date_joined', 'first_name', 'last_name', 'is_active']


class JoueurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Joueur
        fields = ['url', 'user_id', 'phone', 'birthday', 'location', 'country']

"""class JouerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'password', 'email', 'groups']
"""


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
