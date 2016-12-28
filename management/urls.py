#!/usr/bin/python
# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manage, name='management'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
]
