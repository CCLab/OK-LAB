#!/usr/bin/python
# coding: utf-8


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^all/$', views.search, name='all'),
    url(r'^by_name/$', views.search, name='by_name'),
    url(r'^add/$', views.search, name='add'),

]
