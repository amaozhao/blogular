# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.conf.urls import patterns, include, url
from rest_framework import routers

from api.viewset.user import UserViewSet
from api.viewset.entry import EntryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
