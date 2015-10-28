# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_piece_medium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medium',
            name='medium_name',
            field=models.TextField(default='Medium'),
        ),
    ]
