# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20151203_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nome_empresa',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
