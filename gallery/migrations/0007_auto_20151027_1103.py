# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20151027_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medium',
            name='medium_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='piece',
            name='medium',
            field=models.ForeignKey(to='gallery.Medium'),
        ),
    ]
