# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_remove_piece_medium'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medium',
        ),
    ]
