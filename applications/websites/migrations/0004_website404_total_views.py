# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_auto_20160608_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='website404',
            name='total_views',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
