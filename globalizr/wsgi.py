import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "globalizr.settings")

from django.core.wsgi import get_wsgi_application
#Heroku static files
from dj_static import Cling

application = Cling(get_wsgi_application())
