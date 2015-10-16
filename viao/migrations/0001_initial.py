# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
            ],
        ),
        migrations.CreateModel(
            name='Jefe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('documento', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('tipo_usuario', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('direccion', models.CharField(max_length=20, null=True, blank=True)),
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
            name='Tipo_documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=20, choices=[(b'CC', b'Cedula Ciudadania'), (b'CE', b'Cedual Extrangera')])),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.ForeignKey(to='viao.Persona')),
                ('jefe', models.ForeignKey(to='viao.Jefe')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_documento',
            field=models.ForeignKey(to='viao.Tipo_documento'),
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
            field=models.OneToOneField(to='viao.Jefe'),
        ),
    ]
