#!/usr/bin/python
# coding: utf-8
import os

from django.conf.urls import url
from django.conf import settings
from . import views
from glob import glob

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += [url(r'^{}/$'.format(name), views.static_site(file), name=name)
                for name, file in settings.STATIC_SITES.items()]

