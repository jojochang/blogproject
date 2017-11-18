#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-17 14:41:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django.conf.urls import url 
from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$',views.category, name='category'),

]
