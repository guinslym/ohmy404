# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class website404(TimeStampedModel):
    """
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=60, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text="Please write about what user will benefit from subscribing to this Event.")
    screenshot = models.ImageField(upload_to='404/%Y/%m/%d', null=True, blank=True)
    screenshot_thumbnail = ImageSpecField(source='screenshot',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    photo = ThumbnailerImageField(upload_to='404/%Y/%m/%d', resize_source=settings.DEFAULT_MASCOTA_IMAGE_SETTING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager(blank=True, help_text='Enter the Comma separated Taxonomy', verbose_name="标签", related_name="taxonomy")


    def __str__(self):
        return 'Title: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('websites:websites_detail', kwargs={'slug': self.slug})


    class Meta:
        app_label = 'websites'
        verbose_name = 'Website_404'
        verbose_name_plural = 'Websites_404'
        ordering = ('-created', )


class Suggestion(TimeStampedModel):
    """
    """
    website_404_url = models.URLField(blank=True, null=True)
