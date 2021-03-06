# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''

from django.conf.urls import include, url
from rest_framework import routers

from api.viewset.entry import (
    EntryViewSet, RecentEntryView, ArchiveEntryView,
    UserEntryView, FindViewSet
)
from api.viewset.comment import CommentViewSet, RecentCommentView
from api.viewset.tag import TagList, TagDetail, FollowingTagList
from api.viewset.friendship import FollowingViewSet, FollowedViewSet
from api.viewset.archive import ArchiveView

router = routers.DefaultRouter()
router.register(
    r'comments/(?P<entry>\d+)', CommentViewSet, base_name='comments')
router.register(r'find', FindViewSet, base_name='find')
router.register(r'entries', EntryViewSet, base_name='entries')
router.register(r'following', FollowingViewSet, base_name='following')
router.register(r'followed', FollowedViewSet, base_name='followed')
router.register(r'tagfollowing', FollowingTagList, base_name='tagfollowing')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tags/$', TagList.as_view()),
    url(r'^tags/(?P<id>\d+)/$', TagDetail.as_view()),
    url(r'^users/(?P<id>\d+)/$', UserEntryView.as_view()),
    url(r'^recententries/$', RecentEntryView.as_view()),
    url(r'^recentcomments/$', RecentCommentView.as_view()),
    url(r'^archives/$', ArchiveView.as_view()),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        ArchiveEntryView.as_view()),
]
