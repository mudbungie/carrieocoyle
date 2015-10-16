# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='image',
            field=models.ImageField(upload_to='', default='/static/signature.jpg'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=255),
        ),
    ]
