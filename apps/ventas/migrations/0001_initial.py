# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('categoria', models.CharField(max_length=30, choices=[(b'Fruta', b'Fruta'), (b'Liquidos', b'Liquidos'), (b'Congelado', b'Congelados'), (b'Carnes', b'Carnes')])),
                ('existencia', models.IntegerField()),
            ],
        ),
    ]
