# Generated by Django 3.2.8 on 2022-01-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211207_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
