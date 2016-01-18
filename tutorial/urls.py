"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# agrego el import de include
from django.conf.urls import url, include
from django.contrib import admin
# agrego el router
from rest_framework import routers
# e importo las views
from quickstart.views import UserViewSet, GroupViewSet
from libros.views import LibrosViewSet, UsuarioViewSet


# Creo que preseteo las rutas de la API con sus querysets en las vistas
router = routers.DefaultRouter()
router.register( r'Usuarios', UsuarioViewSet )
router.register( r'Libros', LibrosViewSet )
router.register( r'users', UserViewSet )
router.register( r'groups', GroupViewSet )

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('libros.urls')),
    url(r'^', include(router.urls)),
    # Para hacer necesario el loggeo, y que no cualquiera use la API para hacer chanchadas
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
