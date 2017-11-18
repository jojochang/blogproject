#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-18 00:51:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django.conf.urls import url 

from . import views

app_name = 'comments'
urlpatterns = [
	url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]
