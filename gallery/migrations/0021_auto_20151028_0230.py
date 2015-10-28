# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0020_auto_20151028_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='medium',
        ),
        migrations.DeleteModel(
            name='Medium',
        ),
    ]
