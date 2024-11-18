from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from calendarV2app.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('calendarV2app.urls')),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
