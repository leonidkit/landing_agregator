from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'smartwatch', 'smartwatch.urls', name='smartwatch'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'www', 'landing_agregator.urls', name='www'),
)