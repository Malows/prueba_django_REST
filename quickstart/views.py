# importo modelos
from django.contrib.auth.models import User, Group
# esto que se llama viewsets
from rest_framework import viewsets
# y los serializers
from quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet( viewsets.ModelViewSet ):
    """
    API endpoint que permite ver o editar.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet( viewsets.ModelViewSet ):
    """
    API endpoint que permite ver o editar.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
