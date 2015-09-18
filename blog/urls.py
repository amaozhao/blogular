# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.conf.urls import url
from blog.views import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^[a-zA-Z]*', Home.as_view(), name='home'),
]
