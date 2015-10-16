# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_documento',
            field=models.CharField(max_length=20, choices=[(b'CC', b'Cedula Ciudadania'), (b'CE', b'Cedual Extrangera')]),
        ),
        migrations.DeleteModel(
            name='Tipo_documento',
        ),
    ]
