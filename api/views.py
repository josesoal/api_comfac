from django.db.models.query import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Categoria, SubCategoria, Producto, Proveedor, \
    CompraMaestro, CompraDetalle 
from . import serializer

class CategoriaViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all().order_by('descripcion')
    serializer_class = serializer.CategoriaSerializer

class SubCategoriaViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = SubCategoria.objects.all().order_by('descripcion')
    serializer_class = serializer.SubCategoriaSerializer

class ProductoViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all().order_by('descripcion')
    serializer_class = serializer.ProductoSerializer

class ProveedorViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = serializer.ProveedorSerializer

class CompraMaestroViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = CompraMaestro.objects.all().order_by('id')
    serializer_class = serializer.CompraMaestroSerializer

class CompraDetalleViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = CompraDetalle.objects.all().order_by('id')
    serializer_class = serializer.CompraDetalleSerializer
