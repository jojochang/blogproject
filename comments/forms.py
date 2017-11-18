#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-17 22:47:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'url', 'text']
