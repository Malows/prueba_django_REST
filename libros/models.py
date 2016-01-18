from django.db import models
from django.contrib.auth.models import User

class Libros( models.Model ):
    publicado = models.DateTimeField( auto_now_add = True )
    titulo = models.CharField( max_length = 100, blank = True, default = '')
    genero = models.CharField( max_length = 100, blank = True, default = '')
    ISBN = models.IntegerField( )
    owner = models.ForeignKey( 'auth.User', related_name ="libros" )

    class Meta:
        ordering = ('-publicado',)
