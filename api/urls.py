from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register( r'categoria', views.CategoriaViewSet )
router.register( r'subcategoria', views.SubCategoriaViewSet )
router.register( r'producto', views.ProductoViewSet )
router.register( r'proveedor', views.ProveedorViewSet )
router.register( r'compra', views.CompraMaestroViewSet )
router.register( r'compra-detalle', views.CompraDetalleViewSet )
router.register( r'cliente', views.ClienteViewSet )
router.register( r'factura', views.FacturaMaestroViewSet )
router.register( r'factura-detalle', views.FacturaDetalleViewSet )


urlpatterns = [
    path( '', include(router.urls) ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

