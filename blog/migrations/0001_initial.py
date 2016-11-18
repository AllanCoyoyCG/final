# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('libro', models.ForeignKey(to='blog.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('dpi', models.CharField(max_length=40)),
                ('libros', models.ManyToManyField(through='blog.Prestamo', to='blog.Libro')),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='usuario',
            field=models.ForeignKey(to='blog.Usuario'),
        ),
    ]
