# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0018_auto_20151028_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='medium2',
            new_name='medium',
        ),
    ]
