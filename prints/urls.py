#!/usr/bin/python
# coding: utf-8


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^collection/$', views.collection, name='collection'),
    url(r'^by_name/$', views.by_name, name='by_name'),
    url(r'^add/$', views.add, name='add'),

]
