from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

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


# Deployment checklist: https://www.youtube.com/watch?v=_mgMth4im9E
""" SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool) """

#SECURE_HSTS_SECONDS = 31536000
""" SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=False, cast=bool)

SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)

SECURE_REFERRER_POLICY = config('SECURE_SSL_REDIRECT', default=None)

SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=False, cast=bool) """






try:
    from .local import *
except ImportError:
    pass
