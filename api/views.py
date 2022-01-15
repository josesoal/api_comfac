from django.db.models.query import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Categoria, SubCategoria, Producto, Proveedor, \
    CompraMaestro, CompraDetalle, Cliente, FacturaMaestro, FacturaDetalle
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

class ClienteViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = serializer.ClienteSerializer

    @action( 
        methods=['get'], detail=False, permission_classes=[], 
        url_path='by-name/(?P<nombre>[\w\ ]+)'
    )
    def by_name( self, request, pk=None, nombre=None ):
        obj = Cliente.objects.filter( nombre__icontains=nombre, estado=True )
        if not obj:
            return Response( {'detail' : 'No existe cliente buscado'} )
        c_serializer = serializer.ClienteSerializer( obj, many=True )
        return Response( c_serializer.data )

class FacturaMaestroViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = FacturaMaestro.objects.all().order_by('id')
    serializer_class = serializer.FacturaMaestroSerializer

class FacturaDetalleViewSet( viewsets.ModelViewSet ):
    #permission_classes = [IsAuthenticated]
    queryset = FacturaDetalle.objects.all().order_by('id')
    serializer_class = serializer.FacturaDetalleSerializer

    def create( self, request ):
        fd_serializer = serializer.FacturaDetalleSerializer( data=request.data )
        if fd_serializer.is_valid():
            data = request.data
            print(data)#---
            p = Producto.objects.get( pk=data['producto'] )
            if int( p.existencia ) >= int( data['cantidad'] ):
                fd_serializer.save()
                return Response( fd_serializer.data, status=status.HTTP_201_CREATED )
            else:
                print('No hay existencia suficiente')
                return Response('No hay existencia suficiente')
        return Response( fd_serializer.errors, status=status.HTTP_400_BAD_REQUEST )
