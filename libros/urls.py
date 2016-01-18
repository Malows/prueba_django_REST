from libros.views import LibrosViewSet, UsuarioViewSet, api_root
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

libros_list = LibrosViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
libros_detail = LibrosViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
usuarios_list = UsuarioViewSet.as_view({
    'get': 'list'
})
usuarios_detail = UsuarioViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns( [
    url( r'^$', api_root ),
    url( r'^libros/$', libros_list, name = 'libros-list' ),
    url( r'^libros/(?P<pk>[0-9]+)/$', libros_detail, name = 'libros-detail' ),
    url( r'^usuarios/$', usuarios_list, name = 'usuarios-list' ),
    url( r'^usuarios/(?P<pk>[0-9]+)/$', usuarios_detail, name = 'usuarios-detail' ),
] )
