# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_medium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medium',
            name='medium_name',
        ),
    ]
