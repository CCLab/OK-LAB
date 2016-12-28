#!/usr/bin/python
# coding: utf-8

from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),

]

urlpatterns += [url(r'^{}/$'.format(name), views.static_site(file), name=name)
                for name, file in settings.STATIC_SITES.items()]

