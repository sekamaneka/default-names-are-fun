"""
WSGI config for sexy_hunter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sexy_hunter.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
