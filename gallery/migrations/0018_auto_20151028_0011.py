# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0017_auto_20151028_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='medium',
            new_name='medium2',
        ),
    ]
