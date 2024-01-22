# New urls.py for this app

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import api_home
from .views import echo
from .views import random_object
from .views import random_object_rest
from .views import random_object_rest_serialize
from .views import post_req
# or from . import views


urlpatterns = [
    path('auth/', obtain_auth_token),
	path('home/', api_home),
	path('echo/', echo),
	path('random_object/', random_object),
	path('random_object_rest/', random_object_rest),
	path('random_object_rest_serialize/', random_object_rest_serialize),
	path('post_req/', post_req),

]
