# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20151027_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='medium',
        ),
    ]
