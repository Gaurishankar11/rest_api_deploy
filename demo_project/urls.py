from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^get_movie_details', get_movie_details),
	url(r'^add_movie_details', add_movie_details),
	url(r'^edit_movie_details', edit_movie_details),
	url(r'^delete_movie_details', delete_movie_details),
        ]
