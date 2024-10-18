from rest_framework import routers
from django.urls import path, include
from .views import (
    UsuarioViewSet,
    AsignaturaViewSet,
    UsuarioAsignaturaViewSet,
    HorarioViewSet,
    EventoViewSet,
    CalendarioViewSet
)

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'usuario_asignaturas', UsuarioAsignaturaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'eventos', EventoViewSet)
router.register(r'calendarios', CalendarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]