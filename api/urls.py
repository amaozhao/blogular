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
from api.viewset.tag import TagList, TagDetail, FollowingTagList
from api.viewset.friendship import FollowingViewSet, FollowedViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'comments/(?P<entry>\d+)', CommentViewSet, base_name='comments')
router.register(r'find', FindViewSet, base_name='find')
router.register(r'entries', EntryViewSet, base_name='entries')
router.register(r'following', FollowingViewSet, base_name='following')
router.register(r'followed', FollowedViewSet, base_name='followed')
router.register(r'tagfollowing', FollowingTagList, base_name='tagfollowing')

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^tags/$', TagList.as_view()),
    url(r'^tags/(?P<id>\d+)/$', TagDetail.as_view()),
    url(r'^recententries/$', RecentEntryView.as_view()),
    url(r'^auth-user/$', AuthUserView.as_view()),
    url(r'^auth/signin/$', SignInView.as_view()),
    url(r'^auth/signout/$', SignOutView.as_view()),
)
