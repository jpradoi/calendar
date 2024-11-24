from rest_framework import routers
from django.urls import path, include
from .views import (
    UsuarioViewSet,
    AsignaturaViewSet,
    UsuarioAsignaturaViewSet,
    HorarioViewSet,
    EventoViewSet,
    CalendarioViewSet,
    login_docente,
    get_asignaturas_para_dia,
    get_eventos_para_dia,
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
    path('login/', login_docente, name='login'),
    path('api/asignaturas/por_dia/', get_asignaturas_para_dia, name='get_asignaturas_para_dia'),
    path('api/eventos/para_dia/', get_eventos_para_dia, name='get_eventos_para_dia')
]