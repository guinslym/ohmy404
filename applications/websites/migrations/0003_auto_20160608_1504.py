# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_auto_20160607_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website404',
            name='author',
        ),
        migrations.RemoveField(
            model_name='website404',
            name='description',
        ),
        migrations.AlterField(
            model_name='website404',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='404/%Y/%m/%d', blank=True, null=True),
        ),
    ]
