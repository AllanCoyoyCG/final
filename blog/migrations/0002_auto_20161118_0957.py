# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fecha_devolucion_propuesta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
