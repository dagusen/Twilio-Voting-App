import os
import sys
sys.path = ['/var/www/pollapp'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'pollapp.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
