from libros.models import Libros
from django.contrib.auth.models import User
from libros.serializers import LibrosSerializer, UsuarioSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from libros.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

class UsuarioViewSet( viewsets.ReadOnlyModelViewSet ):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class LibrosViewSet( viewsets.ModelViewSet ):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

    def perform_create( self, serializer ):
        serializer.save( owner = self.request.user )

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'Usuarios': reverse( 'usuarios-list', request = request, format = format ),
        'Libros': reverse( 'libros-list', request = request, format = format ),
    })
