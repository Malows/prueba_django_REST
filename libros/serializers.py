from rest_framework import serializers
from libros.models import Libros
from django.contrib.auth.models import User

class LibrosSerializer( serializers.HyperlinkedModelSerializer ):
    owner = serializers.ReadOnlyField( source = 'owner.username' )

    class Meta:
        model = Libros
        fields = ( 'url', 'id', 'titulo', 'genero', 'ISBN', 'publicado', 'owner', )

class UsuarioSerializer( serializers.HyperlinkedModelSerializer ):
    libros = serializers.HyperlinkedRelatedField( many = True, view_name = 'libros-detail', read_only = True )
    # Un momento, todos?

    class Meta:
        model = User
        fields = ( 'url', 'id', 'username', 'libros', )
