# creo este archivo
# importo modelos
from django.contrib.auth.models import User, Group
# esto que se llama serializers
from rest_framework import serializers

class UserSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Group
        fields = ('url', 'name')
