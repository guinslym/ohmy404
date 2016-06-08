from .base import *

DEBUG = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'rest_framework',
    'bootstrap_pagination',
    'debug_toolbar',
    'easy_thumbnails',
    'taggit',
    'imagekit',
    'pipeline',
    'captcha',
    'applications.websites',
)

# LOGGING
LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s'
        },
        'normal': {
            'format': '%(levelname)s %(asctime)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
     },
     'handlers': {
         'file': {
             'level': 'INFO',
             'class': 'logging.FileHandler',
             'formatter': 'verbose',
             'filename': BASE_DIR+'/logs/dev.log',
             'mode': 'a',
         },
     },
     'loggers': {
         'django': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
         'applications.events.views': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
          'applications.events.models': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         '': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
     },
 }

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join('staticfiles')
STATIC_ROOT = os.path.join('staticfiles_dev')

#List of directories that Django could find my Static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

ALLOWED_HOSTS = ['*']



#Pipeline for staticfiles
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE = {
    'PIPELINE_ENABLED': False,
    'JAVASCRIPT': {
        'standard': {
            'source_filenames': {
                'applications.websites/templates/js/*.js',
            },
            'output_filename': 'js/std.js',
        },
    },
    'STYLESHEETS': {
        'standard': {
            'source_filenames': {
                'applications.websites/templates/css/*.css',
            },
            'output_filename': 'std.css',
        },
    },
}
