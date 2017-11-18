#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-17 20:56:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django import template
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
	return Category.objects.all()