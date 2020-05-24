# Pg. 413 - unmodified
"""Defines URL patterns for main_app.""" 
from django.conf.urls import url
from . import views

urlpatterns = [ 
    # Home page
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'), 
]