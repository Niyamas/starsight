from __future__ import absolute_import, unicode_literals
from .base import *

# @39:00: https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17
import django_heroku


DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())         # https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html


# Whitenoise docs: http://whitenoise.evans.io/en/stable/django.html
INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',        # Disable Django's default static file handling and let Whitenoise do it
]


# For whitenoise
# See: https://wagtail.io/blog/deploying-wagtail-heroku/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Let static files be served by whitenoise
django_heroku.settings(locals())                    # @39:00: https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17
#django_heroku.settings(locals(), staticfiles=False)



# Honor the 'X-Forwarded-Proto header for request.is_secure()
# See @ 10:00 - https://www.youtube.com/watch?v=RQ0eKv6HrpM
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


















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