from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenRefreshView
from taller_mecanico.usuarios.views import LoginView, RegistroView, PerfilView

def api_root(request):
    return JsonResponse({
        "message": "Bienvenido a la API de Taller Mecánico Ali",
        "status": "online",
        "version": "1.0.0",
        "endpoints": {
            "auth": "/api/auth/",
            "clientes": "/api/clientes/",
            "vehiculos": "/api/vehiculos/",
            "servicios": "/api/servicios/",
            "ordenes": "/api/ordenes/",
            "facturas": "/api/facturas/",
            "pagos": "/api/pagos/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root-alt'),
    path('admin/', admin.site.urls),

    # ── Auth ──────────────────────────────────────────
    path('api/auth/login/',    LoginView.as_view(),   name='login'),
    path('api/auth/registro/', RegistroView.as_view(), name='registro'),
    path('api/auth/perfil/',   PerfilView.as_view(),   name='perfil'),
    path('api/auth/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),

    # ── Apps ──────────────────────────────────────────
    path('api/clientes/',  include('taller_mecanico.clientes.urls')),
    path('api/vehiculos/', include('taller_mecanico.vehiculos.urls')),
    path('api/servicios/', include('taller_mecanico.servicios.urls')),
    path('api/ordenes/',   include('taller_mecanico.ordenes.urls')),
    path('api/facturas/',  include('taller_mecanico.facturas.urls')),
    path('api/pagos/',     include('taller_mecanico.pagos.urls')),
]
