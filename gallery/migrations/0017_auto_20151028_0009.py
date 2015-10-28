# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0016_auto_20151028_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='medium',
            field=models.TextField(),
        ),
    ]
