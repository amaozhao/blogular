# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.conf.urls import patterns, include, url
from rest_framework import routers

from api.viewset.user import UserViewSet
from api.viewset.entry import (
    EntryViewSet, RecentEntryView, FindViewSet
)
from api.viewset.comment import CommentViewSet
from api.viewset.auth import AuthUserView, SignInView, SignOutView
from api.viewset.tag import TagViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'comments/(?P<entry>\d+)', CommentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'find', FindViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^recententries/$', RecentEntryView.as_view()),
    url(r'^auth-user/$', AuthUserView.as_view()),
    url(r'^auth/signin/$', SignInView.as_view()),
    url(r'^auth/signout/$', SignOutView.as_view()),
)
