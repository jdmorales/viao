# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.PositiveIntegerField()),
                ('lotes', models.PositiveIntegerField()),
                ('tipoMedida', models.CharField(max_length=3)),
                ('fechaRegsitro', models.DateField()),
                ('activo', models.BooleanField(default=True)),
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
                ('activo', models.BooleanField(default=True)),
                ('cultivo', models.ForeignKey(to='backend.Cultivo')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('documento', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('tipo_documento', models.CharField(max_length=20, choices=[(b'CC', b'Cedula Ciudadania'), (b'CE', b'Cedula Extranjera')])),
                ('tipo_usuario', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('direccion', models.CharField(max_length=30, null=True, blank=True)),
                ('fechaNacimiento', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('documento', models.OneToOneField(primary_key=True, serialize=False, to='backend.Persona')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jefe',
            fields=[
                ('documento', models.OneToOneField(primary_key=True, serialize=False, to='backend.Persona')),
                ('asignado', models.BooleanField()),
                ('activo', models.BooleanField(default=True)),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='backend.Dueno', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('documento', models.OneToOneField(primary_key=True, serialize=False, to='backend.Persona')),
                ('activo', models.BooleanField(default=True)),
                ('jefe', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='backend.Jefe', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='lote',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='backend.Trabajador', null=True),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='dueno',
            field=models.ForeignKey(to='backend.Dueno'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='jefe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='backend.Jefe'),
        ),
    ]
