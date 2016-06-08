from django.contrib import admin

# Register your models here.
from .models import website404


class website404Admin(admin.ModelAdmin):
    #list_display = ('title', 'slug',)
    #list_filter = ('status', 'created', 'publish', 'author')
    #search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ['status', 'publish'] 

admin.site.register(website404, website404Admin)
