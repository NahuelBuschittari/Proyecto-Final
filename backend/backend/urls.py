from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Ruta para registrar un nuevo usuario utilizando CreateUserView
    path('api/user/register/', CreateUserView.as_view(), name="register"),

    # Ruta para obtener un token de autenticación
    path('api/token/', TokenObtainPairView.as_view(), name="get_token"),

    # Ruta para refrescar un token de autenticación
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh"),

    # Ruta para las vistas de autenticación proporcionadas por Django REST Framework
    path('api-auth/', include("rest_framework.urls")),

    path('api/', include("api.urls"))
]
