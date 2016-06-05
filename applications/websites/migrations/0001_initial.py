# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('website_404_url', models.URLField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='website404',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('title', models.CharField(null=True, blank=True, max_length=60)),
                ('url', models.URLField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True, help_text='Please write about what user will benefit from subscribing to this Event.')),
                ('screenshot', models.ImageField(null=True, blank=True, upload_to='events/%Y/%m/%d')),
                ('slug', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10, default='draft')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', help_text='Enter the Comma separated Taxonomy', verbose_name='标签', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Website_404',
                'verbose_name_plural': 'Websites_404',
            },
        ),
    ]
