from __future__ import absolute_import, unicode_literals
from .base import *

# @39:00: https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17
import django_heroku


DEBUG = True


# Whitenoise docs: http://whitenoise.evans.io/en/stable/django.html
INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',        # Disable Django's default statif file handling and let Whitenoise do it
]


MIDDLEWARE += [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


# See: https://stackoverflow.com/questions/17636074/operationalerror-could-not-connect-to-server
""" import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
} """





# For whitenoise
# See: https://wagtail.io/blog/deploying-wagtail-heroku/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

""" COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content' """


















# Honor the 'X-Forwarded-Proto header for request.is_secure()
# See @ 10:00 - https://www.youtube.com/watch?v=RQ0eKv6HrpM
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())         # https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html


# Let static files be served by whitenoise
# https://github.com/heroku/django-heroku/issues/25
#django_heroku.settings(locals(), staticfiles=False)                    # @39:00: https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17
django_heroku.settings(locals())                    # @39:00: https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17


#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # For Heroku


















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