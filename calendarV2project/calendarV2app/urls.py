from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from .views import (
    UsuarioViewSet,
    AsignaturaViewSet,
    UsuarioAsignaturaViewSet,
    HorarioViewSet,
    EventoViewSet,
    CalendarioViewSet,
    LoginView
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
    path('login/', TokenObtainPairView.as_view(), name='login'),
]