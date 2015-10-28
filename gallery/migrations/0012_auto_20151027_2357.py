# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_remove_medium_medium_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='medium',
            name='medium_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='piece',
            name='medium',
            field=models.ForeignKey(default='', to='gallery.Medium'),
        ),
    ]
