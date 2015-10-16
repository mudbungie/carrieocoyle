# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150925_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='content',
        ),
        migrations.AlterField(
            model_name='piece',
            name='description',
            field=models.TextField(),
        ),
    ]
