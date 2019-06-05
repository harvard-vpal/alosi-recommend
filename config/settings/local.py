"""
Example Django settings for local development environment
"""

from config.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oiut#=u&f8@g@(_@c2$njw7157@_ldxi_!lkw1@wsd9g6+8@zf'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recommend',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'sslserver'
]

# django-cors-headers settings
# https://github.com/ottoyiu/django-cors-headers#configuration
# You may want to explicitly specify allowed origin hostnames in production with CORS_ORIGIN_WHITELIST.
CORS_ORIGIN_ALLOW_ALL = True

# adaptive engine settings
ENGINE_URL = os.getenv('ENGINE_URL', 'http://engine:8000')
ENGINE_TOKEN = os.getenv('ENGINE_TOKEN', '5ea0b01ea8ee0fc0b7cc47160cf4c91fe0447779')
DEFAULT_TOOL_CONSUMER_INSTANCE_GUID = os.getenv('DEFAULT_TOOL_CONSUMER_INSTANCE_GUID', 'openedx.gse.harvard.edu')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'event': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}