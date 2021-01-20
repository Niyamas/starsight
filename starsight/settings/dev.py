from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())                 # https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar',                                        # For ddt
    'django_extensions',                                    # Enables python manage.py shell_plus in CMD
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',      # For ddt
]

INTERNAL_IPS = ('127.0.0.1', '172.17.0.1')                  # For ddt



STATIC_ROOT = os.path.join(BASE_DIR, 'static')





try:
    from .local import *
except ImportError:
    pass
