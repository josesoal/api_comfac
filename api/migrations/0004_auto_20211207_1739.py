# Generated by Django 3.2.8 on 2021-12-07 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_compradetalle_compramaestro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compradetalle',
            old_name='maestro',
            new_name='cabecera',
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compradetalle',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
