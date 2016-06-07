# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website404',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='events/%Y/%m/%d', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='website404',
            name='screenshot',
            field=models.ImageField(upload_to='404/%Y/%m/%d', blank=True, null=True),
        ),
    ]
