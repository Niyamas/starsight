from __future__ import absolute_import, unicode_literals

from .base import *
from decouple import config, Csv         # https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths


DEBUG = False

# Honor the 'X-Forwarded-Proto header for request.is_secure()
# See @ 10:00 - https://www.youtube.com/watch?v=RQ0eKv6HrpM
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())         # https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html



























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