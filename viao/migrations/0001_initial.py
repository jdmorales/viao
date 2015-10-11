# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.IntegerField()),
                ('tipoMedida', models.CharField(max_length=3)),
                ('fechaRegsitro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perfil', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jefe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perfil', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.IntegerField()),
                ('tipoMedida', models.CharField(max_length=3)),
                ('totalEstacas', models.IntegerField()),
                ('fechaRegsitro', models.DateField()),
                ('cultivo', models.ForeignKey(to='viao.Cultivo')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('documento', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('tipo_documento', models.CharField(max_length=2, choices=[(b'TI', b'Tarjeta de identidad'), (b'CC', b'Cedula de ciudadania')])),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('passw', models.CharField(max_length=20)),
                ('fechaRegistro', models.DateField()),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perfil', models.CharField(max_length=10)),
                ('documento', models.ForeignKey(to='viao.Persona')),
                ('jefe', models.ForeignKey(to='viao.Jefe')),
            ],
        ),
        migrations.AddField(
            model_name='lote',
            name='trabajador',
            field=models.ForeignKey(to='viao.Trabajador'),
        ),
        migrations.AddField(
            model_name='jefe',
            name='documento',
            field=models.ForeignKey(to='viao.Persona'),
        ),
        migrations.AddField(
            model_name='jefe',
            name='dueno',
            field=models.ForeignKey(to='viao.Dueno'),
        ),
        migrations.AddField(
            model_name='dueno',
            name='documento',
            field=models.ForeignKey(to='viao.Persona'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='dueno',
            field=models.ForeignKey(to='viao.Dueno'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='jefe',
            field=models.ForeignKey(to='viao.Jefe'),
        ),
    ]
