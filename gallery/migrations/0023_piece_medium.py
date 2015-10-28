# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0022_medium'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='medium',
            field=models.ForeignKey(default=0, to='gallery.Medium'),
        ),
    ]
