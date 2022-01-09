from rest_framework import serializers
from .models import Categoria, SubCategoria, Producto, Proveedor, \
    CompraMaestro, CompraDetalle, Cliente

class CategoriaSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubCategoriaSerializer( serializers.ModelSerializer ):
    cat_descripcion = serializers.ReadOnlyField(
        source='categoria.descripcion'
    )
    class Meta:
        model = SubCategoria
        fields = ['id','categoria','descripcion','cat_descripcion']

class ProductoSerializer( serializers.ModelSerializer ):
    scat_descripcion = serializers.ReadOnlyField(
        source='subcategoria.descripcion'
    )
    class Meta:
        model = Producto
        fields = [
            'id', 'codigo', 'descripcion', 'existencia', 'precio',
            'subcategoria','scat_descripcion'
        ]

class ProveedorSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Proveedor
        fields = '__all__'

class CompraDetalleSerializer( serializers.ModelSerializer ):
    producto_descripcion = serializers.ReadOnlyField(
        source='producto.descripcion'
    )
    class Meta:
        model = CompraDetalle
        fields = [
            'id', 'cantidad', 'precio', 'descuento', 'cabecera', 
            'producto', 'subtotal', 'total', 'producto_descripcion'
        ]

class CompraMaestroSerializer( serializers.ModelSerializer ):
    detalle = CompraDetalleSerializer( many=True, read_only=True )
    class Meta:
        model = CompraMaestro
        fields = ['id', 'fecha', 'proveedor', 'detalle']

class ClienteSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Cliente
        fields = '__all__'