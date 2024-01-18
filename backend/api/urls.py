# New urls.py for this app

from django.urls import path

from .views import api_home
from .views import echo
from .views import random_object
# or from . import views


urlpatterns = [
	path('home/', api_home),
	path('echo/', echo),
	path('random_object/', random_object),

]
