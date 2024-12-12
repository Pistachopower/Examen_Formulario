# Generated by Django 5.1.4 on 2024-12-12 10:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0002_alter_promociones_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promociones',
            name='fecha_Promocion',
        ),
        migrations.AddField(
            model_name='promociones',
            name='descripcion',
            field=models.CharField(default='vacio', max_length=100),
        ),
        migrations.AddField(
            model_name='promociones',
            name='descuento',
            field=models.FloatField(db_column='Descuento', default=0.0),
        ),
        migrations.AddField(
            model_name='promociones',
            name='fecha_Fin_Promocion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='promociones',
            name='fecha_Inicio_Promocion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='promociones',
            name='codigo',
            field=models.IntegerField(null=True),
        ),
    ]
