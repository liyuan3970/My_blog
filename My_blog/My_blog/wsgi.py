"""
WSGI config for My_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
profile = os.environ.get('MY_BLOG_PROFILE', 'product')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_blog.settings.%s" % profile)
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_blog.settings")
application = get_wsgi_application()
