# Generated by Django 3.2.8 on 2021-12-06 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraMaestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedor')),
            ],
            options={
                'verbose_name_plural': 'encabezados de compras',
            },
        ),
        migrations.CreateModel(
            name='CompraDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('maestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='api.compramaestro')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.producto')),
            ],
            options={
                'verbose_name_plural': 'detalles de compras',
            },
        ),
    ]
