"""
WSGI config for cap1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import sys

sys.path.append('C:/zApache24/htdocs/<PROJECT-ROOT-DIRECTORY>')

import os, sys



path = os.path.abspath(__file__+'/../..')

if path not in sys.path:

    sys.path.append(path)



from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cap1.settings')

application = get_wsgi_application()
