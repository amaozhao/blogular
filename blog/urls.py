# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.conf.urls import patterns, url
from blog.views import Home

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
)
