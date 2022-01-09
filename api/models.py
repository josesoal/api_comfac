from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Categoria( models.Model ):
    descripcion = models.CharField(
        max_length = 50,
        null = False,
        blank = False,
        unique = True
    )
    def __str__( self ):
        return self.descripcion
    
    def save( self, **kwargs ):
        self.descripcion = self.descripcion.upper()
        super( Categoria, self ).save()
    
    class Meta:
        verbose_name_plural = "categorias"

class SubCategoria( models.Model ):
    categoria = models.ForeignKey( Categoria, on_delete=models.CASCADE )
    descripcion = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )

    def __str__( self ):
        return "{} - {}".format( self.categoria, self.descripcion )
    
    def save( self, **kwargs ):
        self.descripcion = self.descripcion.upper()
        super( SubCategoria, self ).save()
    
    class Meta:
        verbose_name_plural = "sub categorias"
        unique_together = ( "categoria", "descripcion" )

class Producto( models.Model ):
    codigo = models.CharField(
        max_length = 10,
        null = False,
        blank = False
    )
    descripcion = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )
    existencia = models.IntegerField( default = 0 )
    precio = models.FloatField( default = 0 )
    subcategoria = models.ForeignKey( SubCategoria, on_delete=models.CASCADE )

    def __str__( self ):
        return self.descripcion

    def save( self, **kwargs ):
        self.descripcion = self.descripcion.upper()
        super( Producto, self ).save()
    
    class Meta:
        verbose_name_plural = "productos"

class Proveedor( models.Model ):
    nombre = models.CharField(
        max_length = 50,
        null = False,
        blank = False,
        unique = True
    )
    telefono = models.CharField(
        max_length = 20,
        null = True,
        blank = True
    )
    email = models.CharField(
        max_length = 20,
        null = True,
        blank = True
    )

    def __str__( self ):
        return self.nombre
    
    def save( self, **kwargs ):
        self.nombre = self.nombre.upper()
        super( Proveedor, self ).save()
    
    class Meta:
        verbose_name_plural = "proveedores"

class ModeloEdit( models.Model ):
    fecha_creacion = models.DateTimeField(
        auto_now_add=True #creates datetime just first time
    ) 
    fecha_modificacion = models.DateTimeField(
        auto_now=True #creates datetime in every modification
    )

    class Meta:
        abstract = True

class CompraMaestro( ModeloEdit ):
    fecha = models.DateField( null=False, blank=False )
    proveedor = models.ForeignKey( 
        Proveedor, 
        on_delete=models.CASCADE
    )

    def __str__( self ):
        return str( self.id )
    
    class Meta:
        verbose_name_plural = 'encabezados de compras'

class CompraDetalle( ModeloEdit ):
    cantidad = models.IntegerField( default=0 )
    precio = models.FloatField( default=0 )
    descuento = models.FloatField( default=0 )
    cabecera = models.ForeignKey( 
        CompraMaestro, 
        related_name='detalle', 
        on_delete=models.CASCADE 
    )
    producto = models.ForeignKey( Producto, on_delete=DO_NOTHING )

    @property
    def subtotal( self ):
        return self.cantidad * self.precio

    @property
    def total( self ):
        return self.subtotal - self.descuento
    
    def __str__(self):
        return '{}-{}-{}'.format( self.id, self.maestro, self.producto )
    
    class Meta:
        verbose_name_plural = 'detalles de compras'

# signals de compra
@receiver( post_save, sender=CompraDetalle )
def vigila_guardar_detalle_compra( sender, instance, **kwargs ):
    id_producto = instance.producto.id
    p = Producto.objects.get( id=id_producto )
    if (p):
        p.existencia = int(p.existencia) + int(instance.cantidad)
        p.save()

@receiver( post_delete, sender=CompraDetalle )
def vigila_eliminar_detalle_compra( sender, instance, **kwargs ):
    id_producto = instance.producto.id
    p = Producto.objects.filter( id=id_producto ).first()
    if (p):
        p.existencia = int(p.existencia) - int(instance.cantidad)
        p.save()

class Cliente( models.Model ):
    nombre = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True,
    )
    telefono = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    ) 
    email = models.TextField(
        null=True,
        blank=True,
    )
    estado =  models.BooleanField( default=True )

    def __str__( self ):
        return self.nombre
    
    def save( self, **kwargs ):
        self.nombre = self.nombre.upper()
        super( Cliente, self ).save()
    
    class Meta:
        verbose_name_plural = "clientes"



