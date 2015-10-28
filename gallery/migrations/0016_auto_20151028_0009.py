# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0015_musician'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.AddField(
            model_name='piece',
            name='medium',
            field=models.ForeignKey(default=datetime.datetime(2015, 10, 28, 0, 9, 0, 214573, tzinfo=utc), to='gallery.Medium'),
            preserve_default=False,
        ),
    ]
